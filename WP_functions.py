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
        genesDict, WPDict = readRequestResultsWP(genesReq)
    except Exception as e:
        print(e)

    # Parsing for output
    for key in genesDict:
        composition = '\t'.join(genesDict[key])
        outputList.append(''.join([key, '\t', WPDict[key], '\t', composition, '\n']))
        if key != 'WPID':
            pathwayOfInterestList.append(key)
    # Write results into file - Write size and composition of each WP
    with open(resultFileName, 'w') as outputFileHandler:
        for line in outputList:
            outputFileHandler.write(line)

    return genesDict, WPDict, pathwayOfInterestList


# def allGenesFromWP(outputPath):
#     """
#     Extract all gene HGNC ID from Homo sapiens WP.
#     Write request result into output file.
#
#     :param str outputPath: Folder path to save the results
#
#     :return:
#         - **geneSetWP** (*list*) – List of uniq genes found in Homo sapiens WP
#     """
#     # Parameters
#     geneSetWP = []
#     date = datetime.today().strftime('%Y_%m_%d')
#     resultFileName = outputPath + "/WP_listOfAllHumanGenes_" + date + ".tsv"
#     sparql = SPARQLWrapper("https://sparql.wikipathways.org/sparql")
#     sparql.setReturnFormat(TSV)
#
#     # Query - Extract all genes from Human WP (HGNC ID)
#     sparql.setQuery("""
#     SELECT DISTINCT (?hgncId as ?HGNC)
#         WHERE {
#           {
#             ?pathway a wp:Pathway ;
#                     wp:organismName "Homo sapiens" ;
#                     dcterms:identifier ?WPID.
#             ?gene a wp:GeneProduct ;
#                     dcterms:isPartOf ?pathway ;
#                     wp:bdbHgncSymbol ?hgncId .
#             }
#           UNION
#           {
#             ?pathway a wp:Pathway ;
#                     wp:organismName "Homo sapiens" ;
#                     dcterms:identifier ?WPID.
#             ?protein a wp:Protein ;
#                     dcterms:isPartOf ?pathway ;
#                     wp:bdbHgncSymbol ?hgncId .
#             }
#         } ORDER BY ?HGNC
#     """)
#     try:
#         allGenesReq = sparql.queryAndConvert()
#         allGenesString = allGenesReq.decode()
#         allGenesString = allGenesString.replace('\"', '')
#         allGenesList = allGenesString.rstrip().split('\n')
#         for gene in allGenesList:
#             if gene != 'HGNC':
#                 geneSetWP.append(gene.split('/')[4])
#     except Exception as e:
#         print(e)
#
#     with open(resultFileName, 'w') as outputFileHandler:
#         for gene in geneSetWP:
#             outputFileHandler.write('%s\n' % gene)
#
#     return geneSetWP


def allGenesFromWP(outputPath):
    """
    Extract all gene HGNC ID from Homo sapiens WP.
    Write request result into output file.

    :param str outputPath: Folder path to save the results

    :return:
        - **geneSetWP** (*list*) – List of uniq genes found in Homo sapiens WP
    """
    # Parameters
    genesDict = {}
    WPDict = {}
    outputList = []
    date = datetime.today().strftime('%Y_%m_%d')
    resultFileName = outputPath + '/WP_allPathways_request_' + date + '.gmt'
    sparql = SPARQLWrapper('https://sparql.wikipathways.org/sparql')
    sparql.setReturnFormat(TSV)

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
        genesDict, WPDict = readRequestResultsWP(genesReq)
    except Exception as e:
        print(e)

    # Parsing for output
    for key in genesDict:
        composition = '\t'.join(genesDict[key])
        outputList.append(''.join([key, '\t', WPDict[key], '\t', composition, '\n']))
    # Write results into file - Write size and composition of each WP
    with open(resultFileName, 'w') as outputFileHandler:
        for line in outputList:
            outputFileHandler.write(line)

    bgName = 'WikiPathway_' + date
    backgroundsDict = {bgName: []}

    for pathway in genesDict:
        for gene in genesDict[pathway]:
            if gene not in backgroundsDict[bgName]:
                backgroundsDict[bgName].append(gene)

    return backgroundsDict


