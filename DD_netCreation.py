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
import scipy.sparse
import time
import multiprocessing
import itertools
from collections import defaultdict


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
    # get the start time
    st = time.process_time()
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
    # get the end time
    et = time.process_time()
    # get execution time
    res = et - st
    return sim, res


# WORKER - PERFORM SIMILARITY BETWEEN TWO DISEASES - PARALLEL
def worker(pair, diseasesArray, diseasesNbPhenoDict, diseasesDict, hpoNet, ICdict):
    # CALULATE SCORE FOR PAIR OF DISEASE
    k, l = pair
    # print('Comparison diseases ', k, ' - ', l)
    score, res = sim_diseases(diseasesArray[k], diseasesArray[l], diseasesNbPhenoDict, diseasesDict, hpoNet, ICdict)
    return (k, l, score, res)


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
# phenotypeFile = 'phenotype_2022_06.hpoa'
# phenotypeFile = 'test.hpoa'
phenotypeFile = 'test_v1.hpoa'
similarityFileName = 'Similarity_matrix.tsv'
edgesListFileName = 'weightedEdgesList.tsv'
allEdgesListFileName = 'allWeightedEdgesList.tsv'
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
for d in diseasesArray:
    diseasesDict[d] = list(np.unique(np.array(list(phenoAnnotationDF[phenoAnnotationDF['DatabaseID'] == d]['HPO_ID']))))

# HPO ONTOLOGY STRUCTURE LOADING
hpoNet = obonet.read_obo('hp.obo')
hpoIDsDict = {id_: data.get('name') for id_, data in hpoNet.nodes(data=True)}

# INFORMATION CONTENT CALCULATION
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

# CALCULATE SIMILARITY MATRIX BETWEEN DISEASES
st = time.time()
size = len(diseasesArray)
Similarity = sp.sparse.lil_matrix((size, size))
processTime = 0
for k in range(size):
    for l in range(k, size):
        score, res = sim_diseases(diseasesArray[k], diseasesArray[l], diseasesNbPhenoDict, diseasesDict, hpoNet, ICdict)
        Similarity[k, l] = score
        Similarity[l, k] = score
        processTime += res
print(processTime)
et = time.time()
print(et - st)

# CALCULATE SIMILARITY MATRIX BETWEEN DISEASES // PARALLEL
st = time.time()
size = len(diseasesArray)
SimilarityPar = sp.sparse.lil_matrix((size, size))
processTimePar = 0
combination = itertools.combinations_with_replacement(range(0,size), 2)
p = multiprocessing.Pool(processes=8)
for k, l, score, res in p.starmap_async(worker, [(pair, diseasesArray, diseasesNbPhenoDict, diseasesDict, hpoNet, ICdict) for pair in combination]).get():
    SimilarityPar[k, l] = score
    SimilarityPar[l, k] = score
    processTimePar += res
p.close()
print(processTimePar)
et = time.time()
print(et - st)



# SAVE SIMILARITY MATRIX
# Similarity.data
similarityArray = Similarity.toarray()
similarityDf = pd.DataFrame(similarityArray, columns=diseasesArray, index=diseasesArray)
# similarityDf.to_csv(similarityFileName, index=True, sep='\t')

# CREATE NETWORK
graph = nx.from_scipy_sparse_matrix(Similarity, edge_attribute='weight')
graph.nodes()
nx.edges(graph)
len(nx.edges(graph))
nx.get_edge_attributes(graph, 'weight')

# SET ATTRIBUTES
diseasesDict = dict(enumerate(diseasesArray.flatten(), 0))
nx.set_node_attributes(graph, diseasesDict, 'nodeNames')

# REMOVE SELF LOOP
graph.remove_edges_from(nx.selfloop_edges(graph))
nx.edges(graph)
len(nx.edges(graph))
nx.get_edge_attributes(graph, 'weight')

