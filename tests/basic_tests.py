#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Morgane T.

Tests script

This script tests some functions from different modules inside the project.
"""

# Libraries
import unittest
import os
import WP_functions as WP


class TestMethodsFromWPModule(unittest.TestCase):

    def test_readBackgroundsFile(self):
        # Parameters
        backgroundsDict_expected = {}
        backgroundsList_expected = []
        # Input
        backgroundsFile = 'test_WPFunctions/backgroundsFile.tsv'
        backgroundsDict_expectedFiles = ['test_WPFunctions/source1.gmt.expectedList.tsv',
                                         'test_WPFunctions/source2.gmt.expectedList.tsv',
                                         'test_WPFunctions/source3.gmt.expectedList.tsv',
                                         'test_WPFunctions/source4.gmt.expectedList.tsv']
        backgroundsList_expectedFile = 'test_WPFunctions/expectedBgList.tsv'
        # Read background expected files
        for file in backgroundsDict_expectedFiles:
            with open(file, 'r') as fileHandler:
                name = os.path.basename(file).split('.exp')[0]
                backgroundsDict_expected[name] = []
                for line in fileHandler:
                    backgroundsDict_expected[name].append(line.strip())
        # Read list of source expected
        with open(backgroundsList_expectedFile, 'r') as fileHandler:
            for line in fileHandler:
                linesList = line.strip().split('\t')
                backgroundsList_expected.append(linesList[1])
        # Run function
        with open(backgroundsFile, 'r') as bgFile:
            backgroundsDict, backgroundsList = WP.readBackgroundsFile(bgFile)
        # Compare
        self.assertEqual(backgroundsList, backgroundsList_expected)

    def test_readGMTFile(self):
        # Parameters
        GMTFile = 'test_WPFunctions/pathwaysOfInterest.gmt'
        WPDict_expected = {'WPID': 'pathways',
                           'WP4153': 'Degradation pathway of sphingolipids, including diseases',
                           'WP4156': 'Biosynthesis and regeneration of tetrahydrobiopterin and catabolism of phenylalanine',
                           'WP4157': 'GABA metabolism (aka GHB)',
                           'WP4220': 'Neurotransmitter disorders'}
        pathwaySizesDict = {}
        pathwaySizesDict_expected = {'WPID': 1, 'WP4153': 10, 'WP4156': 2, 'WP4157': 6, 'WP4220': 4}
        pathwayDict_expected = {'WP4220': ['MAOA', 'TH', 'DDC', 'DBH']}
        pathwaysOfInterestList_expected = ['WP4153', 'WP4156', 'WP4157', 'WP4220']
        # Run function
        with open(GMTFile, 'r') as GMTContent:
            genesDict, WPDict, pathwaysOfInterestList = WP.readGMTFile(GMTContent)
        # Calcul number of genes for each pathway
        for pathway in genesDict:
            pathwaySizesDict[pathway] = len(genesDict[pathway])
        # Compare
        self.assertEqual(WPDict, WPDict_expected)
        self.assertEqual(pathwaySizesDict, pathwaySizesDict_expected)
        self.assertEqual(genesDict['WP4220'], pathwayDict_expected['WP4220'])
        self.assertEqual(pathwaysOfInterestList, pathwaysOfInterestList_expected)

    def test_allGenesFromWP(self):
        # Parameters
        outputPath = 'test_WPFunctions/'
        backgroundGenesList_expectedFile = 'test_WPFunctions/bgGenesWP_2022_07_expected.csv'
        WPBackgroundGenesDict_expected = {'WikiPathway': []}
        # Read background genes file
        with open(backgroundGenesList_expectedFile, 'r') as backgroundGenesList_expected:
            for line in backgroundGenesList_expected:
                WPBackgroundGenesDict_expected['WikiPathway'].append(line.strip())
        # Run command
        WPBackgroundGenesDict = WP.allGenesFromWP(outputPath=outputPath)
        # Compare
        WPBackgroundGenesDict['WikiPathway'].sort()
        WPBackgroundGenesDict_expected['WikiPathway'].sort()
        self.assertEqual(len(WPBackgroundGenesDict['WikiPathway']), len(WPBackgroundGenesDict_expected['WikiPathway']))
        self.assertEqual(WPBackgroundGenesDict, WPBackgroundGenesDict_expected)

    def test_rareDiseasesWPrequest(self):
        # Parameters
        outputPath = 'test_WPFunctions/'
        pIfInt_GMT_File = 'test_WPFunctions/WP_RareDiseases_request_2022_07_29.gmt'
        # Expected results
        WPGeneRDDict_expected, WPDict_expected, pathwaysOfInterestList_expected = WP.readGMTFile(pIfInt_GMT_File)
        # Run command
        WPGeneRDDict, WPDict, pathwaysOfInterestList = WP.rareDiseasesWPrequest(outputPath=outputPath)
        # Compare
        self.assertEqual(pathwaysOfInterestList, pathwaysOfInterestList_expected)


if __name__ == '__main__':
    unittest.main()
