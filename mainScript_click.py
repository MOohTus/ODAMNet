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
import multixrank
from alive_progress import alive_bar


# Script version
VERSION = '1.0'


@click.group()
@click.version_option(VERSION)
def main():
    """Analyse the link between environmental factors and rare disease pathways.
    Select the approach you want to perform :

    overlap | domino | multiXrank
    """
    pass


@main.command()
@optgroup.group('Input data sources', cls=RequiredMutuallyExclusiveOptionGroup, help='Choice the input data source')
@optgroup.option('--factorList', 'factorListFile', type=click.File(), help='Factor list input data file')
@optgroup.option('--CTD_file', 'CTD_file', type=click.File(), help='CTD results request file')
@optgroup.option('--geneList', 'geneListFile', type=click.File(), help='Genes list input data file')
@click.option('--directAssociation', 'directAssociation', default=True, type=bool, show_default=True)
@click.option('--nbPub', 'nbPub', default=2, type=int, show_default=True)
@click.option('--WP_GMT', 'WP_GMT', type=click.File(), cls=customClick.RequiredIf, required_if='universFile')
@click.option('--universFile', 'universFile', type=click.File(), cls=customClick.RequiredIf, required_if='WP_GMT', help='Universe file name with gene names. ')
@click.option('-o', '--outputPath', 'outputPath', type=click.Path(), default='OutputResults')
def overlap(factorListFile, CTD_file, geneListFile, directAssociation, nbPub, WP_GMT, universFile, outputPath):
    """Perform overlap analysis between genes targeted by chemicals and Rare Diseases pathways from WikiPathway"""

    # Parameters
    outputPath = os.path.join(outputPath, 'OutputOverlapResults')
    featuresDict = {}

    # Check if outputPath exist and create it if does not
    if not os.path.exists(outputPath):
        os.makedirs(outputPath, exist_ok=True)

    # Rare Diseases pathways and extract all genes from WP
    if WP_GMT:
        # Files reading
        WPGeneRDDict, WPDict = WP.readGMTFile(GMTFile=WP_GMT)
        WPBackgroundGenes = WP.readUniversFile(UniversFile=universFile)
    else:
        # Request WP
        WPGeneRDDict, WPDict = WP.rareDiseasesWPrequest(outputPath=outputPath)
        WPBackgroundGenes = WP.allGenesFromWP(outputPath=outputPath)

    if factorListFile:
        # Analysis from factor list
        featuresDict = CTD.targetExtraction(CTDFile=factorListFile, directAssociations=directAssociation, outputPath=outputPath, nbPub=nbPub)
    if geneListFile:
        # Analysis from gene list
        featuresDict["genesList"] = CTD.readListFile(listFile=geneListFile)
    if CTD_file:
        # Analysis from CTD file
        featuresDict = CTD.readCTDFile(CTDFile=CTD_file, nbPub=nbPub, outputPath=outputPath)

    # Overlap between our features list and pathways of interest
    methods.overlapAnalysis(chemTargetsDict=featuresDict,
                            WPGeneRDDict=WPGeneRDDict,
                            WPBackgroundGenes=WPBackgroundGenes,
                            WPDict=WPDict,
                            outputPath=outputPath)

    print('Overlap analysis finished')


