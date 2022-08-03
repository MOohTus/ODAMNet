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
import networkx as nx
from scipy.stats import hypergeom
from statsmodels.stats.multitest import multipletests
from alive_progress import alive_bar


# Functions
def overlap(targetGeneSet, WPGenesDict, backgroundGenesDict, pathwaysOfInterestList, chemNames, WPDict, outputPath):
    """
    Calculate overlap.rst between target genes and Rase Diseases WP

    Metrics :
        - M is the population size (Nb of genes inside WikiPathway for Homo sapiens pathways)
        - n is the number of successes in the population (Nb of genes inside the selected RD WP)
        - N is the sample size (Nb of genes shared between target list (from chemical) and background genes from WP)
        - x is the number of drawn “successes” (Nb of genes shared between target list and RD WP)

    :param set targetGeneSet: Set of HGNC targets
    :param dict WPGenesDict: Dictionary of Rare Diseases WP
    :param set backgroundGenesDict:
    :param set pathwaysOfInterestList:
    :param str chemNames: MeSH ID of chemical of interest
    :param dict WPDict: Dictionary of WP composed of title of them
    :param str outputPath: Folder path to save the results

    :return:
        - **df** (*pd.DataFrame*) – Data frame of overlap.rst metrics for each rare diseases WP
    """
    # Parameters
    WPIDs = []
    WPTitles = []
    WPsizes = []
    sourcesList = []
    TargetSizes = []
    intersectionSizes = []
    universSizes = []
    pValues = []
    intersections = []

    # Calculate pvalue overlap.rst for each RD WP found
    for pathway in pathwaysOfInterestList:
        pathwayName = pathway[0]
        source = pathway[1]

        genesSet = set(WPGenesDict[pathwayName])
        backgroundGenesSet = set(backgroundGenesDict[source])

        # Metrics calculation
        M = len(backgroundGenesSet)
        n = len(genesSet)
        N = len(targetGeneSet.intersection(backgroundGenesSet))  # Taking only genes that are also in background
        intersection = list(genesSet.intersection(targetGeneSet))
        x = len(intersection)
        # print(pathwayName, M, n, N, x)

        # Hyper geometric test
        pval = hypergeom.sf(x - 1, M, n, N)

        # Fill variable to store information and metrics
        WPIDs.append(pathwayName)
        WPTitles.append(WPDict[pathwayName])
        WPsizes.append(n)
        sourcesList.append(source)
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
                       'Source': sourcesList,
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


def overlapAnalysis(chemTargetsDict, WPGeneRDDict, backgroundGenesDict, pathwaysOfInterestList, WPDict, outputPath):
    """
    For each chemical given in input, calculate overlap.rst with RD WP.

    :param dict chemTargetsDict: Dict composed of interaction genes list for each chemical
    :param dict WPGeneRDDict: Dictionary of Rare Diseases WP
    :param list backgroundGenesDict:
    :param list pathwaysOfInterestList:
    :param dict WPDict: Dict of titles for each RD WikiPathway
    :param str outputPath: Folder path to save the results
    """
    # For each chemical targets, calculate overlap.rst with RD WP
    for chem in chemTargetsDict:
        overlap(targetGeneSet=set(chemTargetsDict[chem]),
                WPGenesDict=WPGeneRDDict,
                backgroundGenesDict=backgroundGenesDict,
                pathwaysOfInterestList=pathwaysOfInterestList,
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
    with alive_bar(title='Random walks through the networks', theme='musical') as bar:
        multixrank_obj = multixrank.Multixrank(config=configPath, wdir=networksPath)
        ranking_df = multixrank_obj.random_walk_rank()
        multixrank_obj.write_ranking(ranking_df, path=outputPath)
        multixrank_obj.to_sif(ranking_df, path=sifPathName, top=top)
        bar()


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


def DOMINOandOverlapAnalysis(featuresDict, networkFile, WPGeneRDDict, backgroundGenesDict, pathwaysOfInterestList,
                             WPDict, outputPath):
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
                        backgroundGenesDict=backgroundGenesDict,
                        pathwaysOfInterestList=pathwaysOfInterestList,
                        WPDict=WPDict,
                        outputPath=outputPath)
        print(featureName + " analysis done!\n")



