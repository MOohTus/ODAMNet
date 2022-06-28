#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Morgane T.

DOMINO functions
"""

# Libraries
from alive_progress import alive_bar
import requests
import os

# Change work directory
os.chdir('/home/morgane/Documents/05_EJPR_RD/WF_Environment/EnvironmentProject/test/InputData/')
## os.chdir('D:\\Morgane\\Work\\MMG\\05_EJP_RD\\WF_Environment\\EnvironmentProject\\test\\InputData\\')

# Read files and create dict of them
# geneSet = '/home/morgane/Documents/05_EJPR_RD/WF_Environment/EnvironmentProject/test/InputData/InputFile_DOMINO_tnfa_active_genes_file.txt'
# network = '/home/morgane/Documents/05_EJPR_RD/WF_Environment/EnvironmentProject/test/InputData/InputFile_DOMINO_string.sif'


## geneSet = 'InputFile_DOMINO_tnfa_active_genes_file.txt'
## network = 'InputFile_DOMINO_string.sif'
## --> WORK
## ENSEMBL

# geneSet = 'InputFile_DOMINO_D014801.txt'
# network = 'InputFile_DOMINO_string.sif'
## --> DON'T WORK
## SYMBOLS + ENSEMBL

# geneSet = 'InputFile_DOMINO_D014801.txt'
# network = 'InputFile_DOMINO_PPI_Janv2021.sif'
## --> DON'T WORK
## SYMBOLS

# geneSet = 'InputFile_DOMINO_D014801_ENSEMBL.txt'
# network = 'InputFile_DOMINO_string.sif'
## --> WORK
## ENSEMBL

geneSet = 'DOMINO_inputGeneList_D014807.txt'
network = 'InputFile_PPI_2016.sif'
## --> DON'T WORK
## SYMBOLS

data_dict = {
    'Network file name': network,
    'Active gene file name': geneSet
}
files_dict = {
    'Network file contents': open(network, 'rb'),
    'Active gene file contents': open(geneSet, 'rb')
}
with alive_bar(title='Search active modules using DOMINO', theme='musical') as bar:
    response = requests.post(url='http://domino.cs.tau.ac.il/upload', data=data_dict, files=files_dict)
    bar()

print(response)

response_dict = response.json()
activeModules_list = response_dict['algOutput']['DefaultSet']['modules']
print(activeModules_list.keys())
print(activeModules_list)