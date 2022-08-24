#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Morgane T.

Main script
Using click for argument parsing
Analysis calling
"""

# Methods
import CTD_functions as CTD
import WP_functions as WP
import methods_functions as methods
# Libraries
from click_option_group import optgroup, RequiredMutuallyExclusiveOptionGroup
import click
import customClick as customClick
import os
from alive_progress import alive_bar
import shutil as shutil

# Script version
VERSION = '1.0'

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(context_settings=CONTEXT_SETTINGS, cls=customClick.NaturalOrderGroup)
@click.version_option(VERSION)
def main():
    """
    [OPTIONS] = overlap | domino | multixrank | networkCreation

    Analyse the link between environmental factors and rare disease pathways.
    Select the approach you want to perform :

    overlap | domino | multixrank

    If you need to create a network with the pathways of interest, select : networkCreation
    """
    pass


@main.command(short_help='Perform overlap analysis', context_settings=CONTEXT_SETTINGS)
@optgroup.group('Input data sources', cls=RequiredMutuallyExclusiveOptionGroup, help='Choice the input data source')
@optgroup.option('-f', '--factorList', 'factorListFile', type=click.File(), help='Factors list data file name')
@optgroup.option('-c', '--CTD_file', 'CTD_file', type=click.File(), help='CTD request result file name')
@optgroup.option('-g', '--geneList', 'geneListFile', type=click.File(), help='Genes list data file name')
@click.option('--directAssociation', 'directAssociation', default=True, type=bool, show_default=True,
              help='True: Only chem targets \\ False:Chem + descendants targets')
@click.option('--nbPub', 'nbPub', default=2, type=int, show_default=True,
              help='Number of references needed at least to keep an interaction')
@click.option('--GMT', 'pathOfInterestGMT', type=click.File(), cls=customClick.RequiredIf, required_if='backgroundFile',
              help='Pathways of interest in GMT like format. ')
@click.option('--backgroundFile', 'backgroundFile', type=click.File(), cls=customClick.RequiredIf, required_if='pathOfInterestGMT',
              help='Background genes file name. ')
@click.option('-o', '--outputPath', 'outputPath', type=click.Path(), default='OutputResults', show_default=True,
              help='Output folder name')
def overlap(factorListFile, CTD_file, geneListFile, directAssociation, nbPub, pathOfInterestGMT, backgroundFile, outputPath):
    """Perform overlap analysis between genes targeted by chemicals and Rare Diseases pathways from WikiPathway"""

    # Parameters
    outputPath = os.path.join(outputPath, 'OutputOverlapResults')
    featuresDict = {}
    pathwaysOfInterestList = []

    # Check if outputPath exist and create it if it does not exist
    if not os.path.exists(outputPath):
        os.makedirs(outputPath, exist_ok=True)

    # Extract genes from background and pathways of interest
    if pathOfInterestGMT:
        # Files reading
        pathOfInterestGenesDict, pathOfInterestNamesDict, pathwaysOfInterestList = WP.readGMTFile(GMTFile=pathOfInterestGMT)
        backgroundGenesDict, backgroundsList = WP.readBackgroundsFile(backgroundsFile=backgroundFile)
        pathwaysOfInterestList = list(zip(pathwaysOfInterestList, backgroundsList))
        analysisName = 'pathOfInterest'
    else:
        # Request WP
        with alive_bar(title='Request WikiPathways', theme='musical') as bar:
            pathOfInterestGenesDict, pathOfInterestNamesDict, pathwayOfInterestList = WP.rareDiseasesWPrequest(outputPath=outputPath)
            backgroundGenesDict = WP.allHumanGenesFromWP(outputPath=outputPath)
            for pathway in pathwayOfInterestList:
                pathwaysOfInterestList.append([pathway, list(backgroundGenesDict.keys())[0]])
            analysisName = 'RDWP'
            bar()

    if factorListFile:
        # Analysis from factor list
        featuresDict = CTD.targetGenesExtraction(chemicalsFile=factorListFile, directAssociations=directAssociation,
                                                 outputPath=outputPath, nbPub=nbPub)
    if geneListFile:
        # Analysis from gene list
        featuresDict['genesList'] = CTD.readFeaturesFile(featuresFile=geneListFile)
    if CTD_file:
        # Analysis from CTD file
        featuresDict = CTD.readCTDFile(CTDFile=CTD_file, nbPub=nbPub, outputPath=outputPath)

    # Overlap between our features list and pathways of interest
    methods.overlapAnalysis(targetGenesDict=featuresDict,
                            pathOfInterestGenesDict=pathOfInterestGenesDict,
                            pathOfInterestNamesDict=pathOfInterestNamesDict,
                            pathwaysOfInterestList=pathwaysOfInterestList,
                            backgroundGenesDict=backgroundGenesDict,
                            outputPath=outputPath,
                            analysisName=analysisName)
    print('Overlap analysis finished')


@main.command(short_help='Active Module Identification analysis', context_settings=CONTEXT_SETTINGS)
@optgroup.group('Input data sources', cls=RequiredMutuallyExclusiveOptionGroup, help='Choice the input data source')
@optgroup.option('-f', '--factorList', 'factorListFile', type=click.File(), help='Factors list data file name')
@optgroup.option('-c', '--CTD_file', 'CTD_file', type=click.File(), help='CTD request result file name')
@optgroup.option('-g', '--geneList', 'geneListFile', type=click.File(), help='Genes list data file name')
@click.option('--directAssociation', 'directAssociation', default=True, type=bool, show_default=True,
              help='True: Only chem targets \\ False:Chem + descendants targets')
@click.option('--nbPub', 'nbPub', default=2, type=int, show_default=True,
              help='Number of references needed at least to keep an interaction')
@click.option('-n', '--networkFile', 'networkFileName', type=str, metavar='FILENAME', required=True, help='Network file name')
@click.option('--netUUID', 'networkUUID', type=str, help='NDEx network ID')
@click.option('--GMT', 'pathOfInterestGMT', type=click.File(), cls=customClick.RequiredIf, required_if='backgroundFile',
              help='Pathways of interest in GMT like format.')
@click.option('--backgroundFile', 'backgroundFile', type=click.File(), cls=customClick.RequiredIf, required_if='pathOfInterestGMT',
              help='Background genes file name. ')
@click.option('-o', '--outputPath', 'outputPath', type=click.Path(), default='OutputResults', show_default=True,
              help='Output folder name')
def DOMINO(factorListFile, CTD_file, geneListFile, networkFileName, networkUUID, directAssociation, nbPub, pathOfInterestGMT, backgroundFile,
           outputPath):
    """DOMINO defines the target genes as active genes and search active modules through a given network."""
    # Parameters
    outputPath = os.path.join(outputPath, 'OutputDOMINOResults')
    featuresDict = {}
    pathwaysOfInterestList = []

    # Check if outputPath exist and create it if it does not exist
    if not os.path.exists(outputPath):
        os.makedirs(outputPath, exist_ok=True)

    # Extract network from NDEx website
    if os.path.exists(networkFileName):
        if networkUUID:
            print('Network File already exists. Give only file name (without network UUID) or rename/remove file.')
            exit()
    else:
        if networkUUID:
            methods.downloadNDExNetwork(networkUUID=networkUUID, outputFileName=networkFileName)
        else:
            print('Network file doesn\'t exist. Add the network UUID to request NEDx or give another network file.')
            exit()

    # Extract genes from background and pathways of interest
    if pathOfInterestGMT:
        # Files reading
        pathOfInterestGenesDict, pathOfInterestNamesDict, pathwaysOfInterestList = WP.readGMTFile(GMTFile=pathOfInterestGMT)
        backgroundGenesDict, backgroundsList = WP.readBackgroundsFile(backgroundsFile=backgroundFile)
        pathwaysOfInterestList = list(zip(pathwaysOfInterestList, backgroundsList))
        analysisName = 'pathOfInterest'
    else:
        # Request WP
        with alive_bar(title='Request WikiPathways', theme='musical') as bar:
            pathOfInterestGenesDict, pathOfInterestNamesDict, pathwayOfInterestList = WP.rareDiseasesWPrequest(outputPath=outputPath)
            backgroundGenesDict = WP.allHumanGenesFromWP(outputPath=outputPath)
            for pathway in pathwayOfInterestList:
                pathwaysOfInterestList.append([pathway, list(backgroundGenesDict.keys())[0]])
            analysisName = 'RDWP'
            bar()

    if factorListFile:
        # Analysis from factor list
        featuresDict = CTD.targetGenesExtraction(chemicalsFile=factorListFile, directAssociations=directAssociation,
                                                 outputPath=outputPath, nbPub=nbPub)
    if geneListFile:
        # Analysis from gene list
        featuresDict['genesList'] = CTD.readFeaturesFile(featuresFile=geneListFile)
    if CTD_file:
        # Analysis from CTD file
        featuresDict = CTD.readCTDFile(CTDFile=CTD_file, nbPub=nbPub, outputPath=outputPath)

    # DOMINO analysis for each environmental factor
    methods.DOMINOandOverlapAnalysis(featuresDict=featuresDict,
                                     networkFileName=networkFileName,
                                     pathOfInterestGenesDict=pathOfInterestGenesDict,
                                     pathOfInterestNamesDict=pathOfInterestNamesDict,
                                     pathwaysOfInterestList=pathwaysOfInterestList,
                                     backgroundGenesDict=backgroundGenesDict,
                                     outputPath=outputPath,
                                     analysisName=analysisName)


@main.command('networkCreation', short_help='Create network and bipartite', context_settings=CONTEXT_SETTINGS)
@click.option('--networksPath', 'networksPath', type=click.Path(), required=True,
              help='Output path where save the network')
@click.option('--networksName', 'networksName', type=str, default='WP_RareDiseasesNetwork.sif', show_default=True,
              metavar='FILENAME', help='Network output name')
@click.option('--bipartitePath', 'bipartitePath', type=click.Path(), required=True,
              help='Output path where save the bipartite')
@click.option('--bipartiteName', 'bipartiteName', type=str, default='Bipartite_WP_RareDiseases_geneSymbols.tsv',
              show_default=True, metavar='FILENAME', help='Bipartite output name')
@click.option('--GMT', 'pathOfInterestGMT', type=click.File(),
              help='Pathways of interest in GMT like format (e.g. from WP request).')
@click.option('-o', '--outputPath', 'outputPath', type=click.Path(), default='OutputResults', show_default=True,
              help='Output path name (for complementary output files)')
def createNetworkFiles(pathOfInterestGMT, networksPath, networksName, bipartitePath, bipartiteName, outputPath):
    """Create network SIF file from WP request or pathways of interest GMT file"""
    # Parameters
    outputPath = os.path.join(outputPath, 'OutputCreateNetwork')
    networkFileName = networksPath + '/' + networksName
    bipartiteFileName = bipartitePath + '/' + bipartiteName

    # Check if outputPath exist and create it if it does not exist
    if not os.path.exists(outputPath):
        os.makedirs(outputPath, exist_ok=True)
    # Check if networksPath exist and create it if it does not exist
    if not os.path.exists(networksPath):
        os.makedirs(networksPath, exist_ok=True)
    # Check if bipartitePath exist and create it if it does not exist
    if not os.path.exists(bipartitePath):
        os.makedirs(bipartitePath, exist_ok=True)

    # Extract pathways of interest
    if pathOfInterestGMT:
        # From file
        pathOfInterestGenesDict, pathOfInterestNamesDict, pathwaysOfInterestList = WP.readGMTFile(GMTFile=pathOfInterestGMT)
    else:
        # From request
        pathOfInterestGenesDict, pathOfInterestNamesDict, pathwayOfInterestList = WP.rareDiseasesWPrequest(outputPath=outputPath)

    # Create network and bipartite
    methods.createNetworkandBipartiteFiles(bipartiteName=bipartiteFileName,
                                           networkName=networkFileName,
                                           pathOfInterestGenesDict=pathOfInterestGenesDict)


@main.command(short_help='Random Walk with Restart Analysis', context_settings=CONTEXT_SETTINGS)
@optgroup.group('Input data sources', cls=RequiredMutuallyExclusiveOptionGroup, help='Choice the input data source')
@optgroup.option('-f', '--factorList', 'factorListFile', type=click.File(), help='Factors list data file name')
@optgroup.option('-c', '--CTD_file', 'CTD_file', type=click.File(), help='CTD request result file name')
@optgroup.option('-g', '--geneList', 'geneListFile', type=click.File(), help='Genes list data file name')
@click.option('--directAssociation', 'directAssociation', default=True, type=bool, show_default=True,
              help='True: Only chem targets \\ False:Chem + descendants targets')
@click.option('--nbPub', 'nbPub', default=2, type=int, show_default=True,
              help='Number of references needed at least to keep an interaction')
@click.option('--configPath', 'configPath', type=click.Path(), required=True, help='Configurations path name')
@click.option('--networksPath', 'networksPath', type=click.Path(), required=True, help='Network directory path')
@click.option('--seedsFile', 'seedsFileName', type=str, required=True, help='Seeds file path name', metavar='FILENAME')
@click.option('--sifFileName', 'sifFileName', type=str, required=True, help='Name of the output file network SIF',
              metavar='FILENAME')
@click.option('--top', 'top', type=int, default=10, show_default=True,
              help='Top number of results to write into output file')
@click.option('-o', '--outputPath', 'outputPath', type=click.Path(), default='OutputResults', show_default=True,
              help='Output folder name')
def multiXrank(factorListFile, CTD_file, geneListFile, directAssociation, nbPub, configPath,
               networksPath, seedsFileName, outputPath, sifFileName, top):
    """Performs a Random Walk with Restart through heterogeneous multilayer using the target genes as seeds"""
    # Parameters
    outputPath = os.path.join(outputPath, 'OutputMultiXRankResults')
    featuresDict = {}
    nodesList = []

    # Check if outputPath exist and create it if it does not exist
    if not os.path.exists(outputPath):
        os.makedirs(outputPath, exist_ok=True)

    # Seeds initiation
    if factorListFile:
        # Analysis from factor list
        featuresDict = CTD.targetGenesExtraction(chemicalsFile=factorListFile, directAssociations=directAssociation,
                                                 outputPath=outputPath, nbPub=nbPub)
    if geneListFile:
        # Analysis from gene list
        featuresDict['genesList'] = CTD.readFeaturesFile(featuresFile=geneListFile)
    if CTD_file:
        # Analysis from CTD file
        featuresDict = CTD.readCTDFile(CTDFile=CTD_file, nbPub=nbPub, outputPath=outputPath)

    # Extract nodes from multilayer
    with alive_bar(title='Extract nodes from multilayer', theme='musical') as bar:
        for root, dirs, files in os.walk(networksPath + '/multiplex'):
            for filename in files:
                with open(root + '/' + filename, 'r') as networkFileHandler:
                    for line in networkFileHandler:
                        nodes = line.strip().split('\t')
                        for n in nodes:
                            if n not in nodesList:
                                nodesList.append(n)
        bar()

    # Remove seed that are missing in network
    # Run RWR
    for factor in featuresDict:
        print('\tRandom walk analysis for : ' + factor)
        # Create output folder
        analysisOutputPath = outputPath + '/RWR_' + factor
        # If folder exist, change the name of it to not erase it
        n = 1
        while os.path.exists(analysisOutputPath):
            analysisOutputPath = outputPath + '/RWR_' + factor + '_' + str(n)
            n = n + 1
        # Check if outputPath exist and create it if it does not exist
        if not os.path.exists(analysisOutputPath):
            os.makedirs(analysisOutputPath, exist_ok=True)
        # Output names creation
        sifPathName = os.path.join(analysisOutputPath, sifFileName)

        # Write gene list into seed file
        seedList = []
        for gene in featuresDict[factor]:
            if gene in nodesList:
                seedList.append(gene)
        with open(seedsFileName, 'w') as seedFileHandler:
            seedFileHandler.write('\n'.join(seedList))
            seedFileHandler.write('\n')
        print('Number of seeds : ' + str(len(seedList)))
        # Run multiXrank
        shutil.copyfile(seedsFileName, analysisOutputPath + '/' + os.path.basename(seedsFileName))
        shutil.copyfile(configPath, analysisOutputPath + '/' + os.path.basename(configPath))
        methods.RWR(configPath=configPath, networksPath=networksPath, outputPath=analysisOutputPath,
                    sifPathName=sifPathName, top=top)


if __name__ == '__main__':
    main()
