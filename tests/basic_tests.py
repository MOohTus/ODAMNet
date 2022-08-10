#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Morgane T.

Tests script

This script tests some functions from different modules inside the project.
"""

# Libraries
import unittest
import requests
import os
import filecmp
import WP_functions as WP
import CTD_functions as CTD
from datetime import datetime
import methods_functions as methods


class TestReadingFileFunction(unittest.TestCase):
    """
    Test reading file functions from CTD_functions and WP_functions
    """

    def test_readFeaturesFile(self):
        # Parameters
        featuresFileName = 'TestReadingFileFunction/featureNames.csv'
        featureNamesList_expected = ['feature1', 'feature2', 'feature3', 'feature4;feature1']
        # Function calling
        with open(featuresFileName, 'r') as featuresFile:
            featureNamesList = CTD.readFeaturesFile(featuresFile=featuresFile)
        # Comparison
        self.assertEqual(featureNamesList, featureNamesList_expected)

    def test_readCTDFile(self):
        # Parameters
        CTDFileName = 'TestReadingFileFunction/CTDFile.tsv'
        outputPath = 'TestReadingFileFunction/'
        targetGenesDict_expected = {'FEATURE1_FEATURE2': ['Gene1', 'Gene2', 'Gene3', 'Gene5']}
        # Function calling
        with open(CTDFileName, 'r') as CTDFile:
            targetGenesDict = CTD.readCTDFile(CTDFile=CTDFile, nbPub=2, outputPath=outputPath)
        # Comparison
        self.assertEqual(targetGenesDict, targetGenesDict_expected)
        self.assertTrue(filecmp.cmp(f1='TestReadingFileFunction/CTD_requestFiltered_FEATURE1_FEATURE2.tsv',
                                    f2='TestReadingFileFunction/CTDFile_expected.tsv', shallow=False))

    def test_readGMTFile(self):
        # Parameters
        GMTFileName = 'TestReadingFileFunction/pathwaysOfIntesrest.gmt'
        pathOfInterestGenesDict_expected = {'WPID': ['HGNC'],
                                            'WP4153': ['GLB1', 'HEXA', 'ARSA', 'GLA', 'GM2A', 'HEXB', 'NEU1', 'NEU3', 'NEU2', 'NEU4'],
                                            'WP4156': ['PTS', 'GCH1'],
                                            'WP4157': ['DPEP1', 'ALDH5A1', 'ABAT', 'PON3', 'AKR7A2', 'ADHFE1'],
                                            'WP4220': ['MAOA', 'TH', 'DDC', 'DBH']}
        pathOfInterestNamesDict_expected = {'WPID': 'pathways',
                                            'WP4153': 'Degradation pathway of sphingolipids, including diseases',
                                            'WP4156': 'Biosynthesis and regeneration of tetrahydrobiopterin and catabolism of phenylalanine',
                                            'WP4157': 'GABA metabolism (aka GHB)',
                                            'WP4220': 'Neurotransmitter disorders'}
        pathwaysOfInterestList_expected = ['WP4153', 'WP4156', 'WP4157', 'WP4220']
        # Function calling
        with open(GMTFileName, 'r') as GMTFile:
            pathOfInterestGenesDict, pathOfInterestNamesDict, pathwaysOfInterestList = WP.readGMTFile(GMTFile=GMTFile)
        # Comparison
        self.assertEqual(pathOfInterestGenesDict, pathOfInterestGenesDict_expected)
        self.assertEqual(pathOfInterestNamesDict, pathOfInterestNamesDict_expected)
        self.assertEqual(pathwaysOfInterestList, pathwaysOfInterestList_expected)


        pass

    def test_readBackgroundFile(self):
        pass
        # Parameters
        bgFileName = 'TestReadingFileFunction/backgroundsFile.txt'
        bgList_expected = ['source1.gmt', 'source2.gmt', 'source3.gmt', 'source3.gmt', 'source4.gmt',
                           'source1.gmt', 'source1.gmt', 'source4.gmt', 'source3.gmt', 'source3.gmt', 'source3.gmt']
        bg_expected = ['TestReadingFileFunction/source1.gmt.expected',
                       'TestReadingFileFunction/source2.gmt.expected',
                       'TestReadingFileFunction/source3.gmt.expected',
                       'TestReadingFileFunction/source4.gmt.expected']
        bgDict_expected = {}
        # Function calling
        with open(bgFileName, 'r') as bgFile:
            bgDict, bgList = WP.readBackgroundsFile(backgroundsFile=bgFile)
        # Expected results
        for file in bg_expected:
            bgName = os.path.basename(file).split('.exp')[0]
            bgDict_expected[bgName] = []
            with open(file, 'r') as bgFileHandler:
                for line in bgFileHandler:
                    gene = line.strip()
                    if gene not in bgDict_expected[bgName]:
                        bgDict_expected[bgName].append(gene)
        # Comparison
        self.assertEqual(bgDict, bgDict_expected)
        self.assertEqual(bgList, bgList_expected)


class TestRequestFunctions(unittest.TestCase):

    def test1_targetGenesExtraction_1Chem(self):
        """
        test1 : one chemical or two in the same line - Complete test
        """
        # Parameters
        files2Test = ['TestRequestFunctions/chemical_test1.csv', 'TestRequestFunctions/chemical_test2.csv']
        outputPath = 'TestRequestFunctions/'
        date = datetime.today().strftime('%Y_%m_%d')
        # Function calling
        for nbPub in range(5):
            for directAssociations in [True, False]:
                for chemicalsFileName in files2Test:
                    print('\n{0} :  - directAssociations : {1} - nbPub : {2}'.format(chemicalsFileName,
                                                                                     str(directAssociations),
                                                                                     str(nbPub)))
                    with open(chemicalsFileName, 'r') as chemicalsFile:
                        chemList = CTD.readFeaturesFile(featuresFile=chemicalsFile)
                    with open(chemicalsFileName, 'r') as chemicalsFile:
                        chemTargetsDict = CTD.targetGenesExtraction(chemicalsFile=chemicalsFile,
                                                                    directAssociations=directAssociations,
                                                                    outputPath=outputPath, nbPub=nbPub)
                    # Expected results
                    for n in chemList:
                        name = '_'.join(n.split(';'))
                        resultsFileName = 'TestRequestFunctions/CTD_requestFiltered_' + name + '_' + date + '.tsv'
                        with open(resultsFileName, 'r') as resultsFile:
                            chemTargetsDict_expected = CTD.readCTDFile(CTDFile=resultsFile, nbPub=nbPub, outputPath=outputPath)
                    # Comparison
                    self.assertEqual(chemTargetsDict, chemTargetsDict_expected)

    def test1_targetGenesExtraction_1Chem(self):
        """
        test1 : one chemical or two in the same line - Short version
        """
        # Parameters
        files2Test = ['TestRequestFunctions/chemical_test1.csv', 'TestRequestFunctions/chemical_test2.csv']
        outputPath = 'TestRequestFunctions/'
        date = datetime.today().strftime('%Y_%m_%d')
        nbPub = 2
        directAssociations = False
        # Function calling
        for chemicalsFileName in files2Test:
            with open(chemicalsFileName, 'r') as chemicalsFile:
                chemList = CTD.readFeaturesFile(featuresFile=chemicalsFile)
            with open(chemicalsFileName, 'r') as chemicalsFile:
                chemTargetsDict = CTD.targetGenesExtraction(chemicalsFile=chemicalsFile,
                                                            directAssociations=directAssociations,
                                                            outputPath=outputPath, nbPub=nbPub)
            # Expected results
            for n in chemList:
                name = '_'.join(n.split(';'))
                resultsFileName = 'TestRequestFunctions/CTD_requestFiltered_' + name + '_' + date + '.tsv'
                with open(resultsFileName, 'r') as resultsFile:
                    chemTargetsDict_expected = CTD.readCTDFile(CTDFile=resultsFile, nbPub=nbPub, outputPath=outputPath)
            # Comparison
            self.assertEqual(chemTargetsDict, chemTargetsDict_expected)

    def test2_targetGenesExtraction_severalChem(self):
        """
        test2 : two lines of uniq chemical
        """
        # Parameters
        chemicalsFileName = 'TestRequestFunctions/chemical_test3.csv'
        outputPath = 'TestRequestFunctions/'
        date = datetime.today().strftime('%Y_%m_%d')
        chemList_expected = ['D001205', 'D014807']
        chemTargetsDict_expected = {}
        nbPub = 2
        directAssociations = False
        # Function calling
        with open(chemicalsFileName, 'r') as chemicalsFile:
            chemList = CTD.readFeaturesFile(featuresFile=chemicalsFile)
        with open(chemicalsFileName, 'r') as chemicalsFile:
            chemTargetsDict = CTD.targetGenesExtraction(chemicalsFile=chemicalsFile,
                                                        directAssociations=directAssociations,
                                                        outputPath=outputPath, nbPub=2)
        # Expected results
        for chem in chemList_expected:
            resultsFileName = 'TestRequestFunctions/CTD_requestFiltered_' + chem + '_' + date + '.tsv'
            with open(resultsFileName, 'r') as resultsFile:
                chemTargetsDict_expected.update(CTD.readCTDFile(CTDFile=resultsFile, nbPub=nbPub,
                                                                outputPath=outputPath))
        # Comparison
        self.assertEqual(chemList, chemList_expected)
        self.assertEqual(chemTargetsDict, chemTargetsDict_expected)

    def test3_targetGenesExtraction_mix(self):
        """
        test3 : one two chemical line and one uniq chemical
        """
        # Parameters
        chemicalsFileName = 'TestRequestFunctions/chemical_test4.csv'
        outputPath = 'TestRequestFunctions/'
        date = datetime.today().strftime('%Y_%m_%d')
        chemList_expected = ['D014801;D001205', 'D014810']
        chemTargetsDict_expected = {}
        nbPub = 2
        directAssociations = False
        # Function calling
        with open(chemicalsFileName, 'r') as chemicalsFile:
            chemList = CTD.readFeaturesFile(featuresFile=chemicalsFile)
        with open(chemicalsFileName, 'r') as chemicalsFile:
            chemTargetsDict = CTD.targetGenesExtraction(chemicalsFile=chemicalsFile,
                                                        directAssociations=directAssociations,
                                                        outputPath=outputPath, nbPub=2)
        # Expected results
        for line in chemList_expected:
            chem = line.replace(';', '_')
            resultsFileName = 'TestRequestFunctions/CTD_requestFiltered_' + chem + '_' + date + '.tsv'
            with open(resultsFileName, 'r') as resultsFile:
                chemTargetsDict_expected.update(CTD.readCTDFile(CTDFile=resultsFile, nbPub=nbPub,
                                                                outputPath=outputPath))
        # Comparison
        self.assertEqual(chemList, chemList_expected)
        self.assertEqual(chemTargetsDict, chemTargetsDict_expected)

    def test_rareDiseasesWPrequest(self):
        pass

    def test_allHumanGenesFromWP(self):
        pass









# class TestMethodsFromWPModule(unittest.TestCase):
#
#     def test_allGenesFromWP(self):
#         # Parameters
#         outputPath = 'test_WPFunctions/'
#         backgroundGenesList_expectedFile = 'test_WPFunctions/bgGenesWP_2022_07_expected.csv'
#         date = datetime.today().strftime('%Y_%m_%d')
#         bgName = 'WikiPathway_' + date
#         WPBackgroundGenesDict_expected = {bgName: []}
#         # Read background genes file
#         with open(backgroundGenesList_expectedFile, 'r') as backgroundGenesList_expected:
#             for line in backgroundGenesList_expected:
#                 WPBackgroundGenesDict_expected[bgName].append(line.strip())
#         # Run command
#         WPBackgroundGenesDict = WP.allGenesFromWP(outputPath=outputPath)
#         # Compare
#         WPBackgroundGenesDict[bgName].sort()
#         WPBackgroundGenesDict_expected[bgName].sort()
#         self.assertEqual(len(WPBackgroundGenesDict[bgName]), len(WPBackgroundGenesDict_expected[bgName]))
#         self.assertEqual(WPBackgroundGenesDict, WPBackgroundGenesDict_expected)
#
#     def test_rareDiseasesWPrequest(self):
#         # Parameters
#         outputPath = 'test_WPFunctions/'
#         date = datetime.today().strftime('%Y_%m_%d')
#         pIfInt_GMT_File = 'test_WPFunctions/WP_RareDiseases_request_' + date + '.gmt'
#         # Run command
#         WPGeneRDDict, WPDict, pathwaysOfInterestList = WP.rareDiseasesWPrequest(outputPath=outputPath)
#         # Expected results
#         with open(pIfInt_GMT_File, 'r') as expectedGMTFile:
#             WPGeneRDDict_expected, WPDict_expected, pathwaysOfInterestList_expected = WP.readGMTFile(expectedGMTFile)
#         # Compare
#         self.assertEqual(pathwaysOfInterestList, pathwaysOfInterestList_expected)
#
#
# class TestOverlapAnalysis(unittest.TestCase):
#
#     def test_overlap_from1Source(self):
#         # Init
#         targetGeneSet = set(['gene1', 'gene2', 'gene3', 'gene4'])
#         WPGenesDict = {'Pathway1': ['gene1', 'gene2', 'gene4', 'gene6', 'gene8'],
#                        'Pathway2': ['gene1', 'gene3', 'gene5', 'gene7', 'gene9'],
#                        'Pathway3': ['gene1', 'gene10']}
#         backgroundGenesDict = {'Source1': ['gene1', 'gene2', 'gene3', 'gene4', 'gene5', 'gene6', 'gene7', 'gene8', 'gene9', 'gene10']}
#         pathwaysOfInterestList = [['Pathway1', 'Source1'], ['Pathway2', 'Source1'], ['Pathway3', 'Source1']]
#         chemNames = 'unittests_source1'
#         WPDict = {'Pathway1': 'Pathway1 from source 1',
#                   'Pathway2': 'Pathway2 from source 1',
#                   'Pathway3': 'Pathway3 from source 1'}
#         outputPath = '.'
#         # Run overlap analysis
#         methods.overlap(targetGeneSet, WPGenesDict, backgroundGenesDict, pathwaysOfInterestList, chemNames, WPDict, outputPath)
#         # Compare
#         self.assertTrue(filecmp.cmp(f1='Overlap_unittests_source1_withRDWP.csv',
#                                     f2='Overlap_unittests_source1_withRDWP_expected.csv',
#                                     shallow=False))
#
#     def test_overlap_fromDifferentSources(self):
#         # Init
#         targetGeneSet = set(['gene1', 'gene2', 'gene3', 'gene4'])
#         WPGenesDict = {'Pathway1': ['gene1', 'gene2', 'gene4', 'gene6', 'gene8'],
#                        'Pathway2': ['gene1', 'gene3', 'gene5', 'gene7', 'gene9'],
#                        'Pathway3': ['gene1', 'gene10'],
#                        'Pathway4': ['gene1', 'gene4', 'gene5', 'gene8', 'gene10']}
#         backgroundGenesDict = {
#             'Source1': ['gene1', 'gene2', 'gene3', 'gene4', 'gene5', 'gene6', 'gene7', 'gene8', 'gene9', 'gene10'],
#             'Source2': ['gene1', 'gene2', 'gene3', 'gene4', 'gene5', 'gene6', 'gene7', 'gene8', 'gene9'],
#             'Source3': ['gene1', 'gene20', 'gene3', 'gene4', 'gene50', 'gene6', 'gene10']}
#         pathwaysOfInterestList = [
#             ['Pathway1', 'Source1'], ['Pathway2', 'Source2'], ['Pathway3', 'Source3'], ['Pathway4', 'Source1']]
#         chemNames = 'unittests_manySources'
#         WPDict = {'Pathway1': 'Pathway1 from source 1',
#                   'Pathway2': 'Pathway2 from source 2',
#                   'Pathway3': 'Pathway3 from source 3',
#                   'Pathway4': 'Pathway4 from source 1'}
#         outputPath = '.'
#         # Run overlap analysis
#         methods.overlap(targetGeneSet, WPGenesDict, backgroundGenesDict, pathwaysOfInterestList, chemNames, WPDict,
#                         outputPath)
#         # Compare
#         self.assertTrue(filecmp.cmp(f1='Overlap_unittests_manySources_withRDWP.csv',
#                                     f2='Overlap_unittests_manySources_withRDWP_expected.csv',
#                                     shallow=False))
#
#
# class TestMethodFunctions(unittest.TestCase):
#
#     def test_intersectionFunction(self):
#         # GMT files
#         GMTFile = 'test_methodFunctions/PathwaysOfInterestBackground.txt'
#         with open(GMTFile, 'r') as GMTFileContent:
#             bgDict, bgList = WP.readBackgroundsFile(GMTFileContent)
#         for bg in bgDict:
#             print(bg, len(bgDict[bg]))
#             with open('test_methodFunctions/' + bg + '.list', 'w') as output:
#                 output.write("\n".join(bgDict[bg]))
#                 output.write("\n")
#         # Genes file
#         genesFile = 'test_methodFunctions/VitA-Balmer2002-Genes.txt'
#         with open(genesFile, 'r') as inputFileHandler:
#             geneList = CTD.readListFile(listFile=inputFileHandler)
#         with open('test_methodFunctions/genesList.list', 'w') as output:
#             output.write("\n".join(geneList))
#             output.write("\n")
#         # Comparison
#         genesSet = set(geneList)
#         for bg in bgDict:
#             bgSet = set(bgDict[bg])
#             intersectionSet = genesSet.intersection(bgSet)
#             with open('test_methodFunctions/' + bg + 'intersection.list', 'w') as output:
#                 output.write("\n".join(intersectionSet))
#                 output.write("\n")
#
#     def test_dominoRequest(self):
#         # Input names
#         genesFileName = '/home/morgane/Documents/05_EJPR_RD/WF_Environment/EnvironmentProject/examples/InputData/InputFromPaper/VitA-Balmer2002-Genes.txt'
#         networkFile = '/home/morgane/Documents/05_EJPR_RD/WF_Environment/EnvironmentProject/examples/InputData/PPI_network_2016.sif'
#         outputFileName = '/home/morgane/Documents/05_EJPR_RD/WF_Environment/EnvironmentProject/tests/DOMINO_outputTests.tsv'
#         genesList = []
#         # Request domino
#         data_dict = {
#             'Network file name': os.path.basename(networkFile),
#             'Active gene file name': os.path.basename(genesFileName)
#         }
#         # Input file contents
#         files_dict = {
#             'Network file contents': open(networkFile, 'rb'),
#             'Active gene file contents': open(genesFileName, 'rb')
#         }
#         response = requests.post(url='http://domino.cs.tau.ac.il/upload', data=data_dict, files=files_dict)
#         response_dict = response.json()
#         nodes = response_dict['algOutput']['DefaultSet']['nodes']
#         nodes.sort()
#         with open(genesFileName, 'r') as genesFile:
#             for line in genesFile:
#                 genesList.append(line.strip())
#         genesList.sort()
#         # Compare
#         nodesSet = set(nodes)
#         genesSet = set(genesList)
#         len(genesSet.intersection(nodesSet))
#         #
#         activeModules_dict = response_dict['algOutput']['DefaultSet']['modules']
#         with open(outputFileName, 'w') as outputFileHandler:
#             outputFileHandler.write('geneSymbol\tActiveModule\tactiveGene\n')
#             for module in activeModules_dict:
#                 for gene in activeModules_dict[module]:
#                     active = False
#                     if gene in genesList:
#                         active = True
#                     line = gene + '\t' + module + '\t' + str(active) + '\n'
#                     outputFileHandler.write(line)
#
#     def test_DOMINOOutputFunction(self):
#         # Parameters
#         networkFileName = '/home/morgane/Documents/05_EJPR_RD/WF_Environment/EnvironmentProject/examples/InputData/PPI_network_2016.sif'
#         AMIFileName = '/home/morgane/Documents/05_EJPR_RD/WF_Environment/EnvironmentProject/examples/OutputResults_example1/OutputDOMINOResults/DOMINO_D014801_activeModules.txt'
#         featureName = 'D014801'
#         outputPath = '/home/morgane/Documents/05_EJPR_RD/WF_Environment/EnvironmentProject/examples/OutputResults_example1/OutputDOMINOResults/'
#         # Create output from DOMINO results
#         methods.DOMINOOutput(networkFileName, AMIFileName, featureName, outputPath)


if __name__ == '__main__':
    unittest.main()