# SAVE EDGES LIST WITH WEIGHT INTO FILE
renamedGraph = nx.relabel_nodes(graph, diseasesDict, copy=True)
nx.write_weighted_edgelist(renamedGraph, allEdgesListFileName, delimiter='\t')

# SELECT TOP N EDGES FOR EACH DISEASE
topEdgesDict = defaultdict(list)
topEdgesList = list()
# SORT EDGES FOR EACH NODE
for u, v in sorted(graph.edges(), key=lambda x: graph.get_edge_data(x[0], x[1])['weight'], reverse=True):
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
nx.set_edge_attributes(filteredGraph, nx.get_edge_attributes(graph, 'weight'), 'weight')
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
nx.write_weighted_edgelist(filteredGraph, edgesListFileName, delimiter='\t')













# TEST PARALELLISATION

# Solution Without Paralleization

import numpy as np
from time import time

# Prepare data
np.random.RandomState(100)
arr = np.random.randint(0, 10, size=[200000, 5])
data = arr.tolist()
data[:5]

def howmany_within_range(row, minimum, maximum):
    """Returns how many numbers lie within `maximum` and `minimum` in a given `row`"""
    count = 0
    for n in row:
        if minimum <= n <= maximum:
            count = count + 1
    return count

results = []
for row in data:
    results.append(howmany_within_range(row, minimum=4, maximum=8))

print(results[:5])

# Parallelizing using Pool.apply()

import multiprocessing as mp

# Step 1: Init multiprocessing.Pool()
pool = mp.Pool(mp.cpu_count())

# Step 2: `pool.apply` the `howmany_within_range()`
results = [pool.apply(howmany_within_range, args=(row, 4, 8)) for row in data]

# Step 3: Don't forget to close
pool.close()

print(results[:5])

# Redefine, with only 1 mandatory argument.
def howmany_within_range_rowonly(row, minimum=4, maximum=8):
    count = 0
    for n in row:
        if minimum <= n <= maximum:
            count = count + 1
    return count

pool = mp.Pool(mp.cpu_count())

results = pool.map(howmany_within_range_rowonly, [row for row in data])

pool.close()

print(results[:5])

# Parallelizing with Pool.starmap()
pool = mp.Pool(mp.cpu_count())
results = pool.starmap(howmany_within_range, [(row, 4, 8) for row in data])
pool.close()
print(results[:5])


# Parallel processing with Pool.apply_async()
pool = mp.Pool(mp.cpu_count())

results = []

# Step 1: Redefine, to accept `i`, the iteration number
def howmany_within_range2(i, row, minimum, maximum):
    """Returns how many numbers lie within `maximum` and `minimum` in a given `row`"""
    count = 0
    for n in row:
        if minimum <= n <= maximum:
            count = count + 1
    return (i, count)


# Step 2: Define callback function to collect the output in `results`
def collect_result(result):
    global results
    results.append(result)


# Step 3: Use loop to parallelize
for i, row in enumerate(data):
    pool.apply_async(howmany_within_range2, args=(i, row, 4, 8), callback=collect_result)

# Step 4: Close Pool and let all the processes complete
pool.close()
pool.join()  # postpones the execution of next line of code until all processes in the queue are done.

# Step 5: Sort results [OPTIONAL]
results.sort(key=lambda x: x[0])
results_final = [r for i, r in results]

print(results_final[:5])

# Parallelizing with Pool.starmap_async()

def howmany_within_range2(i, row, minimum, maximum):
    """Returns how many numbers lie within `maximum` and `minimum` in a given `row`"""
    count = 0
    for n in row:
        if minimum <= n <= maximum:
            count = count + 1
    return (i, count)

pool = mp.Pool(mp.cpu_count())
results = []

results = pool.starmap_async(howmany_within_range2, [(i, row, 4, 8) for i, row in enumerate(data)]).get()
pool.close()
print(results[:5])


import numpy as np
import pandas as pd
import multiprocessing as mp

df = pd.DataFrame(np.random.randint(3, 10, size=[5, 2]))
print(df.head())