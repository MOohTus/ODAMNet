#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Morgane T. and Ozan O.

Script of methods that we can apply to CTD and WP lists
Adapted from overlapAnalysis.py from Ozan O. (Paper vitamin A)
"""

# Libraries
import requests
import os
import multixrank
import pandas as pd
from scipy.stats import hypergeom
from statsmodels.stats.multitest import multipletests
from alive_progress import alive_bar


# Functions
def overlap(targetGeneSet, WPGenesDict, WPBackgroundGenesSet, chemNames, WPDict, outputPath):
    """
    Calculate overlap between target genes and Rase Diseases WP

    Metrics :
        - M is the population size (Nb of genes inside WikiPathway for Homo sapiens pathways)
        - n is the number of successes in the population (Nb of genes inside the selected RD WP)
        - N is the sample size (Nb of genes shared between target list (from chemical) and background genes from WP)
        - x is the number of drawn “successes” (Nb of genes shared between target list and RD WP)

    :param set targetGeneSet: Set of HGNC targets
    :param dict WPGenesDict: Dictionary of Rare Diseases WP
    :param set WPBackgroundGenesSet: Set of all HGNC inside WikiPathway for Homo sapiens
    :param str chemNames: MeSH ID of chemical of interest
    :param dict WPDict: Dictionary of WP composed of title of them
    :param str outputPath: Folder path to save the results

    :return:
        - **df** (*pd.DataFrame*) – Data frame of overlap metrics for each rare diseases WP
    """
    # Parameters
    WPIDs = []
    WPTitles = []
    WPsizes = []
    TargetSizes = []
    intersectionSizes = []
    universSizes = []
    pValues = []
    intersections = []

    # Calculate pvalue overlap for each RD WP found
    for WP in WPGenesDict:
        if WP != "WPID":
            WPGeneSet = set(WPGenesDict[WP])

            # Metrics calculation
            M = len(WPBackgroundGenesSet)
            n = len(WPGeneSet)
            N = len(targetGeneSet.intersection(WPBackgroundGenesSet))  # Taking only genes that are also in background
            intersection = list(WPGeneSet.intersection(targetGeneSet))
            x = len(intersection)
            # print(M, n, N, x)

            # Hyper geometric test
            pval = hypergeom.sf(x - 1, M, n, N)

            # Fill variable to store information and metrics
            WPIDs.append(WP)
            WPTitles.append(WPDict[WP])
            WPsizes.append(n)
            TargetSizes.append(N)
            intersectionSizes.append(x)
            universSizes.append(M)
            pValues.append(pval)
            intersection.sort()
            intersections.append(' '.join(intersection))

    # Multiple tests to correct pvalue
    reject, pValsAdj, alphacSidak, alphacBonf = multipletests(pValues, alpha=0.05, method='fdr_bh')

    # Final
    df = pd.DataFrame({'WPID': WPIDs,
                       'WPTitle': WPTitles,
                       'WPSize': WPsizes,
                       'TargetSize': TargetSizes,
                       'IntersectionSize': intersectionSizes,
                       'UniversSize': universSizes,
                       'pValue': pValues,
                       'pAdjusted': pValsAdj,
                       'Intersection': intersections
                       })

    # Write into a file
    dfSorted = df.sort_values(by=['pAdjusted'])
    dfSorted.to_csv(outputPath + '/Overlap_' + chemNames + '_withRDWP.csv', ';', index=False)

    print('\tOverlap analysis done!')
    # return df


def overlapAnalysis(chemTargetsDict, WPGeneRDDict, WPBackgroundGenes, WPDict, outputPath):
    """
    For each chemical given in input, calculate overlap with RD WP.

    :param dict chemTargetsDict: Dict composed of interaction genes list for each chemical
    :param dict WPGeneRDDict: Dictionary of Rare Diseases WP
    :param list WPBackgroundGenes: List of uniq genes found in Homo sapiens WP
    :param dict WPDict: Dict of titles for each RD WikiPathway
    :param str outputPath: Folder path to save the results
    """
    # For each chemical targets, calculate overlap with RD WP
    for chem in chemTargetsDict:
        overlap(targetGeneSet=set(chemTargetsDict[chem]),
                WPGenesDict=WPGeneRDDict,
                WPBackgroundGenesSet=set(WPBackgroundGenes),
                chemNames=chem,
                WPDict=WPDict,
                outputPath=outputPath)


def RWR(configPath, networksPath, outputPath, sifPathName, top):
    """
    Perform a Random Walk with Restart analysis on different multiplex and networks.
    You have to specify seeds and networks.

    :param str configPath: Configuration file name path
    :param str networksPath: Networks path name
    :param str outputPath: Output folder path name
    :param str sifPathName: Result file name path to write SIF result file
    :param int top: Number of results to report in SIF file
    """
    # Analysis
    multixrank_obj = multixrank.Multixrank(config=configPath, wdir=networksPath)
    ranking_df = multixrank_obj.random_walk_rank()
    multixrank_obj.write_ranking(ranking_df, path=outputPath)
    multixrank_obj.to_sif(ranking_df, path=sifPathName, top=top)
    pass


def DOMINO(genesFileName, networkFile, outputPath, featureName):
    """"""
    # Input file names
    data_dict = {
        'Network file name': os.path.basename(networkFile.name),
        'Active gene file name': os.path.basename(genesFileName)
    }
    # Input file contents
    files_dict = {
        'Network file contents': open(networkFile.name, 'rb'),
        'Active gene file contents': open(genesFileName, 'rb')
    }

    # Request and run DOMINO
    with alive_bar(title='Search active modules using DOMINO', theme='musical') as bar:
        response = requests.post(url='http://domino.cs.tau.ac.il/upload', data=data_dict, files=files_dict)
        bar()

        # Parse the result request
        response_dict = response.json()
        activeModules_list = response_dict['algOutput']['DefaultSet']['modules']

    if len(activeModules_list.keys()) > 0:
        # Write results into file
        resultOutput = outputPath + "/DOMINO_" + featureName + "_activeModules.txt"
        with open(resultOutput, 'w') as outputFileHandler:
            for module in activeModules_list:
                for gene in activeModules_list[module]:
                    line = gene + "\t" + module + "\n"
                    outputFileHandler.write(line)
        # Add chemMeSH into AM name
        activeModules_list = {f'AM_{activeModules_list}_' + featureName: v for activeModules_list, v in
                              activeModules_list.items()}
    else:
        print("No Active Modules detected")

    return activeModules_list


def DOMINOandOverlapAnalysis(featuresDict, networkFile, WPGeneRDDict, WPBackgroundGenes, WPDict, outputPath):
    """ """
    # Parameters
    resultsDict = {}
    # For each feature, search active modules using DOMINO
    for featureName in featuresDict:
        print(featureName + " analysis :")
        # Write genes list into result file
        resultFileName = outputPath + "/DOMINO_inputGeneList_" + featureName + ".txt"
        with open(resultFileName, 'w') as outputFileHandler:
            for gene in featuresDict[featureName]:
                outputFileHandler.write(gene)
                outputFileHandler.write('\n')
        # Run DOMINO
        resultsDict[featureName] = DOMINO(genesFileName=resultFileName,
                                          networkFile=networkFile,
                                          outputPath=outputPath,
                                          featureName=featureName)
        # Run Overlap
        overlapAnalysis(chemTargetsDict=resultsDict[featureName],
                        WPGeneRDDict=WPGeneRDDict,
                        WPBackgroundGenes=WPBackgroundGenes,
                        WPDict=WPDict,
                        outputPath=outputPath)
        print(featureName + " analysis done!\n")

# def DOMINO(genesFileName, networkFileName, outputPath, chemMeSH):
#     """
#
#     :param genesFileName:
#     :param networkFileName:
#     :return:
#     """
#     # Debug part
#     # genesFileName = 'TestDOMINO/OutputDOMINOResults_old/DOMINO_inputGeneList_D014801.txt'
#     # networkFileName = 'test/InputData/InputFile_PPI_2016.sif'
#     # outputPath=outputPath
#     # chemMeSH=chemMeSH
#     # # os.chdir('D:\\Morgane\\Work\\MMG\\05_EJP_RD\\WF_Environment\\EnvironmentProject\\test')
#     # os.chdir('/home/morgane/Documents/05_EJPR_RD/WF_Environment/EnvironmentProject')
#
#     # Input file names
#     data_dict = {
#         'Network file name': os.path.basename(networkFileName),
#         'Active gene file name': os.path.basename(genesFileName)
#     }
#     # Input file contents
#     files_dict = {
#         'Network file contents': open(networkFileName, 'rb'),
#         'Active gene file contents': open(genesFileName, 'rb')
#     }
#
#     # Request and run DOMINO
#     with alive_bar(title='Search active modules using DOMINO', theme='musical') as bar:
#         response = requests.post(url='http://domino.cs.tau.ac.il/upload', data=data_dict, files=files_dict)
#         bar()
#
#     # Parse the result request
#     response_dict = response.json()
#     activeModules_list = response_dict['algOutput']['DefaultSet']['modules']
#
#     if(len(activeModules_list.keys()) > 0):
#         # Write results into file
#         resultOutput = outputPath + "/DOMINO_" + chemMeSH + "_activeModules.txt"
#         with open(resultOutput, 'w') as outputFileHandler:
#             for module in activeModules_list:
#                 for gene in activeModules_list[module]:
#                     line = gene + "\t" + module + "\n"
#                     outputFileHandler.write(line)
#         # Add chemMeSH into AM name
#         activeModules_list = {f'AM_{activeModules_list}_' + chemMeSH: v for activeModules_list, v in
#         activeModules_list.items()}
#     else:
#         print("No Active Modules detected")
#
#     return activeModules_list

