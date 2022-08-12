#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Morgane T.

Tests script

This script tests some functions from different modules inside the project.
"""

# Libraries
import unittest
import pandas as pd
import networkx as nx
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

    def test_readBackgroundFile(self):
        """
        test_readBackgroundFile
        """
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
    """
    Test request functions from CTD_functions and WP_functions
    """

    def test_targetGenesExtraction_1Chem(self):
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

    def test_targetGenesExtraction_1Chem(self):
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

    def test_targetGenesExtraction_severalChem(self):
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

    def test_targetGenesExtraction_mix(self):
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
        # Parameters
        outputPath = 'TestRequestFunctions/'
        date = datetime.today().strftime('%Y_%m_%d')
        GMTFileName = outputPath + '/WP_RareDiseases_request_' + date + '.gmt'
        # Function calling
        genesWPDict, namesWPDict, WPnamesList = WP.rareDiseasesWPrequest(outputPath=outputPath)
        # Expected results
        with open(GMTFileName, 'r') as GMTFile:
            genesWPDict_expected, namesWPDict_expected, WPnamesList_expected = WP.readGMTFile(GMTFile=GMTFile)
        # Comparison
        self.assertEqual(genesWPDict, genesWPDict_expected)
        self.assertEqual(namesWPDict, namesWPDict_expected)
        self.assertEqual(WPnamesList, WPnamesList_expected)

    def test_allHumanGenesFromWP(self):
        """
        test_allHumanGenesFromWP
        """
        # Parameters
        outputPath = 'TestRequestFunctions/'
        outputBgFileName = 'TestRequestFunctions/backgroundsFile.txt'
        date = datetime.today().strftime('%Y_%m_%d')
        bgName = 'WikiPathway_' + date
        with open(outputBgFileName, 'w') as output:
            bgFileName_expected = 'WP_allPathways_request_' + date + '.gmt'
            output.write(bgFileName_expected)
            output.write('\n')
        # Function calling
        bgDict = WP.allHumanGenesFromWP(outputPath=outputPath)
        # Expected results
        with open(outputBgFileName, 'r') as bgFile_expected:
            bgDict_expected, bgList_expected = WP.readBackgroundsFile(backgroundsFile=bgFile_expected)
        # Comparison
        bgDict[bgName].sort()
        bgDict_expected[bgFileName_expected].sort()
        self.assertEqual(len(bgDict[bgName]), len(bgDict_expected[bgFileName_expected]))
        self.assertEqual(bgDict[bgName], bgDict_expected[bgFileName_expected])


class TestNetworkCreationFunction(unittest.TestCase):

    def test_createNetworkandBipartiteFiles(self):
        # Parameters
        pathwaysOfInterestDict = {'P1': ['G1', 'G2', 'G3', 'G4'],
                                  'P2': ['G10'],
                                  'P3': ['G100', 'G200', 'G300', 'G400', 'G500'],
                                  'P4': ['G1000', 'G2000', 'G3000', 'G4000']}
        bipartiteName = 'TestCreateNetworkFunction/bipartite.sif'
        networkName = 'TestCreateNetworkFunction/network.sif'
        bipartiteName_expected = 'TestCreateNetworkFunction/bipartite_expected.sif'
        networkName_expected = 'TestCreateNetworkFunction/network_expected.sif'
        # Function calling
        methods.createNetworkandBipartiteFiles(bipartiteName=bipartiteName,
                                               networkName=networkName,
                                               pathOfInterestGenesDict=pathwaysOfInterestDict)
        # Comparison
        self.assertTrue(filecmp.cmp(f1=bipartiteName, f2=bipartiteName_expected, shallow=False))
        self.assertTrue(filecmp.cmp(f1=networkName, f2=networkName_expected, shallow=False))


class TestOverlapAnalysis(unittest.TestCase):

    def test_overlap_1Bg(self):
        # Parameters
        targetGeneSet = {'gene1', 'gene2', 'gene3', 'gene4', 'gene18'}
        pathOfInterestGenesDict = {'Pathway1': ['gene1', 'gene2', 'gene4', 'gene6', 'gene8'],
                                   'Pathway2': ['gene1', 'gene3', 'gene5', 'gene7', 'gene9'],
                                   'Pathway3': ['gene1', 'gene10']}
        pathOfInterestNamesDict = {'Pathway1': 'Pathway1 from source 1',
                                   'Pathway2': 'Pathway2 from source 1',
                                   'Pathway3': 'Pathway3 from source 1'}
        pathwaysOfInterestList = [['Pathway1', 'Source1'], ['Pathway2', 'Source1'], ['Pathway3', 'Source1']]
        backgroundGenesDict = {'Source1': ['gene1', 'gene2', 'gene3', 'gene4', 'gene5', 'gene6', 'gene7', 'gene8', 'gene9', 'gene10']}
        featureName = 'unittests_source1'
        outputPath = 'TestOverlapAnalysis/'
        analysisName = 'test'
        # Function calling
        methods.overlap(targetGeneSet=targetGeneSet,
                        pathOfInterestGenesDict=pathOfInterestGenesDict,
                        pathOfInterestNamesDict=pathOfInterestNamesDict,
                        pathwaysOfInterestList=pathwaysOfInterestList,
                        backgroundGenesDict=backgroundGenesDict,
                        featureName=featureName, outputPath=outputPath, analysisName=analysisName)
        # Comparison
        self.assertTrue(filecmp.cmp(f1='TestOverlapAnalysis/Overlap_unittests_source1_withtest.csv',
                                    f2='TestOverlapAnalysis/Overlap_unittests_source1_withtest_expected.csv',
                                    shallow=False))

    def test_overlap_severalBg(self):
        # Parameters
        targetGeneSet = {'gene1', 'gene2', 'gene3', 'gene4', 'gene10'}
        pathOfInterestGenesDict = {'Pathway1': ['gene1', 'gene2', 'gene4', 'gene6', 'gene8'],
                                   'Pathway2': ['gene1', 'gene3', 'gene5', 'gene7', 'gene9'],
                                   'Pathway3': ['gene1', 'gene10'],
                                   'Pathway4': ['gene1', 'gene3', 'gene4', 'gene8', 'gene10']}
        pathOfInterestNamesDict = {'Pathway1': 'Pathway1 from source 1',
                                   'Pathway2': 'Pathway2 from source 2',
                                   'Pathway3': 'Pathway3 from source 3',
                                   'Pathway4': 'Pathway4 from source 1'}
        pathwaysOfInterestList = [
            ['Pathway1', 'Source1'], ['Pathway2', 'Source2'], ['Pathway3', 'Source3'], ['Pathway4', 'Source1']]
        backgroundGenesDict = {
            'Source1': ['gene1', 'gene2', 'gene3', 'gene4', 'gene5', 'gene6', 'gene7', 'gene8', 'gene9', 'gene10'],
            'Source2': ['gene1', 'gene2', 'gene3', 'gene4', 'gene5', 'gene6', 'gene7', 'gene8', 'gene9'],
            'Source3': ['gene1', 'gene20', 'gene3', 'gene4', 'gene50', 'gene6', 'gene10']}
        featureName = 'unittests_multipleSources'
        outputPath = 'TestOverlapAnalysis/'
        analysisName = 'test'
        # Function calling
        methods.overlap(targetGeneSet=targetGeneSet,
                        pathOfInterestGenesDict=pathOfInterestGenesDict,
                        pathOfInterestNamesDict=pathOfInterestNamesDict,
                        pathwaysOfInterestList=pathwaysOfInterestList,
                        backgroundGenesDict=backgroundGenesDict,
                        featureName=featureName, outputPath=outputPath, analysisName=analysisName)
        # Comparison
        self.assertTrue(filecmp.cmp(f1='TestOverlapAnalysis/Overlap_unittests_multipleSources_withtest.csv',
                                    f2='TestOverlapAnalysis/Overlap_unittests_multipleSources_withtest_expected.csv',
                                    shallow=False))


class TestDOMINOAnalysis(unittest.TestCase):

    def test_DOMINOOutputFunction(self):
        # Parameters
        networkFileName = 'TestDOMINOmethods/network.sif'
        AMIFileName = 'TestDOMINOmethods/DOMINO_testDOMINOoutput_activeModules.txt'
        featureName = 'testDOMINOoutput'
        outputPath = 'TestDOMINOmethods/'
        AMIFileInit = ['geneSymbol\tActiveModule\tActiveGene\n',
                       'g1\t1\tFalse\n', 'g2\t1\tFalse\n', 'g5\t1\tFalse\n', 'g4\t1\tTrue\n', 'g20\t1\tFalse\n',
                       'g16\t3\tFalse\n', 'g7\t3\tFalse\n', 'g17\t3\tTrue\n', 'g6\t3\tTrue\n',
                       'g14\t2\tTrue\n', 'g18\t2\tFalse\n', 'g9\t2\tFalse\n', 'g13\t2\tFalse\n']
        # Function calling
        with open(AMIFileName, 'w') as outputHandler:
            for line in AMIFileInit:
                outputHandler.write(line)
        methods.DOMINOOutput(networkFileName=networkFileName, AMIFileName=AMIFileName,
                             featureName=featureName, outputPath=outputPath)
        # Comparison of AMI network
        network_df = pd.read_csv('TestDOMINOmethods/DOMINO_testDOMINOoutput_activeModulesNetwork.txt', delimiter='\t')
        network_graph = nx.from_pandas_edgelist(network_df, 'source', 'target', 'link')
        network_df_expected = pd.read_csv('TestDOMINOmethods/DOMINO_testDOMINOoutput_activeModulesNetwork.txt', delimiter='\t')
        network_graph_expected = nx.from_pandas_edgelist(network_df_expected, 'source', 'target', 'link')
        self.assertTrue(network_graph.nodes, network_graph_expected.nodes)
        self.assertTrue(network_graph.edges, network_graph_expected.edges)
        # Comparison of AM metadata
        AMI_metadataFileName = 'TestDOMINOmethods/DOMINO_testDOMINOoutput_activeModules.txt'
        AMI_metadataFileName_expected = 'TestDOMINOmethods/DOMINO_testDOMINOoutput_activeModules_expected.txt'
        AMI_df = pd.read_csv(AMI_metadataFileName, delimiter='\t')
        AMI_df = AMI_df.sort_values(by='geneSymbol')
        AMI_df_expected = pd.read_csv(AMI_metadataFileName_expected, delimiter='\t')
        AMI_df_expected = AMI_df_expected.sort_values(by='geneSymbol')
        pd.testing.assert_frame_equal(AMI_df, AMI_df_expected)
        # Comparison of metrics
        metricsFileName = 'TestDOMINOmethods/DOMINO_testDOMINOoutput_activeModulesNetworkMetrics.txt'
        metricsFileName_expected = 'TestDOMINOmethods/DOMINO_testDOMINOoutput_activeModulesNetworkMetrics_expected.txt'
        metrics_df = pd.read_csv(metricsFileName, delimiter='\t')
        metrics_df = metrics_df.sort_values(by='AMINumber')
        metrics_df_expected = pd.read_csv(metricsFileName_expected, delimiter='\t')
        metrics_df_expected = metrics_df_expected.sort_values(by='AMINumber')
        pd.testing.assert_frame_equal(metrics_df.reset_index(drop=True), metrics_df_expected.reset_index(drop=True))


if __name__ == '__main__':
    unittest.main()
