#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Morgane T.

WikiPathways functions
"""

# Libraries
from SPARQLWrapper import SPARQLWrapper, CSV


# Functions
def readRequestResultsWP(request):
    """
    Read request from WP.

    :param request: request from WikiPathway
    :return:
    """
    # Parameters
    dictionary = {}

    # Read and extract elements from WP
    requestSring = request.decode()
    requestSring = requestSring.replace('\"', '')
    listOfPathways = requestSring.rstrip().split('\n')
    for line in listOfPathways:
        listLine = line.split(',')
        if listLine[1] != 'HGNC':
            listLine[1] = listLine[1].split('/')[4]
        if listLine[0] in dictionary.keys():
            dictionary[listLine[0]].append(listLine[1])
        else:
            dictionary[listLine[0]] = [listLine[1]]
    return dictionary


def rareDiseasesWPrequest(resultFileName):
    """
    Function requests WikiPathway database.

    Search all WikiPathways related to Rare Diseases.
    Focus on pathways related with Homo sapiens.
    Write results into result file.

    :param str resultFileName: output file name where write request results

    :return:
        - **genesDict** (*dictionary*) – Dict of genes for each WikiPathway found
    """
    # Parameters
    genesDict = {}
    outputList = []
    sparql = SPARQLWrapper("https://sparql.wikipathways.org/sparql")
    sparql.setReturnFormat(CSV)

    # Query - Extract gene HGNC ID from RD pathways
    sparql.setQuery("""
    SELECT DISTINCT ?WPID (?hgncId as ?HGNC)
        WHERE {
          {
            ?pathway wp:ontologyTag cur:RareDiseases ;
                    a wp:Pathway ;
                    wp:organismName "Homo sapiens" ;
                    dcterms:identifier ?WPID.
            ?gene a wp:GeneProduct ;
                    dcterms:isPartOf ?pathway ;
                    wp:bdbHgncSymbol ?hgncId .
            }
          UNION
          {
            ?pathway wp:ontologyTag cur:RareDiseases ;
                    a wp:Pathway ;
                    wp:organismName "Homo sapiens" ;
                    dcterms:identifier ?WPID.
            ?protein a wp:Protein ;
                    dcterms:isPartOf ?pathway ;
                    wp:bdbHgncSymbol ?hgncId .
            }
        } ORDER BY ?WPID
    """)
    try:
        genesReq = sparql.queryAndConvert()
        genesDict = readRequestResultsWP(genesReq)
    except Exception as e:
        print(e)

    # Parsing for output
    for key in genesDict:
        size = str(len(genesDict[key]))
        composition = ' '.join(genesDict[key])
        outputList.append(''.join([key, '\t', size, '\t', composition, '\n']))
    # Write results into file - Write size and composition of each WP
    with open(resultFileName, 'w') as outputFileHandler:
        for line in outputList:
            outputFileHandler.write(line)

    return genesDict


def allGenesFromWP():
    """
    Extract all gene HGNC ID from Homo sapiens WP

    :return:
        - **geneSetWP** (*list*) – List of uniq genes found in Homo sapiens WP
    """
    # Parameters
    allGenesList = []
    geneSetWP = []
    sparql = SPARQLWrapper("https://sparql.wikipathways.org/sparql")
    sparql.setReturnFormat(CSV)

    # Query - Extract all genes from Human WP (HGNC ID)
    sparql.setQuery("""
    SELECT DISTINCT (?hgncId as ?HGNC)
        WHERE {
          {
            ?pathway a wp:Pathway ;
                    wp:organismName "Homo sapiens" ;
                    dcterms:identifier ?WPID.
            ?gene a wp:GeneProduct ;
                    dcterms:isPartOf ?pathway ;
                    wp:bdbHgncSymbol ?hgncId .
            }
          UNION
          {
            ?pathway a wp:Pathway ;
                    wp:organismName "Homo sapiens" ;
                    dcterms:identifier ?WPID.
            ?protein a wp:Protein ;
                    dcterms:isPartOf ?pathway ;
                    wp:bdbHgncSymbol ?hgncId .
            }
        } ORDER BY ?HGNC
    """)
    try:
        allGenesReq = sparql.queryAndConvert()
        allGenesString = allGenesReq.decode()
        allGenesString = allGenesString.replace('\"', '')
        allGenesList = allGenesString.rstrip().split('\n')
        for gene in allGenesList:
            if gene != 'HGNC':
                geneSetWP.append(gene.split('/')[4])
    except Exception as e:
        print(e)

    return geneSetWP
