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
import filecmp
import WP_functions as WP
from datetime import datetime
import methods_functions as methods


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
        date = datetime.today().strftime('%Y_%m_%d')
        bgName = 'WikiPathway_' + date
        WPBackgroundGenesDict_expected = {bgName: []}
        # Read background genes file
        with open(backgroundGenesList_expectedFile, 'r') as backgroundGenesList_expected:
            for line in backgroundGenesList_expected:
                WPBackgroundGenesDict_expected[bgName].append(line.strip())
        # Run command
        WPBackgroundGenesDict = WP.allGenesFromWP(outputPath=outputPath)
        # Compare
        WPBackgroundGenesDict[bgName].sort()
        WPBackgroundGenesDict_expected[bgName].sort()
        self.assertEqual(len(WPBackgroundGenesDict[bgName]), len(WPBackgroundGenesDict_expected[bgName]))
        self.assertEqual(WPBackgroundGenesDict, WPBackgroundGenesDict_expected)

    def test_rareDiseasesWPrequest(self):
        # Parameters
        outputPath = 'test_WPFunctions/'
        date = datetime.today().strftime('%Y_%m_%d')
        pIfInt_GMT_File = 'test_WPFunctions/WP_RareDiseases_request_' + date + '.gmt'
        # Run command
        WPGeneRDDict, WPDict, pathwaysOfInterestList = WP.rareDiseasesWPrequest(outputPath=outputPath)
        # Expected results
        with open(pIfInt_GMT_File, 'r') as expectedGMTFile:
            WPGeneRDDict_expected, WPDict_expected, pathwaysOfInterestList_expected = WP.readGMTFile(expectedGMTFile)
        # Compare
        self.assertEqual(pathwaysOfInterestList, pathwaysOfInterestList_expected)


class TestOverlapAnalysis(unittest.TestCase):

    def test_overlap_from1Source(self):
        # Init
        targetGeneSet = set(['gene1', 'gene2', 'gene3', 'gene4'])
        WPGenesDict = {'Pathway1': ['gene1', 'gene2', 'gene4', 'gene6', 'gene8'],
                       'Pathway2': ['gene1', 'gene3', 'gene5', 'gene7', 'gene9'],
                       'Pathway3': ['gene1', 'gene10']}
        backgroundGenesDict = {'Source1': ['gene1', 'gene2', 'gene3', 'gene4', 'gene5', 'gene6', 'gene7', 'gene8', 'gene9', 'gene10']}
        pathwaysOfInterestList = [['Pathway1', 'Source1'], ['Pathway2', 'Source1'], ['Pathway3', 'Source1']]
        chemNames = 'unittests_source1'
        WPDict = {'Pathway1': 'Pathway1 from source 1',
                  'Pathway2': 'Pathway2 from source 1',
                  'Pathway3': 'Pathway3 from source 1'}
        outputPath = '.'
        # Run overlap analysis
        methods.overlap(targetGeneSet, WPGenesDict, backgroundGenesDict, pathwaysOfInterestList, chemNames, WPDict, outputPath)
        # Compare
        self.assertTrue(filecmp.cmp(f1='Overlap_unittests_source1_withRDWP.csv',
                                    f2='Overlap_unittests_source1_withRDWP_expected.csv',
                                    shallow=False))

    def test_overlap_fromDifferentSources(self):
        # Init
        targetGeneSet = set(['gene1', 'gene2', 'gene3', 'gene4'])
        WPGenesDict = {'Pathway1': ['gene1', 'gene2', 'gene4', 'gene6', 'gene8'],
                       'Pathway2': ['gene1', 'gene3', 'gene5', 'gene7', 'gene9'],
                       'Pathway3': ['gene1', 'gene10'],
                       'Pathway4': ['gene1', 'gene4', 'gene5', 'gene8', 'gene10']}
        backgroundGenesDict = {
            'Source1': ['gene1', 'gene2', 'gene3', 'gene4', 'gene5', 'gene6', 'gene7', 'gene8', 'gene9', 'gene10'],
            'Source2': ['gene1', 'gene2', 'gene3', 'gene4', 'gene5', 'gene6', 'gene7', 'gene8', 'gene9'],
            'Source3': ['gene1', 'gene20', 'gene3', 'gene4', 'gene50', 'gene6', 'gene10']}
        pathwaysOfInterestList = [
            ['Pathway1', 'Source1'], ['Pathway2', 'Source2'], ['Pathway3', 'Source3'], ['Pathway4', 'Source1']]
        chemNames = 'unittests_manySources'
        WPDict = {'Pathway1': 'Pathway1 from source 1',
                  'Pathway2': 'Pathway2 from source 2',
                  'Pathway3': 'Pathway3 from source 3',
                  'Pathway4': 'Pathway4 from source 1'}
        outputPath = '.'
        # Run overlap analysis
        methods.overlap(targetGeneSet, WPGenesDict, backgroundGenesDict, pathwaysOfInterestList, chemNames, WPDict,
                        outputPath)
        # Compare
        self.assertTrue(filecmp.cmp(f1='Overlap_unittests_manySources_withRDWP.csv',
                                    f2='Overlap_unittests_manySources_withRDWP_expected.csv',
                                    shallow=False))


if __name__ == '__main__':
    unittest.main()
