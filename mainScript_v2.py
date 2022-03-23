#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Morgane T.

mainScript
"""

# Libraries
from argparse import ArgumentParser
from distutils import util
import CTD_functions as CTD
import WP_functions as WP
import methods_functions as methods
import os

# Script version
VERSION = '1.0'


def overlap_analysis(argsDict):
    """
    Perform overlap analysis between genes targeted by chemicals and Rare Diseases pathways from WikiPathway

    :param argparse.ArgumentParser argsDict: List of arguments for RWR analysis
    """
    # Input parameters
    # CTDFile = "test/InputData/CTDFile_byMeSH_inputFile.txt"
    # CTDFile = "test/InputData/CTDFile_byNames_inputFile.txt"
    # CTDFile = "/home/morgane/Documents/05_EJPR_RD/WF_Environment/EnvironmentProject/test/InputData/InputFile_CTD_sevMeSH.txt"
    CTDFile = argsDict['CTDFile']
    if argsDict['directAssociations']:
        association = 'directAssociations'
    else:
        association = 'hierarchicalAssociations'
    outputPath = argsDict['outputPath']

    # Check if outputPath exist and create it if does not
    if not os.path.exists(outputPath):
        os.mkdir(outputPath)

    # Read CTD file and request CTD database
    chemNameList = CTD.readCTDFile(CTDFile)
    chemTargetsDict = CTD.CTDrequestFromList(chemList=chemNameList, association=association, outputPath=outputPath)

    # Search Rare Diseases pathways and extract all genes from WP
    WPGeneRDDict, WPDict = WP.rareDiseasesWPrequest(outputPath=outputPath)
    WPBackgroundGenes = WP.allGenesFromWP()

    # Overlap between our target list from CTD and WP of interest
    methods.overlapAnalysis(chemTargetsDict=chemTargetsDict,
                            WPGeneRDDict=WPGeneRDDict,
                            WPBackgroundGenes=WPBackgroundGenes,
                            WPDict=WPDict,
                            outputPath=outputPath)


def RWR_analysis(argsDict):
    """
    Perform RWR analysis

    :param argparse.ArgumentParser argsDict: List of arguments for RWR analysis
    """
    # Parameters
    configPath = argsDict['configPath']
    networksPath = argsDict['networksPath']
    outputPath = argsDict['outputPath']
    sifPathName = argsDict['sifPath']
    top = argsDict['top']

    # RWR analysis
    methods.RWR(configPath=configPath, networksPath=networksPath, outputPath=outputPath, sifPathName=sifPathName, top=top)


def argumentParserFunction():
    """
    Argument parser function.

    :return:
        - **parser** (*argparse.ArgumentParser*) – List of arguments
    """
    parser = ArgumentParser(description='mainScript')
    parser.add_argument('-v', '--version', action='version', version=VERSION)
    subparsers = parser.add_subparsers(title='Required mode', help='Choose which analysis you want to perform', metavar='overlap | RWR')

    # Overlap analysis
    parser_overlap = subparsers.add_parser('overlap', help='Overlap analysis between genes targeted by chemical and rare diseases pathways')
    parser_overlap.add_argument('-c', '--CTDFile', required=True, help='File path of the chemical name (or MeDH ID) list')
    parser_overlap.add_argument('--directAssociations', required=True, type=util.strtobool,
                                help='Direct associations (only chem) or hierarchical associations (chem + all related chem) - False / True')
    parser_overlap.add_argument('-o', '--outputPath', default='OutputResults', help='Folder path for writing results')
    parser_overlap.set_defaults(func=overlap_analysis)

    # RWR analysis
    parser_RWR = subparsers.add_parser('RWR', help='RWR analysis using chemical names as seeds')
    parser_RWR.add_argument('-c', '--CTDFile', required=True, help='File path of the chemical name (or MeDH ID) list')
    # parser_RWR.add_argument('-s', '--seedPath', required=True, help='Seed file path')
    parser_RWR.add_argument('--configPath', required=True, help='Configuration for RWR file path')
    parser_RWR.add_argument('-n', '--networksPath', required=True, help='Networks folder path')
    parser_RWR.add_argument('-o', '--outputPath', required=True, help='Output file name path')
    parser_RWR.add_argument('--sifPath', required=True, help='SIF file name path')
    parser_RWR.add_argument('--top', default=3, help='Top number of results for SIF file')
    parser_RWR.set_defaults(func=RWR_analysis)

    return(parser)


# Main
if __name__ == "__main__":
    # Command-line interface
    parser = argumentParserFunction()
    args = parser.parse_args()
    argsDict = vars(args)
    args.func(argsDict)

