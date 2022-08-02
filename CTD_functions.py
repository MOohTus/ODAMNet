#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Morgane T.

CTD functions
"""

# Libraries
from datetime import datetime
import requests
import re


# Debugging part / Global parameters
# CTDFile = '/home/morgane/Documents/05_EJPR_RD/WF_Environment/EnvironmentProject/test/InputData/InputFile_CTD_vitaminAD.txt'
# association = 'hierarchicalAssociations'
# nbPub = 2
# listFileName = CTDFile
# chemList = featureNameList
# outputPath = '/home/morgane/'

# Functions
# def readListFile(listFileName):
#     """
#     Read a list file (composed of gene names or chemical names)
#
#     :param str listFileName:
#     :return:
#         - **featureNameList** (*list*) – List of feature names
#     """
#     featureNameList = []
#     try:
#         with open(listFileName, 'r') as listFileHandler:
#             for line in listFileHandler:
#                 featureNameList.append(line.rstrip())
#         return featureNameList
#     except IOError:
#         print("I/O error while reading input file.")


def readListFile(listFile):
    featureNameList = []
    for line in listFile.readlines():
        featureNameList.append(line.rstrip())
    return featureNameList


def readCTDFile(CTDFile, nbPub, outputPath):
    # Parameters
    targetGenesList = []
    targetGenesDict = {}
    chemNameList = []
    outputLines = []
    chemName = ''

    for line in CTDFile:
        lineList = line.rstrip().split("\t")
        if len(lineList[8].split("|")) >= nbPub:
            outputLines.append("\t".join(lineList))
            # Gene name extraction
            geneName = lineList[4]
            if geneName not in targetGenesList:
                targetGenesList.append(geneName)
            # Query name extraction
            chemName = lineList[0].upper()
            if chemName not in chemNameList:
                chemNameList.append(chemName)
    # Dictionary creation
    targetGenesDict["_".join([chemName])] = targetGenesList

    # Write filtered result into file
    filteredResultFileName = outputPath + "/CTD_requestFiltered_" + "_".join([chemName]) + ".tsv"
    with open(filteredResultFileName, 'w') as outputFileHandler:
        for line in outputLines:
            outputFileHandler.write(line)
            outputFileHandler.write("\n")

    # Return
    return targetGenesDict


# def readCTDFile(CTDFileName, nbPub):
#     """
#     Read CTD File.
#     This file is created from the CTD request using an environmental factor (Raw file)
#
#     :param str CTDFileName:
#     :return:
#         - **chemNameList** (*list*) – List of chemical names
#     """
#
#     # CTDFile = "/home/morgane/Documents/05_EJPR_RD/WF_Environment/EnvironmentProject/test/VitaminAD/OutputOverlapResults/CTD_request_D014801.tsv"
#
#     targetGenesList = []
#     targetGenesDict = {}
#     chemNameList = []
#
#     try:
#         with open(CTDFileName, 'r') as CTDFileHandler:
#             for line in CTDFileHandler:
#                 lineList = line.rstrip().split("\t")
#                 if len(lineList[8].split("|")) >= nbPub:
#                     # Gene name extraction
#                     geneName = lineList[4]
#                     if geneName not in targetGenesList:
#                         targetGenesList.append(geneName)
#                     # Query name extraction
#                     chemName = lineList[0].upper()
#                     if chemName not in chemNameList:
#                         chemNameList.append(chemName)
#             # Dictionary creation
#             targetGenesDict["_".join([chemName])] = targetGenesList
#         return targetGenesDict
#     except IOError:
#         print("I/O error while reading CTD file.")


