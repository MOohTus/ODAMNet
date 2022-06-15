#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Morgane T.

mainScript
"""
# Debug part
# import os, sys
# sys.path.append('/home/morgane/Documents/05_EJPR_RD/WF_Environment/EnvironmentProject/')

# Libraries
from argparse import ArgumentParser, SUPPRESS
from distutils import util
import CTD_functions as CTD
import WP_functions as WP
import methods_functions as methods
import os, sys

# Script version
VERSION = '1.0'


def overlap_analysis(argsDict):
    """
    Perform overlap analysis between genes targeted by chemicals and Rare Diseases pathways from WikiPathway

    :param argparse.ArgumentParser argsDict: List of arguments for overlap analysis
    """
    # Debug part
    # CTDFile = "test/InputData/CTDFile_byMeSH_inputFile.txt"
    # CTDFile = "test/InputData/CTDFile_byNames_inputFile.txt"
    # CTDFile = "/home/morgane/Documents/05_EJPR_RD/WF_Environment/EnvironmentProject/test/InputData/InputFile_CTD_sevMeSH.txt"
    # CTDFile = 'D:\\Morgane\\Work\\MMG\\05_EJP_RD\\WF_Environment\\EnvironmentProject\\test\\InputData\\InputFile_CTD_sevMeSH.txt'

    # Input parameters
    argsDict['outputPath'] = argsDict['outputPath'] + "/OutputOverlapResults/"
    outputPath = argsDict['outputPath']

    # Read CTD file and request CTD database
    chemNameList, chemTargetsDict = CTD.targetExtraction(argsDict=argsDict)

    # Search Rare Diseases pathways and extract all genes from WP
    WPGeneRDDict, WPDict = WP.rareDiseasesWPrequest(outputPath=outputPath)
    WPBackgroundGenes = WP.allGenesFromWP()

    # Overlap between our target list from CTD and WP of interest
    methods.overlapAnalysis(chemTargetsDict=chemTargetsDict,
                            WPGeneRDDict=WPGeneRDDict,
                            WPBackgroundGenes=WPBackgroundGenes,
                            WPDict=WPDict,
                            outputPath=outputPath)

    # Finish
    print('Overlap analysis finished')

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


def DOMINO_analysis(argsDict):
    """
    Perform DOMINO (active modules identification) analysis

    :param argparse.ArgumentParser argsDict: List of arguments for DOMINO analysis
    """
    # Debug part
    # argsDict = {}
    # argsDict['CTDFile'] = 'D:\\Morgane\\Work\\MMG\\05_EJP_RD\\WF_Environment\\EnvironmentProject\\test\\InputData\\InputFile_CTD_1MeSH.txt'
    # argsDict['directAssociations'] = True
    # argsDict['networkFileName'] = 'D:\\Morgane\\Work\\MMG\\05_EJP_RD\\WF_Environment\\EnvironmentProject\\test\\InputData\\InputFile_DOMINO_string.sif'
    # argsDict['outputPath'] = 'D:\\Morgane\\Work\\MMG\\05_EJP_RD\\WF_Environment\\EnvironmentProject\\test\\20220603_Analysis\\'
    # chemMeSH = 'D014801'
    # Debug part
    # argsDict = {}
    # argsDict['CTDFile'] = '/home/morgane/Documents/05_EJPR_RD/WF_Environment/EnvironmentProject/test/InputData/InputFile_CTD_vitaminAD.txt'
    # argsDict['directAssociations'] = True
    # argsDict['networkFileName'] = '/home/morgane/Documents/05_EJPR_RD/WF_Environment/EnvironmentProject/test/InputData/InputFile_PPI_2016.sif'
    # argsDict['outputPath'] = '/home/morgane/Documents/05_EJPR_RD/WF_Environment/EnvironmentProject/TestDOMINO/'
    # argsDict['nbPub'] = 2
    # chemMeSH = 'D014801'


    # Parameters
    argsDict['outputPath'] = argsDict['outputPath'] + "/OutputDOMINOResults/"
    networkName = argsDict['networkFileName']
    outputPath = argsDict['outputPath']
    resultsDict = {}

    # Read CTD file and request CTD database
    chemNameList, chemTargetsDict = CTD.targetExtraction(argsDict=argsDict)

    # Search Rare Diseases pathways and extract all genes from WP
    WPGeneRDDict, WPDict = WP.rareDiseasesWPrequest(outputPath=outputPath)
    WPBackgroundGenes = WP.allGenesFromWP()

    # DOMINO analysis for each environmental factor
    for chemMeSH in chemTargetsDict:
        print(chemMeSH + " analysis :")
        # Write genes list into result files
        resultFileName = outputPath + "/DOMINO_inputGeneList_" + chemMeSH + ".txt"
        with open(resultFileName, 'w') as outputFileHandler:
            for gene in chemTargetsDict[chemMeSH]:
                outputFileHandler.write(gene)
                outputFileHandler.write("\n")
        # Run DOMINO
        resultsDict[chemMeSH] = methods.DOMINO(genesFileName=resultFileName,
                                               networkFileName=networkName,
                                               outputPath=outputPath,
                                               chemMeSH=chemMeSH)
        # Run Overlap
        methods.overlapAnalysis(chemTargetsDict=resultsDict[chemMeSH],
                                WPGeneRDDict=WPGeneRDDict,
                                WPBackgroundGenes=WPBackgroundGenes,
                                WPDict=WPDict,
                                outputPath=outputPath)
        print(chemMeSH + " analysis done!\n")


def argumentParserFunction():
    """
    Argument parser function.

    :return:
        - **parser** (*argparse.ArgumentParser*) – List of arguments
    """
    parser = ArgumentParser(
        description='Perform overlap analyse between chemicals and rare diseases at different levels !')
    parser.add_argument('-v', '--version', action='version', version=VERSION)
    subparsers = parser.add_subparsers(title='Required mode', help='Choose which analysis you want to perform',
                                       metavar='overlap | RWR | DOMINO')

    # Overlap analysis
    parser_overlap = subparsers.add_parser('overlap',
                                           help='Overlap analysis between genes targeted by chemical and rare diseases pathways')
    parser_overlap_required = parser_overlap.add_argument_group('required arguments')
    # parser_overlap_optional = parser_overlap.add_argument_group('optional arguments')
    # Required
    parser_overlap_required.add_argument('-c', '--CTDFile', required=True,
                                         help='File path of the chemical name (or MeDH ID) list')
    parser_overlap_required.add_argument('--directAssociations', required=True, type=util.strtobool,
                                         help='Direct associations (only chem) or hierarchical associations (chem + all related chem) - False / True')
    # Optional
    parser_overlap.add_argument('-o', '--outputPath', default='OutputResults', help='Folder path for writing results')
    parser_overlap.add_argument('-r', '--nbPub', default=2, type=int,
                                help='Number of references needed to keep an interaction')
    # parser_overlap_optional.add_argument('-h', '--help', action = 'help', default = SUPPRESS, help = 'Show this help message and exit')
    parser_overlap.set_defaults(func=overlap_analysis)

    # RWR analysis
    parser_RWR = subparsers.add_parser('RWR', help='RWR analysis using chemical names as seeds')
    parser_RWR_required = parser_RWR.add_argument_group('required arguments')
    # parser_RWR_optional = parser_RWR.add_argument_group('optional arguments')
    # Required
    parser_RWR_required.add_argument('-c', '--CTDFile', required=True,
                                     help='File path of the chemical name (or MeDH ID) list')
    parser_RWR_required.add_argument('--directAssociations', required=True, type=util.strtobool,
                                     help='Direct associations (only chem) or hierarchical associations (chem + all related chem) - False / True')
    parser_RWR_required.add_argument('--configPath', required=True, help='Configuration for RWR file path')
    parser_RWR_required.add_argument('-n', '--networksPath', required=True, help='Networks folder path')
    # parser_RWR.add_argument('-o', '--outputPath', required=True, help='Output file name path')
    parser_RWR_required.add_argument('--sifPath', required=True, help='SIF file name path')
    # Optional
    parser_RWR.add_argument('-o', '--outputPath', default='OutputResults', help='Folder path for writing results')
    parser_RWR.add_argument('--top', type=int, default=3, help='Top number of results for SIF file')
    # parser_RWR_optional.add_argument('-h', '--help', action = 'help', default = SUPPRESS, help = 'Show this help message and exit')
    parser_RWR.set_defaults(func=RWR_analysis)

    # DOMINO analysis
    parser_DOMINO = subparsers.add_parser('DOMINO', help='DOMINO analysis using chemical target genes')
    parser_DOMINO_required = parser_DOMINO.add_argument_group('required arguments')
    # parser_DOMINO_optional = parser_DOMINO.add_argument_group('optional arguments')
    # Required
    parser_DOMINO_required.add_argument('-c', '--CTDFile', required=True,
                                        help='File path of the chemical name (or MeDH ID) list')
    parser_DOMINO_required.add_argument('--directAssociations', required=True, type=util.strtobool,
                                        help='Direct associations (only chem) or hierarchical associations (chem + all related chem) - False / True')
    parser_DOMINO_required.add_argument('-n', '--networkFileName', required=True, help='Network file name')
    # parser_DOMINO.add_argument('-g', '--genesFileName', required=True, help='Active gene set file name')
    # Optional
    parser_DOMINO.add_argument('-o', '--outputPath', default='OutputResults', help='Folder path for writing results')
    parser_DOMINO.add_argument('--nbPub', type=int, default=2, help='Number of references needed to keep an interaction')
    # parser_DOMINO_optional.add_argument('-h', '--help', action = 'help', default = SUPPRESS, help = 'Show this help message and exit')
    parser_DOMINO.set_defaults(func=DOMINO_analysis)

    return parser


# Main
if __name__ == "__main__":
    # Command-line interface
    parser = argumentParserFunction()
    args = parser.parse_args()
    argsDict = vars(args)
    if bool(argsDict):
        args.func(argsDict)
    else:
        parser.print_help(sys.stderr)
