#!/usr/bin/env python3
# -*- coding: utf-8 -*-*

# From Anthony Baptista script Diseases_similarity.py

# LIBRARIES
import os
import pandas as pd
import numpy as np
import obonet
import networkx as nx
import scipy as sp
import matplotlib.pyplot as plt
from collections import defaultdict
from alive_progress import alive_bar


# FUNCTIONS
# PHENOTYPES SIMILARITY
def sim_phenotypes(fi, fj, hpoNet, ICdict):
    # Extract descendant phenotypes
    ances_fi = nx.descendants(hpoNet, fi)
    ances_fi.add(fi)
    ances_fj = nx.descendants(hpoNet, fj)
    ances_fj.add(fj)
    # Intersection between two phenotypes
    inter = list(ances_fi.intersection(ances_fj))
    temp = list()
    for i in inter:
        if i in ICdict.keys():
            temp.append(ICdict[i])
        else:
            temp.append(0)
    if len(temp) != 0:
        sim_phen = max(temp)
    else:
        sim_phen = 0
    return sim_phen


# DISEASES SIMILARITY
def sim_diseases(Da, Db, diseasesNbPhenoDict, diseasesDict, hpoNet, ICdict):
    # Extract number of phenotypes
    DA = diseasesNbPhenoDict[Da]
    DB = diseasesNbPhenoDict[Db]
    # Extract list of phenotypes
    phenA = diseasesDict[Da]
    phenB = diseasesDict[Db]
    #
    valA = 0
    valB = 0
    # Calculate similarity between
    for pheni in phenA:
        temp = list()
        for phenj in phenB:
            temp.append(sim_phenotypes(pheni, phenj, hpoNet, ICdict))
        valA += max(temp)
    for pheni in phenB:
        temp = list()
        for phenj in phenA:
            temp.append(sim_phenotypes(pheni, phenj, hpoNet, ICdict))
        valB += max(temp)
    # Calculate similarity between Da and Db
    sim = (1/(2*DA))*valA + (1/(2*DB))*valB
    return sim


# DRAW NETWORK
def drawNetwork(graph, nodeLabelsDict, edgesList, weightName):
    # Positions for all nodes
    pos = nx.spring_layout(graph, seed=7)
    # nodes and nodes labels
    nx.draw_networkx_nodes(graph, pos, node_size=700)
    #nx.draw_networkx_labels(graph, pos, labels=nodeLabelsDict)
    nx.draw_networkx_labels(graph, pos)
    # edges and weight labels
    nx.draw_networkx_edges(graph, pos, edgelist=edgesList)
    edges_labelsDict = dict()
    edges_labelsDict = nx.get_edge_attributes(graph, weightName)
    for edge in edges_labelsDict:
        edges_labelsDict[edge] = float("{:.2f}".format(edges_labelsDict[edge]))
    nx.draw_networkx_edge_labels(graph, pos, edges_labelsDict)


# WORK ENVIRONMENT
workDirectory = '/home/morgane/Documents/05_EJPR_RD/WF_Environment/DiseasesNetworks/hpo_disease_net'
phenotypeFile = 'phenotype_2022_06.hpoa'
# phenotypeFile = 'test.hpoa'
similarityFileName = 'Similarity_matrix.tsv'
edgesListFileName = 'weightedEdgesList.tsv'
diseasesNetworkFileName = 'diseases_network.sif'

os.chdir(workDirectory)

# PHENOTYPE ANNOTATION LOADING
phenoAnnotationDF = pd.read_csv(phenotypeFile, sep='\t', dtype=object, comment='#')
phenoAnnotationDF = phenoAnnotationDF[['DatabaseID', 'HPO_ID']]

# EXTRACT ONLY OMIM TERM
phenoAnnotationDF = phenoAnnotationDF[phenoAnnotationDF['DatabaseID'].str.contains('OMIM')]
diseasesArray = np.unique(list(phenoAnnotationDF['DatabaseID']))
# len(diseasesArray)

# CALCULATE FREQ OF HPO IN THE DATABASE
phenoFrequencyDict = dict(phenoAnnotationDF['HPO_ID'].value_counts())
# CALCULATE NB OF PHENOTYPE ASSOCIATED FOR EACH DISEASE
diseasesNbPhenoDict = dict(phenoAnnotationDF['DatabaseID'].value_counts())
# CREATE DISEASE DICT WITH ASSOCIATED PHENOTYPES
diseasesDict = {}
with alive_bar(title='1. Create diseases dict', theme='musical') as bar:
    for d in diseasesArray:
        diseasesDict[d] = list(np.unique(np.array(list(phenoAnnotationDF[phenoAnnotationDF['DatabaseID'] == d]['HPO_ID']))))
    bar()