def readGMTFile(GMTFile):
    # Parameters
    WPDict = {}
    genesDict = {}
    pathwaysOfInterestList = []

    # Read GMT file
    for line in GMTFile:
        lineList = line.rstrip('\n').split('\t')
        WPID = lineList[0]
        genesList = lineList[2:]
        description = lineList[1]
        # Dictionary of description
        if WPID in WPDict:
            WPDict[WPID] = ' '.join([WPDict[WPID], description])
        else:
            WPDict[WPID] = description
        # Dictionary of genes
        if WPID in genesDict:
            genesDict[WPID] = ' '.join([WPDict[WPID], genesList])
        else:
            genesDict[WPID] = genesList
        # List of pathways of interest
        if WPID != 'WPID':
            pathwaysOfInterestList.append(WPID)

    # Return
    return genesDict, WPDict, pathwaysOfInterestList


# def readGMTFile(GMTFileName):
#     """
#     Read a GMT file from WP.
#     Request made : all pathways labeled as Rare Diseases pathways.
#
#     :param str GMTFileName: GMT file name
#
#     :return:
#         - **genesDict** (*dictionary*) – Dict of genes for each WikiPathway
#         - **WPDict** (*dictionary*) – Dict of titles for each WikiPathway
#     """
#     # Parameters
#     WPDict = {}
#     genesDict = {}
#
#     # Read GMT file
#     with open(GMTFileName, 'r') as GMTFileHandler:
#         for line in GMTFileHandler:
#             lineList = line.rstrip('\n').split('\t')
#             WPID = lineList[0]
#             genesList = lineList[3].split(' ')
#             description = lineList[1]
#             # Dictionary of description
#             if WPID in WPDict:
#                 WPDict[WPID] = " ".join([WPDict[WPID], description])
#             else:
#                 WPDict[WPID] = description
#             # Dictionary of genes
#             if WPID in genesDict:
#                 genesDict[WPID] = " ".join([WPDict[WPID], genesList])
#             else:
#                 genesDict[WPID] = genesList
#
#     # Return
#     return genesDict, WPDict


def readUniversFile(UniversFile):
    """
    Read a file to extract list of genes
    The file is composed of one column of genes
    These gene are all human genes in WP

    :param str UniversFile: Univers file content
    :return:
        - **geneSetWP** (*list*) – List of genes that composed the Univers (WP for human)
    """
    # Parameters
    geneSetWP = []

    # Read file with all genes inside univers
    for line in UniversFile:
        geneSetWP.append(line.rstrip('\n'))

    # Return
    return geneSetWP

# def readUniversFile(UniversFileName):
#     """
#     Open and read a file to extract list of genes.
#     The file is composed of one column of genes.
#     These genes are all human genes in WP.
#
#     :param str UniversFileName: Univers file name
#
#     :return:
#         - **geneSetWP** (*list*) – List of genes that composed the Univers (WP for human)
#     """
#     # Parameters
#     geneSetWP = []
#
#     # Read file with all genes inside univers
#     with open(UniversFileName, 'r') as universFileHandler:
#         for line in universFileHandler:
#             geneSetWP.append(line.rstrip('\n'))
#
#     # Return
#     return geneSetWP


# REPLACE readUniversFile() function
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
                with open((folder + '/' + background), 'r') as bgFile:
                    for line in bgFile:
                        linesList = line.strip().split('\t')
                        for gene in linesList[2:]:
                            if gene not in backgroundsDict[name] and gene != 'HGNC':
                                backgroundsDict[name].append(gene)
        bar()
    return backgroundsDict, backgroundsList
