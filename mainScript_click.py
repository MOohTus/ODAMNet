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


@main.command()
@click.option('-o', '--outputPath', 'outputPath', type=click.Path(), default='OutputResults')
def multiXrank(outputPath):
    """"""
    print("multiXrank analysis")


if __name__ == '__main__':
    main()