# HPO ONTOLOGY STRUCTURE LOADING
hpoNet = obonet.read_obo('hp.obo')
hpoIDsDict = {id_: data.get('name') for id_, data in hpoNet.nodes(data=True)}

# INFORMATION CONTENT CALCULATION
with alive_bar(title='2. Calculate IC', theme='musical') as bar:
    ICdict = dict((hpoID, 0) for hpoID in list(hpoNet.nodes()))
    N = len(phenoAnnotationDF['HPO_ID'])
    for hpoID in phenoAnnotationDF['HPO_ID']:
        if hpoID in hpoNet.nodes():
            temp = list(nx.descendants(hpoNet, hpoID))
            temp.append(hpoID)
            for i in temp:
                ICdict[i] += 1
    for hpoID in ICdict.keys():
        ICdict[hpoID] = -np.log(ICdict[hpoID]/N)
    bar()

# CALCULATE SIMILARITY MATRIX BETWEEN DISEASES
size = len(diseasesArray)
Similarity = sp.sparse.lil_matrix((size, size))
with alive_bar(title='3. Calculate similarity matrix', theme='musical') as bar:
    for k in range(size):
        for l in range(size):
            Similarity[k, l] = sim_diseases(diseasesArray[k], diseasesArray[l], diseasesNbPhenoDict, diseasesDict, hpoNet, ICdict)
    bar()

# SAVE SIMILARITY MATRIX
# Similarity.data
similarityArray = Similarity.toarray()
similarityDf = pd.DataFrame(similarityArray, columns=diseasesArray, index=diseasesArray)
similarityDf.to_csv(similarityFileName, index=True, sep='\t')

# CREATE NETWORK
graph = nx.from_scipy_sparse_matrix(Similarity, edge_attribute='weight')
# graph.nodes()
# nx.edges(graph)
# len(nx.edges(graph))
# nx.get_edge_attributes(graph, 'weight')

# SET ATTRIBUTES
diseasesDict = dict(enumerate(diseasesArray.flatten(), 0))
nx.set_node_attributes(graph, diseasesDict, 'nodeNames')

# REMOVE SELF LOOP
graph.remove_edges_from(nx.selfloop_edges(graph))
# nx.edges(graph)
# len(nx.edges(graph))
# nx.get_edge_attributes(graph, 'weight')

# SAVE EDGES LIST WITH WEIGHT INTO FILE
nx.write_weighted_edgelist(graph, edgesListFileName, delimiter='\t')

# SELECT TOP N EDGES FOR EACH DISEASE
topEdgesDict = defaultdict(list)
topEdgesList = list()
# SORT EDGES FOR EACH NODE
for u,v in sorted(graph.edges(), key=lambda x: graph.get_edge_data(x[0], x[1])['weight'], reverse=True):
    topEdgesDict[u].append((u, v))
    topEdgesDict[v].append((u, v))
# SELECT TOP N EDGES
for key in topEdgesDict:
    for edge in topEdgesDict[key][:3]:
        if edge not in topEdgesList:
            topEdgesList.append(edge)
# len(topEdgesList)

# EXTRACT SUBGRAPH
filteredGraph = nx.Graph(topEdgesList)
# SET ATTRIBUTES
nx.set_node_attributes(filteredGraph, diseasesDict, 'nodeNames')
# nx.set_edge_attributes(filteredGraph, nx.get_edge_attributes(graph, 'weight'), 'weight')
# METRICS
# nx.edges(filteredGraph)
# len(nx.edges(filteredGraph))

# DRAW NETWORK
# drawNetwork(graph, diseasesDict, list(nx.edges(graph)), 'weight')
# drawNetwork(graph, diseasesDict, topEdgesList, 'weight')
# drawNetwork(filteredGraph, diseasesDict, list(nx.edges(filteredGraph)), 'weight')

# SAVE FILTERED NETWORK
nx.relabel_nodes(filteredGraph, diseasesDict, copy=False)
nx.write_edgelist(filteredGraph, diseasesNetworkFileName, delimiter='\t', data=False)
