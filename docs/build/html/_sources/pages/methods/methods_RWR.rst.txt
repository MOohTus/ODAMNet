.. _RWR:

==================================================
Random Walk with Restart
==================================================

Principle
------------

.. note::

    The Ranwom Walk is performed using multiXrank [1]_
    (`website <https://multixrank-doc.readthedocs.io/en/latest/>`_ and `github <https://github.com/anthbapt/multixrank>`_).

This method measures the proximity of every gene within a multilayer to the target genes. Every gene from the list is
define as a seed. The walk start with a seed selected randomly. A score is given to each node and proportional of the time
how a node is visited during walks. More the score is high, more the node is visited, more the node is linked to the seed.

It's a kind of diffusion analysis from the genes through different molecular interactions.

Required options
--------------------

.. tip::

    You can mix input type. For instance, request CTD and give a custom GMT file of pathways of interest.
    Every combination is possible !

.. tabs::

    .. group-tab:: Request

        -f, --factorList FILENAME
            Contains a list of chemicals. Could be chemical names (e.g. vitamin A) or the MeSH identifier (e.g. D014801).
            The user can gives several chemicals in the same line : they will be grouped for the analysis.

    .. group-tab:: Request Files

        -c, --CTD_file FILENAME
            It's a tab-separated file from CTD request (e.g. created with an up to date analysis). Refers to XXX to have more information about the format.

    .. group-tab:: Custom Files

        -g, --geneList FILENAME
            List of gens of interest. One gene per line.

--configPath PATH
    Configuration file required by multiXrank tool. It could be short or very details (g.e. with tuned parameters).
    The short one contains the network and bipartite trees and the path of the seed file.
    If the user want more details go the the multiXrank's documentation :
    `github <https://github.com/anthbapt/multixrank>`__ /
    `doc <https://multixrank-doc.readthedocs.io/en/latest/>`__

--networksPath PATH
    The path of the repository that contains the multiplex folder.

--seedsFile FILENAME
    The path name of the seed file. This file contains the list of genes (g.e. target genes, interested genes)
    that are used as seed to start the walk.

--sifFileName FILENAME
    Output file name to save the result into a SIF file.


Optionals options
--------------------

--directAssociation BOOLEAN
    If TRUE, only the genes targeted by the chemical are extracted.
    If FALSE, the genes targeted by the chemical and all the descendant molecules are extracted.
    [default: True]

--nbPub INTEGER
    In CTD, an interaction between a gene and a molecule can have references.
    The user can set a threshold on the number of publications needed to extract the interaction.
    [default: 2]

--top INTEGER
    Threshold used to create the SIF network results.

-o, --outputPath PATH
    Name of the folder where save the results
    [default: OutputResults]


Command line examples
------------------------

.. tabs::

    .. group-tab:: Request

        .. code-block:: bash

            python3 main.py multixrank  --factorList examples/InputData/InputFile_factorsList.csv \
                                        --directAssociation False \
                                        --nbPub 2 \
                                        --configPath examples/InputData/config_minimal.yml \
                                        --networksPath examples/InputData/ \
                                        --seedsFile examples/InputData/seeds.txt \
                                        --sifFileName example1_resultsNetwork.sif \
                                        --top 10 \
                                        --outputPath examples/OutputResults_example1/

    .. group-tab:: Request Files

        .. code-block:: bash

            python3 main.py multixrank  --CTD_file examples/InputData/InputFile_CTD_request_D014801_2022_07_01.tsv \
                                        --nbPub 2 \
                                        --configPath examples/InputData/config_minimal.yml \
                                        --networksPath examples/InputData/ \
                                        --seedsFile examples/InputData/seeds.txt \
                                        --sifFileName example2_resultsNetwork.sif \
                                        --top 10 \
                                        --outputPath examples/OutputResults_example2/

    .. group-tab:: Custom Files

        .. code-block:: bash

            python3 main.py multixrank  --geneList examples/InputData/InputFromPaper/VitA-Balmer2002-Genes.txt \
                                        --configPath examples/InputData/config_minimal.yml \
                                        --networksPath examples/InputData/ \
                                        --seedsFile examples/InputData/seeds.txt \
                                        --sifFileName example3_resultsNetwork.sif \
                                        --top 10 \
                                        --outputPath examples/OutputResults_example3/

Networks available
--------------------

Users can use any multilayer and networks that they want. We propose on this project a set of networks build in the lab.

- multiplex
    - PPI
    - Reactome
    - Complex

- disease network
    - disconected diseases network, created from WP rare diseases pathways :ref:`newNet`
    - disease-disease network build with blablabla

Explanation and description of our multilayer (source, number of edges and nodes etc).

References
------------

.. [1] Baptista, A., Gonzalez, A., & Baudot, A. (2022). Universal multilayer network exploration by random walk with restart. Communications Physics, 5(1), 1-9.