def CTDrequest(chemName, association, outputPath, nbPub):
    """
    Function requests CTD database.

    Search all genes which interact with the chemical given in input.
    Could be several chemicals names. Analysis will be done like if it's only one chemical.
    If hierarchicalAssociations is used, chemical related to the chemical given in input are used as query.
    Focus on genes present in Homo sapiens.

    :param str chemName: chemical name of MeSH ids string
    :param str association: association name (hierarchicalAssociations or directAssociations)
    :param str outputPath: Folder path to save the results
    :param int nbPub: Number of references needed to keep an interaction

    :return:
        - **homoGenesList** (*list*) – List of genes which interact with chemicals given in input (only Homo sapiens)
        - **chemMeSH** (*str*) – Composition of MeSH ID from chemicals given in input
    """
    # Parameters
    URL = "http://ctdbase.org/tools/batchQuery.go"
    PARAMS = {'inputType': "chem", 'inputTerms': chemName, 'report': "genes_curated", 'format': "tsv",
              'inputTermSearchType': association}
    homoResultsList = []
    homoResultsListReferences = []
    homoGenesList = []
    meshNamesDict = {}
    chemMeSHList = []

    # Request CTD
    requestResult = requests.get(url=URL, params=PARAMS)
    requestResultList = requestResult.text.split("\n")

    # Extract results only for Homo sapiens
    for element in requestResultList:
        elementList = element.split("\t")
        # resultsList.append(elementList)
        if re.match('#', elementList[0]):
            elementList[0] = re.sub('# ', '', elementList[0])
            homoResultsList.append(elementList)
        else:
            if re.match(PARAMS['inputTerms'].lower(), elementList[0]):
                if elementList[6] == 'Homo sapiens':
                    homoResultsList.append(elementList)
                    refList = elementList[8].split('|')
                    if len(refList) >= nbPub:
                        homoResultsListReferences.append(elementList)
                        if elementList[4] not in homoGenesList:
                            homoGenesList.append(elementList[4])
                    if elementList[1].lower() not in meshNamesDict:
                        meshNamesDict[elementList[1].lower()] = elementList[2]

    # Result len
    # len(homoResultsList)
    # len(resultsList)

    # Build name of output results file
    for chem in chemName.split('|'):
        if chem in meshNamesDict:
            chemMeSHList.append(meshNamesDict[chem.lower()])
        else:
            chemMeSHList.append(chem)
    chemMeSH = '_'.join(chemMeSHList)
    date = datetime.today().strftime('%Y_%m_%d')
    resultFileName = outputPath + '/CTD_request_' + chemMeSH + '_' + date + '.tsv'
    filteredResultFileName = outputPath + '/CTD_requestFiltered_' + chemMeSH + '_' + date + '.tsv'

    # Write result into file
    with open(resultFileName, 'w') as outputFileHandler:
        for resultLine in homoResultsList:
            outputFileHandler.write('\t'.join(resultLine))
            outputFileHandler.write('\n')

    # Write filtered result into file
    with open(filteredResultFileName, 'w') as outputFileHandler:
        for resultLine in homoResultsListReferences:
            outputFileHandler.write('\t'.join(resultLine))
            outputFileHandler.write('\n')

    # print(chemMeSH + " - Total number of interactions in the request : " + str(len(homoResultsList)))
    # print(chemMeSH + " - Number of uniq chemicals in the request : " + str(len(meshNamesDict)))
    # print(chemMeSH + " - Number of uniq target genes : " + str(len(homoGenesList)))
    # print('\n')

    return chemMeSH, homoGenesList


def CTDrequestFromList(chemList, association, outputPath, nbPub):
    """
    Make CTD request for each chemical present in the list given in input.
    Each element can be composed of one or more element.
    If several element, the analysis will be done like if there is only one chemical.

    :param list chemList: List of chemical to request to CTD (MeSH IDs or chemical names)
    :param str association: association name (hierarchicalAssociations or directAssociations)
    :param str outputPath: Folder path to save the results
    :param int nbPub: Number of references needed to keep an interaction


    :return:
        - **chemTargetsDict** (*dict*) – Dict composed of interaction genes list for each chemical
    """
    # Parameters
    chemTargetsDict = {}
    # For each chemical, request CTD
    for chem in chemList:
        chemNamesList = chem.rstrip().split(';')
        chemNamesString = '|'.join(chemNamesList)
        chemNames, chemTargetsList = CTDrequest(chemName=chemNamesString, association=association, outputPath=outputPath, nbPub=nbPub)
        chemTargetsDict[chemNames] = chemTargetsList
    return chemTargetsDict


def targetExtraction(CTDFile, directAssociations, outputPath, nbPub):
    """
    Read environmental factor file
    Request CTD and extract target genes
    Save results into output file
    Return the gene targets list

    :param CTDFile:
    :param directAssociations:
    :param outputPath:
    :param nbPub:

    :return:
    """
    if directAssociations:
        association = 'directAssociations'
    else:
        association = 'hierarchicalAssociations'

    # # Check if outputPath exist and create it if it does not
    # if not os.path.exists(outputPath):
    #     os.makedirs(outputPath, exist_ok=True)

    # Read CTD file and request CTD database
    # print('\nCTD request: ')
    chemNameList = readListFile(CTDFile)
    chemTargetsDict = CTDrequestFromList(chemList=chemNameList, association=association,
                                         outputPath=outputPath, nbPub=nbPub)

    return chemTargetsDict
