#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Morgane T.

CTD functions
"""

# Libraries
import requests
import re


# Functions
def readCTDFile(CTDFile):
    """
    Read CTD File

    This file contains one column of chemical MeSH IDs or chemical names.
    One name per line.

    :param str CTDFile: File path of the chemical name (or MeSH ID) list.

    :return:
        - **lChemName** (*list*) – List of chemical names
    """
    chemNameList = []
    try:
        with open(CTDFile, 'r') as CTDFileHandler:
            for line in CTDFileHandler:
                chemNameList.append(line.rstrip())
            return chemNameList
    except IOError:
        print("I/O error while reading CTD file.")


def CTDrequest(chemName, association):
    """
    Function requests CTD database.

    Search all genes which interact with the chemical given in input.
    If hierarchicalAssociations is used, chemical related to the chemical given in input are used as query.
    Focus on genes present in Homo sapiens.

    :param str chemName: chemical name of MeSH ids string
    :param str association: association name (hierarchicalAssociations or directAssociations)

    :return:
        - **homoGenesDict** (*dict*) – Dictionary of genes which interact with chemicals given in input (only Homo sapiens)
    """
    # Parameters
    URL = "http://ctdbase.org/tools/batchQuery.go"
    PARAMS = {'inputType': "chem", 'inputTerms': chemName, 'report': "genes_curated", 'format': "tsv",
              'inputTermSearchType': association}
    homoResultsList = []
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
            elementList[0] = re.sub('# ', "", elementList[0])
            homoResultsList.append(elementList)
        else:
            if re.match(PARAMS['inputTerms'].lower(), elementList[0]):
                if elementList[6] == "Homo sapiens":
                    homoResultsList.append(elementList)
                    if elementList[4] not in homoGenesList:
                        homoGenesList.append(elementList[4])
                    if elementList[1].lower() not in meshNamesDict:
                        meshNamesDict[elementList[1].lower()] = elementList[2]

    # Result len
    # len(homoResultsList)
    # len(resultsList)

    # Write result into file
    for chem in chemName.split("|"):
        if(chem in meshNamesDict):
            chemMeSHList.append(meshNamesDict[chem.lower()])
        else:
            chemMeSHList.append(chem)
    chemMeSH = "_".join(chemMeSHList)
    resultFileName = "test/CTD_request_" + chemMeSH + ".tsv"
    with open(resultFileName, 'w') as outputFileHandler:
        for resultLine in homoResultsList:
            outputFileHandler.write("\t".join(resultLine))
            outputFileHandler.write("\n")

    return chemMeSH, homoGenesList


def CTDrequestFromList(chemList, association):
    """

    :param chemList:
    :param association:

    :return:
    """
    # Parameters
    chemTargetsList = []
    chemTargetsDict = {}

    for chem in chemList:
        chemNamesList = chem.rstrip().split(';')
        chemNamesString = "|".join(chemNamesList)
        chemNames, chemTargetsList = CTDrequest(chemName=chemNamesString, association=association)
        chemTargetsDict[chemNames] = chemTargetsList

    return chemTargetsDict
