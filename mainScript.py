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
    CTDFile = "test/CTDFile_byMeSH_inputFile.txt"
    # CTDFile = argsDict['CTDFile']
    if argsDict['directAssociations']:
        association = 'directAssociations'
    else:
        association = 'hierarchicalAssociations'

    # Parameters
    chemNameList = []
    chemTargetsList = []
    WPGeneRDDict = {}
    WPBackgroundGenes = []

    # Read CTD file and request CTD database
    chemNameList = CTD.readCTDFile(CTDFile)
    chemName = "|".join(chemNameList)
    chemTargetsList = CTD.CTDrequest(chemName=chemName, association=association, resultFileName="test/CTD_request.tsv")

    # Search Rare Diseases pathways and extract all genes from WP
    WPGeneRDDict = WP.rareDiseasesWPrequest(resultFileName="test/WP_request.tsv")
    WPBackgroundGenes = WP.allGenesFromWP()

    # Overlap between our target list from CTD and WP of interest
