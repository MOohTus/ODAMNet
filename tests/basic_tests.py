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
import EnvironmentProject.WP_functions as WP
import EnvironmentProject.CTD_functions as CTD
import EnvironmentProject.methods_functions as methods
from datetime import datetime


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
        pathOfInterestGenesDict_expected = {'pathwayIDs': ['HGNC'],
                                            'WP4153': ['GLB1', 'HEXA', 'ARSA', 'GLA', 'GM2A', 'HEXB', 'NEU1', 'NEU3', 'NEU2', 'NEU4'],
                                            'WP4156': ['PTS', 'GCH1'],
                                            'WP4157': ['DPEP1', 'ALDH5A1', 'ABAT', 'PON3', 'AKR7A2', 'ADHFE1'],
                                            'WP4220': ['MAOA', 'TH', 'DDC', 'DBH']}
        pathOfInterestNamesDict_expected = {'pathwayIDs': 'pathways',
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

    @unittest.skip('WP request to extract Rare Diseases pathways do not work anymore. 01/02/2023')
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

    # def test_debugDOMINOOutput(self):
    #     # Input
    #     networkFileName = '/home/morgane/Documents/05_EJPR_RD/WF_Environment/EnvironmentProject/examples/InputData/PPI_network_2016.sif'
    #     AMIFileName = '/home/morgane/Documents/05_EJPR_RD/WF_Environment/EnvironmentProject/examples/OutputResults_example1/OutputDOMINOResults/DOMINO_D014801_activeModules.txt'
    #     featureName = 'D014801'
    #     outputPath = '/home/morgane/Documents/05_EJPR_RD/WF_Environment/EnvironmentProject/examples/OutputResults_example1/OutputDOMINOResults/'
    #
    #     # DOMINOOutput(networkFileName, AMIFileName, featureName, outputPath)
    #
    #     # Parameters
    #     AM_dict = {}
    #     edges_df = pd.DataFrame(columns=['source', 'target', 'link', 'AMI_number'])
    #     AMNumbersList = []
    #     edgeNumberList = []
    #     nodeNumberList = []
    #     AMOverlapList = []
    #     overlapOutputLinesList = []
    #     AMIOutputLinesList = []
    #     AMPathwaysDict = {}
    #
    #     # Create network graph
    #     network_df = pd.read_csv(networkFileName, delimiter='\t')
    #     network_graph = nx.from_pandas_edgelist(network_df, 'node_1', 'node_2', 'link')
    #
    #     # Read Active Module composition
    #     with open(AMIFileName, 'r') as AMIFile:
    #         for line in AMIFile:
    #             line_list = line.strip().split('\t')
    #             AM = line_list[1]
    #             gene = line_list[0]
    #             if AM not in AM_dict:
    #                 AM_dict[AM] = [gene]
    #             else:
    #                 AM_dict[AM].append(gene)
    #
    #     # Extract active module networks
    #     for AMnb in AM_dict:
    #         if AMnb != 'ActiveModule':
    #             AMlist = AM_dict[AMnb]
    #             # Extract active module network
    #             network_subgraph = network_graph.subgraph(AMlist)
    #             subgraph_df = nx.to_pandas_edgelist(network_subgraph)
    #             subgraph_df['AMI_number'] = AMnb
    #             # Metrics about active modules
    #             AMNumbersList.append(AMnb)
    #             edgeNumberList.append(network_subgraph.number_of_edges())
    #             nodeNumberList.append(network_subgraph.number_of_nodes())
    #             # Add the subnetwork edges into a dataframe
    #             edges_df = pd.concat([edges_df, subgraph_df], ignore_index=True)
    #     metrics_df = pd.DataFrame({'AMINumber': AMNumbersList,
    #                                'EdgesNumber': edgeNumberList,
    #                                'NodesNumber': nodeNumberList})
    #
    #     # Parse overlap results
    #     overlapFilesList = fnmatch.filter(os.listdir(outputPath), 'Overlap_AM_*')
    #     for file in overlapFilesList:
    #         AMnb = file.split('_')[2]
    #         with open(outputPath + '/' + file, 'r') as overlapResults:
    #             overlapResults.readline()
    #             for line in overlapResults:
    #                 lineList = line.strip().split(';')
    #                 padj = lineList[8]
    #                 if float(padj) <= 0.05:
    #                     if AMnb not in AMOverlapList:
    #                         AMOverlapList.append(AMnb)
    #                     termID = lineList[0]
    #                     termTitle = lineList[1]
    #                     genesList = lineList[9].split(' ')
    #                     if termID in AMPathwaysDict:
    #                         if float(padj) < AMPathwaysDict[termID]:
    #                             AMPathwaysDict[termID] = float(padj)
    #                     else:
    #                         AMPathwaysDict[termID] = float(padj)
    #                     for gene in genesList:
    #                         overlapOutputLinesList.append([gene, AMnb, termID, termTitle, padj])
    #     AMPathwaysDict = dict(sorted(AMPathwaysDict.items(), key=lambda item: item[1]))
    #
    #     # Add overlap significant in activeModuleFile
    #     activeGenesDict = dict.fromkeys(list(AM_dict.keys()), 0)
    #     with open(AMIFileName, 'r') as AMIinputHandler:
    #         header = AMIinputHandler.readline().strip().split('\t')
    #         for line in AMIinputHandler:
    #             lineList = line.strip().split('\t')
    #             if lineList[2] == 'True':
    #                 activeGenesDict[lineList[1]] = activeGenesDict[lineList[1]] + 1
    #             if lineList[1] in AMOverlapList:
    #                 lineList.append('True')
    #             else:
    #                 lineList.append('False')
    #             AMIOutputLinesList.append(lineList)


class TestHeaderFiles(unittest.TestCase):

    def test_impactOfHeader(self):
        """test_impactOfHeader"""
        # With HEADER
        # Parameters
        CTDFileName_H = 'TestHeaderFiles/CTD_HEADER.tsv'
        pathOfInterestGMTFileName_H = 'TestHeaderFiles/WP_RareDiseases_HEADER.gmt'
        backgroundFileName_H = 'TestHeaderFiles/backgroundsFiles_H.tsv'
        outputPath = 'TestHeaderFiles/'
        analysisName = 'pathOfInterest_HEADER'
        # Function calling
        with open(CTDFileName_H, 'r') as CTDFile_HEADER:
            featuresDict = CTD.readCTDFile(CTDFile=CTDFile_HEADER, nbPub=2, outputPath=outputPath)
        with open(pathOfInterestGMTFileName_H, 'r') as pathOfInterestGMT_H:
            pathOfInterestGenesDict, pathOfInterestNamesDict, pathwaysOfInterestList = WP.readGMTFile(GMTFile=pathOfInterestGMT_H)
        with open(backgroundFileName_H, 'r') as backgroundFile_H:
            backgroundGenesDict, backgroundsList = WP.readBackgroundsFile(backgroundsFile=backgroundFile_H)
        pathwaysOfInterestList = list(zip(pathwaysOfInterestList, backgroundsList))
        methods.overlapAnalysis(targetGenesDict=featuresDict,
                                pathOfInterestGenesDict=pathOfInterestGenesDict,
                                pathOfInterestNamesDict=pathOfInterestNamesDict,
                                pathwaysOfInterestList=pathwaysOfInterestList,
                                backgroundGenesDict=backgroundGenesDict,
                                outputPath=outputPath,
                                analysisName=analysisName)

        # Without HEADER
        # Parameters
        pathOfInterestGMTFileName = 'TestHeaderFiles/WP_RareDiseases.gmt'
        backgroundFileName = 'TestHeaderFiles/backgroundsFiles.tsv'
        analysisName = 'pathOfInterest'
        # Function calling
        with open(CTDFileName_H, 'r') as CTDFile_HEADER:
            featuresDict = CTD.readCTDFile(CTDFile=CTDFile_HEADER, nbPub=2, outputPath=outputPath)
        with open(pathOfInterestGMTFileName, 'r') as pathOfInterestGMT:
            pathOfInterestGenesDict, pathOfInterestNamesDict, pathwaysOfInterestList = WP.readGMTFile(
                GMTFile=pathOfInterestGMT)
        with open(backgroundFileName, 'r') as backgroundFile:
            backgroundGenesDict, backgroundsList = WP.readBackgroundsFile(backgroundsFile=backgroundFile)
        pathwaysOfInterestList = list(zip(pathwaysOfInterestList, backgroundsList))
        methods.overlapAnalysis(targetGenesDict=featuresDict,
                                pathOfInterestGenesDict=pathOfInterestGenesDict,
                                pathOfInterestNamesDict=pathOfInterestNamesDict,
                                pathwaysOfInterestList=pathwaysOfInterestList,
                                backgroundGenesDict=backgroundGenesDict,
                                outputPath=outputPath,
                                analysisName=analysisName)

        # Comparison
        lines_H = []
        lines = []
        with open('TestHeaderFiles/Overlap_D014801_withpathOfInterest_HEADER.csv', 'r') as file_H:
            for line in file_H:
                lineList = line.strip().split(';')
                lineList.pop(2)
                lines_H.append(lineList)
        with open('TestHeaderFiles/Overlap_D014801_withpathOfInterest.csv', 'r') as file_H:
            for line in file_H:
                lineList = line.strip().split(';')
                lineList.pop(2)
                lines.append(lineList)
        self.assertEqual(lines_H, lines)


if __name__ == '__main__':
    unittest.main()