@main.command()
@optgroup.group('Input data sources', cls=RequiredMutuallyExclusiveOptionGroup, help='Choice the input data source')
@optgroup.option('--factorList', 'factorListFile', type=click.File(), help='Factor list input data file')
@optgroup.option('--CTD_file', 'CTD_file', type=click.File(), help='CTD results request file')
@optgroup.option('--geneList', 'geneListFile', type=click.File(), help='Genes list input data file')
@click.option('-n', '--networkFile', 'networkFile', type=click.File(mode='rb'), required=True)
@click.option('--directAssociation', 'directAssociation', default=True, type=bool, show_default=True)
@click.option('--nbPub', 'nbPub', default=2, type=int, show_default=True)
@click.option('--WP_GMT', 'WP_GMT', type=click.File(), cls=customClick.RequiredIf, required_if='universFile')
@click.option('--universFile', 'universFile', type=click.File(), cls=customClick.RequiredIf, required_if='WP_GMT', help='Universe file name with gene names. ')
@click.option('-o', '--outputPath', 'outputPath', type=click.Path(), default='OutputResults')
def DOMINO(factorListFile, CTD_file, geneListFile, networkFile, directAssociation, nbPub, WP_GMT, universFile, outputPath):
    """DOMINO analysis using chemical target genes"""

    # Parameters
    outputPath = os.path.join(outputPath, 'OutputDOMINOResults')
    featuresDict = {}

    # Check if outputPath exist and create it if does not
    if not os.path.exists(outputPath):
        os.makedirs(outputPath, exist_ok=True)

    # Rare Diseases pathways and extract all genes from WP
    if WP_GMT:
        # Files reading
        WPGeneRDDict, WPDict = WP.readGMTFile(GMTFile=WP_GMT)
        WPBackgroundGenes = WP.readUniversFile(UniversFile=universFile)
    else:
        # Request WP
        WPGeneRDDict, WPDict = WP.rareDiseasesWPrequest(outputPath=outputPath)
        WPBackgroundGenes = WP.allGenesFromWP(outputPath=outputPath)

    if factorListFile:
        # Analysis from factor list
        featuresDict = CTD.targetExtraction(CTDFile=factorListFile, directAssociations=directAssociation,
                                            outputPath=outputPath, nbPub=nbPub)
    if geneListFile:
        # Analysis from gene list
        featuresDict["genesList"] = CTD.readListFile(listFile=geneListFile)
    if CTD_file:
        # Analysis from CTD file
        featuresDict = CTD.readCTDFile(CTDFile=CTD_file, nbPub=nbPub, outputPath=outputPath)

    # DOMINO analysis for each environmental factor
    methods.DOMINOandOverlapAnalysis(featuresDict=featuresDict,
                                     networkFile=networkFile,
                                     WPGeneRDDict=WPGeneRDDict,
                                     WPBackgroundGenes=WPBackgroundGenes,
                                     WPDict=WPDict,
                                     outputPath=outputPath)


@main.command('networkCreation')
@click.option('--WP_GMT', 'WP_GMT', type=click.File(), help='GMT file name (e.g. from WP request)')
@click.option('--networksPath', 'networksPath', type=click.Path(), required=True, help='Network output path')
@click.option('--networksName', 'networksName', type=str, default='WP_RareDiseasesNetwork.gr', help='Network output name', show_default=True)
@click.option('--bipartitePath', 'bipartitePath', type=click.Path(), required=True, help='Bipartite output path')
@click.option('--bipartiteName', 'bipartiteName', type=str, default='Bipartite_WP_RareDiseases_geneSymbols.tsv', help='Bipartite output name', show_default=True)
@click.option('-o', '--outputPath', 'outputPath', type=click.Path(), default='OutputResults', help='Output path name (for WP request)', show_default=True)
def createNetworkFileFromWP(WP_GMT, networksPath, networksName, bipartitePath, bipartiteName, outputPath):
    """Create network SIF file from WP request or WP GMT file"""
    # Parameters
    outputPath = os.path.join(outputPath, 'OutputCreateNetworkFromWP')
    pathwayName = networksPath + "/" + networksName
    bipartiteName = bipartitePath + "/" + bipartiteName
    WPID = []
    bipartiteOutputLines = []

    # Check if outputPath exist and create it if does not
    if not os.path.exists(outputPath):
        os.makedirs(outputPath, exist_ok=True)
    # Check if networksPath exist and create it if does not
    if not os.path.exists(networksPath):
        os.makedirs(networksPath, exist_ok=True)
    # Check if bipartitePath exist and create it if does not
    if not os.path.exists(bipartitePath):
        os.makedirs(bipartitePath, exist_ok=True)

    # Extract all rare disease genes from WP
    if WP_GMT:
        # From file
        WPGeneRDDict, WPDict = WP.readGMTFile(GMTFile=WP_GMT)
    else:
        # From request
        WPGeneRDDict, WPDict = WP.rareDiseasesWPrequest(outputPath=outputPath)

    # Create gene symbols and diseases bipartite
    for id in WPGeneRDDict:
        if id != "WPID":
            if id not in WPID:
                WPID.append(id)
            for gene in WPGeneRDDict[id]:
                bipartiteOutputLines.append([id, gene])
    with open(bipartiteName, 'w') as bipartiteOutputFile:
        for line in bipartiteOutputLines:
            bipartiteOutputFile.write("\t".join(line))
            bipartiteOutputFile.write("\n")
    with open(pathwayName, 'w') as networkOutputFile:
        for id in WPID:
            networkOutputFile.write("\t".join([id, id]))
            networkOutputFile.write("\n")


