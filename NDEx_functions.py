#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@author: Morgane T.

NDEx request network
"""

# Libraries
import json
import ndex2


# Functions
def downloadNDExNetwork(networkUUID, outputFileName, symbolBool):
    """
    Download a network from NDEx project
    """
    # Create NDEx2 python client
    client = ndex2.client.Ndex2()

    # Download
    client_resp = client.get_network_as_cx_stream(networkUUID)

    # Convert downloaded network to NiceCXNetwork object
    net_cx = ndex2.create_nice_cx_from_raw_cx(json.loads(client_resp.content))
    net_cx.print_summary()

    #
    df = net_cx.to_pandas_dataframe()
    print(df)
    return(net_cx)

    # node_name_dict = {}
    # name = ''
    # # Build dictionary and print out all the nodes
    # for node_id, node_obj in net_cx.get_nodes():
    #     for el in net_cx.nodeAttributes[node_id]:
    #         if el['n'] == 'symbol':
    #             name = el['v']
    #     # print('node_id: ' + str(node_id) + ' node_obj: ' + str(node_obj) + ' name: ' + name)
    #     # node_name_dict[node_obj['n']] = {}
    #     # node_name_dict[node_obj['n']]['node_id'] = node_id
    #     # node_name_dict[node_obj['n']]['symbol'] = name
    #     node_name_dict[node_obj['n']] = name
    # # Print out dictionary
    # # print(str(node_name_dict))
    #
    # # Converte NiceCXNetwork to panda dataframe
    # df = net_cx.to_pandas_dataframe()
    # if symbolBool:
    #     df = df.replace(node_name_dict)
    # df.to_csv(outputFileName, index=False, sep='\t', na_rep='linked')


# Input
outputFileName = '/home/morgane/Documents/05_EJPR_RD/WF_Environment/EnvironmentProject/examples/InputData/NEDxNetworks.sif'










# Symbol IDs
networkUUID = '110ce6f7-86da-11e7-a10d-0ac135e8bacf' # HumanInteractome
networkUUID = '079f4c66-3b77-11ec-b3be-0ac135e8bacf' # Human Protein Reference Database (HPRD) PPI network
networkUUID = '08ba2a31-86da-11e7-a10d-0ac135e8bacf' # GIANT
networkUUID = 'cfcd4cdb-86da-11e7-a10d-0ac135e8bacf' # STRING
networkUUID = 'f1dd6cc3-0007-11e6-b550-06603eb7f303' # CoCaNet2
# ENSEMBL IDs / symbol in attributs
networkUUID = 'b0ed97ea-5fb9-11e9-9f06-0ac135e8bacf' # uterus
networkUUID = '21b32e30-5fb9-11e9-9f06-0ac135e8bacf' # liver
networkUUID = '4fde0a71-c571-11eb-9a85-0ac135e8bacf' # STRING / display name'
# Protein IDs / Gene names  (primary )
networkUUID = '5e6b0de3-c8fc-11eb-9a85-0ac135e8bacf' # Host receptor protein interaction network
# Mixe
networkUUID = '669f30a3-cee6-11ea-aaef-0ac135e8bacf' # BioGRID: Protein-Protein Interactions (SARS-CoV)
# Multiscale
networkUUID = '7fc70ab6-9fb1-11ea-aaef-0ac135e8bacf' # MuSIC
# Run
net_cx = downloadNDExNetwork(networkUUID, outputFileName, False)
net_cx.print_summary()
net_cx.nodeAttributes
