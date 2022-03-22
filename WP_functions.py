#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Morgane T.

WikiPathways functions
"""

# Libraries
from SPARQLWrapper import SPARQLWrapper, TSV


# Functions
def readRequestResultsWP(request):
    """
    Read request from WP.
    Parse and extract information from request.

    :param bytes request: request from WikiPathway

    :return:
        - **dictionary** (*dictionary*) – Dict of genes for each WikiPathway
        - **WPdictionary** (*dictionary*) – Dict of titles for each WikiPathway
    """
    # Parameters
    dictionary = {}
    WPdictionary = {}

    # Read and extract elements from WP
    requestString = request.decode()
    requestString = requestString.replace('\"', '')
    listOfPathways = requestString.rstrip().split('\n')
    for line in listOfPathways:
        listLine = line.split('\t')
        if listLine[2] != 'HGNC':
            listLine[2] = listLine[2].split('/')[4]
        if listLine[0] in dictionary.keys():
            dictionary[listLine[0]].append(listLine[2])
        else:
            dictionary[listLine[0]] = [listLine[2]]
            WPdictionary[listLine[0]] = listLine[1]
    return dictionary, WPdictionary


def rareDiseasesWPrequest(outputPath):
    """
    Function requests WikiPathway database.

    Search all WikiPathways related to Rare Diseases.
    Focus on pathways related with Homo sapiens.
    Write results into result file.

    :param str outputPath: Folder path to save the results

    :return:
        - **genesDict** (*dictionary*) – Dict of genes for each RD WikiPathway
        - **WPDict** (*dictionary*) – Dict of titles for each RD WikiPathway
    """
    # Parameters
    genesDict = {}
    WPDict = {}
    outputList = []
    resultFileName = outputPath + "/WP_RareDiseases_request.tsv"
    sparql = SPARQLWrapper("https://sparql.wikipathways.org/sparql")
    sparql.setReturnFormat(TSV)

    # Query - Extract gene HGNC ID from RD pathways
    sparql.setQuery("""
    SELECT DISTINCT ?WPID (?title as ?pathways) (?hgncId as ?HGNC)
        WHERE {
          {
            ?pathway wp:ontologyTag cur:RareDiseases ;
                    a wp:Pathway ;
                    wp:organismName "Homo sapiens" ;
                    dc:title ?title ; 
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
                    dc:title ?title ;
                    dcterms:identifier ?WPID.
            ?protein a wp:Protein ;
                    dcterms:isPartOf ?pathway ;
                    wp:bdbHgncSymbol ?hgncId .
            }
        } ORDER BY ?WPID
    """)
    try:
        genesReq = sparql.queryAndConvert()
        genesDict, WPDict = readRequestResultsWP(genesReq)
    except Exception as e:
        print(e)

    # Parsing for output
    for key in genesDict:
        size = str(len(genesDict[key]))
        composition = ' '.join(genesDict[key])
        outputList.append(''.join([key, '\t', WPDict[key], '\t', size, '\t', composition, '\n']))
    # Write results into file - Write size and composition of each WP
    with open(resultFileName, 'w') as outputFileHandler:
        for line in outputList:
            outputFileHandler.write(line)

    return genesDict, WPDict


def allGenesFromWP():
    """
    Extract all gene HGNC ID from Homo sapiens WP

    :return:
        - **geneSetWP** (*list*) – List of uniq genes found in Homo sapiens WP
    """
    # Parameters
    geneSetWP = []
    sparql = SPARQLWrapper("https://sparql.wikipathways.org/sparql")
    sparql.setReturnFormat(TSV)

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