def DOMINOOutput(networkFileName, AMIFileName, outputPath):
    # Input parameters
    # outputPath = '/home/morgane/Documents/05_EJPR_RD/WF_Environment/EnvironmentProject/examples/OutputResults_example3/OutputDOMINOResults/'
    # AMIFileName = '/home/morgane/Documents/05_EJPR_RD/WF_Environment/EnvironmentProject/examples/OutputResults_example3/OutputDOMINOResults/DOMINO_genesList_activeModules.txt'
    # networkFileName= '/home/morgane/Documents/05_EJPR_RD/WF_Environment/EnvironmentProject/examples/InputData/PPI_network_2016.sif'
    edges_df = pd.DataFrame(columns=['source', 'target', 'link', 'AMI_number'])
    nList = []
    edgeNumberList = []
    nodeNumberList = []
    # Create network graph
    network_df = pd.read_csv(networkFileName, delimiter="\t")
    df = pd.DataFrame({'node_1': network_df['node_1'],
                       'node_2': network_df['node_2'],
                       'link': network_df['link']})
    network_graph = nx.from_pandas_edgelist(network_df, 'node_1', 'node_2', 'link')
    # network_graph.number_of_edges()
    # network_graph.number_of_nodes()
    # Read AMI results
    AMI_dict = {}
    with open(AMIFileName, 'r') as AMIFile:
        for line in AMIFile:
            line_list = line.strip().split('\t')
            AMI = line_list[1]
            gene = line_list[0]
            if AMI not in AMI_dict:
                AMI_dict[AMI] = [gene]
            else:
                AMI_dict[AMI].append(gene)
    # Extract subgraph
    for n in AMI_dict:
        AMIlist = AMI_dict[n]
        # Extract active module network
        network_subgraph = network_graph.subgraph(AMIlist)
        subgraph_df = nx.to_pandas_edgelist(network_subgraph)
        subgraph_df['AMI_number'] = n
        # Metrics about active modules
        nList.append(n)
        edgeNumberList.append(network_subgraph.number_of_edges())
        nodeNumberList.append(network_subgraph.number_of_nodes())
        # Add the subnetwork edges into a dataframe
        edges_df = pd.concat([edges_df, subgraph_df], ignore_index=True)
    # Display metrics
    metrics_df = pd.DataFrame({'AMINumber': nList,
                               'EdgesNumber': edgeNumberList,
                               'NodesNUmber': nodeNumberList})
    print(metrics_df)
    # Write results into files
    metrics_df.to_csv(outputPath + 'metrics.csv', index=False, sep='\t')
    edges_df.to_csv(outputPath + 'edges.csv', index=False, sep='\t')

    # number = '1'
    # AMIlist = AMI_dict[number]
    # network_subgraph = network_graph.subgraph(AMIlist)
    # nx.set_node_attributes(network_subgraph, 1, name='AMI_number')
    # network_subgraph.number_of_edges()
    # network_subgraph.number_of_nodes()
    # list(network_subgraph.nodes().data())
    # nx.write_edgelist(network_subgraph, outputPath + 'AMI_1.gr', delimiter='\t')

    # subgraph_df = nx.to_pandas_edgelist(network_subgraph)
    # subgraph_df['AMI_number'] = number

    # pd.DataFrame.from_dict(dict(network_subgraph.nodes(data=True)), orient='index')
    # pd.DataFrame.from_dict(network_subgraph.nodes, orient='index')

    # edges_df = pd.DataFrame(columns=['source', 'target', 'link', 'AMI_number'])
    # edges_df = edges_df.append(subgraph_df, ignore_index=True)
    #
    # edges_df = pd.concat([edges_df, subgraph_df])


