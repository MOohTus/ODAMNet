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
os.chdir('D:\\Morgane\\Work\\MMG\\05_EJP_RD\\WF_Environment\\EnvironmentProject\\test\\InputData\\')

# Read files and create dict of them
# geneSet = '/home/morgane/Documents/05_EJPR_RD/WF_Environment/EnvironmentProject/test/InputData/InputFile_DOMINO_tnfa_active_genes_file.txt'
# network = '/home/morgane/Documents/05_EJPR_RD/WF_Environment/EnvironmentProject/test/InputData/InputFile_DOMINO_string.sif'

geneSet = 'InputFile_DOMINO_tnfa_active_genes_file.txt'
network = 'InputFile_DOMINO_string.sif'

data_dict = {
    'Network file name': network,
    'Active gene file name': geneSet
}

files_dict = {
    'Network file contents': open(network, 'rb'),
    'Active gene file contents': open(geneSet, 'rb')
}

response = requests.post(url='http://domino.cs.tau.ac.il/upload', data=data_dict, files=files_dict)
response
response.text

response_dict = response.json()

