#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Morgane T.

WikiPathways functions
"""

# Libraries
import os.path
from SPARQLWrapper import SPARQLWrapper, TSV
from datetime import datetime
from alive_progress import alive_bar


# Functions
def readRequestResultsWP(WPrequestResult):
    """
    Read request from WP.

    Parse and extract information from request.
    Extract genes, names and IDs of pathways.

    :param bytes WPrequestResult: request result from WikiPathway

    :return:
        - **genesWPdict** (*dictionary*) – Dict of genes for each WikiPathway
        - **nameWPdict** (*dictionary*) – Dict of titles for each WikiPathway
    """
    # Parameters
    genesWPdict = {}
    nameWPdict = {}

    # Read and extract elements from WP
    requestString = WPrequestResult.decode()
    requestString = requestString.replace('\"', '')
    listOfPathways = requestString.rstrip().split('\n')
    for line in listOfPathways:
        listLine = line.split('\t')
        if listLine[2] != 'HGNC':
            listLine[2] = listLine[2].split('/')[4]
        if listLine[0] in genesWPdict.keys():
            genesWPdict[listLine[0]].append(listLine[2])
        else:
            genesWPdict[listLine[0]] = [listLine[2]]
            nameWPdict[listLine[0]] = listLine[1]

    # Return
    return genesWPdict, nameWPdict


def rareDiseasesWPrequest(outputPath):
    """
    Function requests WikiPathway database.

    Search all WikiPathways related to Rare Diseases.
    Focus on pathways related with Homo sapiens.
    Write results into result file.

    :param str outputPath: Folder path to save the results

    :return:
        - **genesWPDict** (*dictionary*) – Dict of genes for each RD WikiPathway
        - **namesWPDict** (*dictionary*) – Dict of names for each RD WikiPathway
        - **pathwayOfInterestList** (*list*) – Pathway names list
    """
    # Parameters
    genesWPDict = {}
    namesWPDict = {}
    outputList = []
    pathwayOfInterestList = []
    date = datetime.today().strftime('%Y_%m_%d')
    resultFileName = outputPath + '/WP_RareDiseases_request_' + date + '.gmt'
    sparql = SPARQLWrapper('https://sparql.wikipathways.org/sparql')
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
        genesWPDict, namesWPDict = readRequestResultsWP(genesReq)
    except Exception as e:
        print(e)

    # Parsing for output
    for key in genesWPDict:
        composition = '\t'.join(genesWPDict[key])
        outputList.append(''.join([key, '\t', namesWPDict[key], '\t', composition, '\n']))
        if key != 'WPID':
            pathwayOfInterestList.append(key)

    # Write results into file - Write composition of each WP
    with open(resultFileName, 'w') as outputFileHandler:
        for line in outputList:
            outputFileHandler.write(line)

    # Return
    return genesWPDict, namesWPDict, pathwayOfInterestList


def allHumanGenesFromWP(outputPath):
    """
    Extract all gene HGNC ID from Homo sapiens WP.
    Write request result into output file.

    :param str outputPath: Folder path to save the results

    :return:
        - **backgroundsDict** (*dict*) – dict of all human genes from WP
    """
    # Parameters
    genesWPDict = {}
    namesWPDict = {}
    outputList = []
    date = datetime.today().strftime('%Y_%m_%d')
    resultFileName = outputPath + '/WP_allPathways_request_' + date + '.gmt'
    sparql = SPARQLWrapper('https://sparql.wikipathways.org/sparql')
    sparql.setReturnFormat(TSV)
    bgName = 'WikiPathway_' + date
    backgroundsDict = {bgName: []}

    # Query - Extract all genes from Human WP (HGNC ID)
    sparql.setQuery("""
        SELECT DISTINCT ?WPID (?title as ?pathways) (?hgncId as ?HGNC)
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
        genesReq = sparql.queryAndConvert()
        genesWPDict, namesWPDict = readRequestResultsWP(genesReq)
    except Exception as e:
        print(e)

    # Parsing for output
    for key in genesWPDict:
        composition = '\t'.join(genesWPDict[key])
        outputList.append(''.join([key, '\t', namesWPDict[key], '\t', composition, '\n']))
    # Write results into file - Write composition of each WP
    with open(resultFileName, 'w') as outputFileHandler:
        for line in outputList:
            outputFileHandler.write(line)

    # Remove redundancy
    for pathway in genesWPDict:
        for gene in genesWPDict[pathway]:
            if gene not in backgroundsDict[bgName]:
                backgroundsDict[bgName].append(gene)

    # Return
    return backgroundsDict


def readGMTFile(GMTFile):
    """
    Parse and extract information from GMT file.

    :param FILE GMTFile: content of GMT file

    :return:
        - **genesWPDict** (*dict*) – Dict of genes for each WikiPathway
       - **namesWPDict** (*dict*) – Dict of titles for each WikiPathway
       - **pathwaysOfInterestList** (*list*) – Pathway names list
    """
    # Parameters
    namesWPDict = {}
    genesWPDict = {}
    pathwaysOfInterestList = []

    # Read GMT file
    for line in GMTFile:
        lineList = line.rstrip('\n').split('\t')
        WPID = lineList[0]
        genesList = lineList[2:]
        description = lineList[1]
        # Pathway names dict
        namesWPDict[WPID] = description
        # Pathway genes dict
        genesWPDict[WPID] = genesList
        # List of pathways of interest
        if WPID != 'WPID':
            pathwaysOfInterestList.append(WPID)

    # Return
    return genesWPDict, namesWPDict, pathwaysOfInterestList


def readBackgroundsFile(backgroundsFile):
    """
    Read a backgrounds file
    Each line contains a background file name source correspondant of each pathway of interest
    The order of sources depends on the order of pathways of interest.

    :param filename backgroundsFile: File name of the background source of each pathway of interest

    :return:
        - **backgroundsDict** (*dict*) – Dictionary of the background genes from different sources
        - **backgroundsList** (*list*) – List of the background gene sources to use
    """
    # Parameters
    backgroundsDict = {}
    backgroundsList = []
    folder = os.path.dirname(backgroundsFile.name)

    # Read backgrounds file
    with alive_bar(title='Background genes dictionary creation', theme='musical') as bar:
        for background in backgroundsFile:
            background = background.strip()
            backgroundsList.append(background)
            name = background
            if name not in backgroundsDict:
                backgroundsDict[name] = []
                # Read and extract genes from a background file
                with open((folder + '/' + background), 'r') as bgFile:
                    for line in bgFile:
                        linesList = line.strip().split('\t')
                        for gene in linesList[2:]:
                            if gene not in backgroundsDict[name] and gene != 'HGNC':
                                backgroundsDict[name].append(gene)
            backgroundsDict[name].sort()
        bar()

    # Return
    return backgroundsDict, backgroundsList
