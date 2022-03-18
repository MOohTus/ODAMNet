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

# Script version
VERSION = '1.0'


# Functions
def argumentParserFunction():
    """
    Argument parser function.

    :return:
        - **parser** (*argparse.ArgumentParser*) – List of arguments
    """
    parser = ArgumentParser(description="mainScript")
    parser.add_argument('-v', '--version', action='version', version=VERSION)
    parser.add_argument('-c', '--CTDFile', required=True, help="File path of the chemical name (or MeDH ID) list")
    parser.add_argument('--directAssociations', required=True, type=util.strtobool,
                        help="Direct associations (only chem) or hierarchical associations (chem + all related chem) - False / True")
    return parser


# Main
if __name__ == "__main__":
    # Command-line interface
    parser = argumentParserFunction()
    args = parser.parse_args()
    argsDict = vars(args)

    # Input parameters
    # CTDFile = "test/InputData/CTDFile_byMeSH_inputFile.txt"
    # CTDFile = "test/InputData/CTDFile_byNames_inputFile.txt"
    # CTDFile = "/home/morgane/Documents/05_EJPR_RD/WF_Environment/EnvironmentProject/test/InputData/InputFile_CTD_sevMeSH.txt"
    CTDFile = argsDict['CTDFile']
    if argsDict['directAssociations']:
        association = 'directAssociations'
    else:
        association = 'hierarchicalAssociations'

    # Read CTD file and request CTD database
    chemNameList = CTD.readCTDFile(CTDFile)
    chemTargetsDict = CTD.CTDrequestFromList(chemList=chemNameList, association=association)

    # Search Rare Diseases pathways and extract all genes from WP
    WPGeneRDDict, WPDict = WP.rareDiseasesWPrequest()
    WPBackgroundGenes = WP.allGenesFromWP()

    # Overlap between our target list from CTD and WP of interest
    methods.overlapAnalysis(chemTargetsDict=chemTargetsDict,
                            WPGeneRDDict=WPGeneRDDict,
                            WPBackgroundGenes=WPBackgroundGenes,
                            WPDict=WPDict)