@main.command()
@optgroup.group('Input data sources', cls=RequiredMutuallyExclusiveOptionGroup, help='Choice the input data source')
@optgroup.option('--factorList', 'factorListFile', type=click.File(), help='Factor list input data file')
@optgroup.option('--CTD_file', 'CTD_file', type=click.File(), help='CTD results request file')
@optgroup.option('--geneList', 'geneListFile', type=click.File(), help='Genes list input data file')
@click.option('--directAssociation', 'directAssociation', default=True, type=bool, show_default=True)
@click.option('--nbPub', 'nbPub', default=2, type=int, show_default=True)
@click.option('--configPath', 'configPath', type=click.Path(), required=True)
@click.option('--networksPath', 'networksPath', type=click.Path(), required=True)
@click.option('--seedsFile', 'seedsFile', type=click.File(mode='w'), required=True)
@click.option('-o', '--outputPath', 'outputPath', type=click.Path(), default='OutputResults')
@click.option('--sifFileName', 'sifFileName', type=str, required=True)
@click.option('--top', 'top', type=int, default=10)
def multiXrank(factorListFile, CTD_file, geneListFile, directAssociation, nbPub, configPath,
               networksPath, seedsFile, outputPath, sifFileName, top):
    """"""
    # Parameters
    outputPath = os.path.join(outputPath, 'OutputMultiXRankResults')
    sifPathName = os.path.join(outputPath, sifFileName)
    featuresDict = {}
    nodesList = []

    # Check if outputPath exist and create it if does not
    if not os.path.exists(outputPath):
        os.makedirs(outputPath, exist_ok=True)

    # Seeds initiation
    if factorListFile:
        # Analysis from factor list
        featuresDict = CTD.targetExtraction(CTDFile=factorListFile, directAssociations=directAssociation,
                                            outputPath=outputPath, nbPub=nbPub)
    if geneListFile:
        # Analysis from gene list
        featuresDict["genesList"] = CTD.readListFile(listFile=geneListFile)
    if CTD_file:
        # Analysis from CTD file
        featuresDict = CTD.readCTDFile(CTDFile=CTD_file, nbPub=nbPub, outputPath=outputPath)

    with alive_bar(title='Seed file creation', theme='musical') as bar:
        # Check if seed is in the multiplex, if doesn't remove it
        for root, dirs, files in os.walk(networksPath + "/multiplex"):
            for filename in files:
                with open(root + "/" + filename, "r") as networkFileHandler:
                    for line in networkFileHandler:
                        nodes = line.strip().split("\t")
                        for n in nodes:
                            if n not in nodesList:
                                nodesList.append(n)
        # Write gene list into seed file
        for factor in featuresDict:
            seedList = []
            for gene in featuresDict[factor]:
                if gene in nodesList:
                    seedList.append(gene)
            seedsFile.write("\n".join(seedList))
            seedsFile.write("\n")
        bar()

    # Run multiXrank
    methods.RWR(configPath=configPath, networksPath=networksPath, outputPath=outputPath, sifPathName=sifPathName, top=top)


if __name__ == '__main__':
    main()




