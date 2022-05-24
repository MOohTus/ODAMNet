#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Morgane T.

DOMINO functions
"""

# Libraries
import requests
import os

# Change work directory
os.chdir('/home/morgane/Documents/05_EJPR_RD/WF_Environment/EnvironmentProject/test/InputData/')

# Read files and create dict of them
# geneSet = '/home/morgane/Documents/05_EJPR_RD/WF_Environment/EnvironmentProject/test/InputData/InputFile_DOMINO_tnfa_active_genes_file.txt'
# network = '/home/morgane/Documents/05_EJPR_RD/WF_Environment/EnvironmentProject/test/InputData/InputFile_DOMINO_string.sif'

geneSet = 'InputFile_DOMINO_tnfa_active_genes_file.txt'
network = 'InputFile_DOMINO_string.sif'

data_dict = {}
with open(geneSet, 'r') as geneSetFileHandler:
    data_dict['Active gene file name'] = 'InputFile_DOMINO_tnfa_active_genes_file.txt'
    data_dict['Active gene file contents'] = geneSetFileHandler
    with open(network, 'r') as networkFileHandler:
        data_dict['Network file name'] = 'InputFile_DOMINO_string.sif'
        data_dict['Network file contents'] = networkFileHandler

        response = requests.post(url='http://domino.cs.tau.ac.il/', data=data_dict)

response
response.text


data_dict = {
    'Network file name': 'InputFile_DOMINO_string.sif',
    'Network file contents': open('InputFile_DOMINO_string.sif', 'rb'),
    'Active gene file name': 'InputFile_DOMINO_tnfa_active_genes_file.txt',
    'Active gene file contents': open('InputFile_DOMINO_tnfa_active_genes_file.txt', 'rb')
}
response = requests.post(url='http://domino.cs.tau.ac.il/upload', files=data_dict)
print(response.text)