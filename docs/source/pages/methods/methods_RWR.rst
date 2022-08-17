.. _RWR:

==================================================
Random Walk with Restart
==================================================

Principle
------------

- Measure proximity of every gene within a multilayer to the target genes
- It's a kind of diffusion analysis from the factor through different molecular interactions

Example 1 : data source from requests
---------------------------------------

Required options
""""""""""""""""""""

-f, --factorList FILENAME
    Contains a list of chemicals. Could be chemical names (e.g. vitamin A) or the MeSH identifier (e.g. D014801).
    The user can gives several chemicals in the same line : they will be grouped for the analysis.

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
""""""""""""""""""""

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


Command lines
""""""""""""""""""""

.. tabs::

    .. group-tab:: short

        .. code-block:: bash

           python3 main.py multixrank   --factorList examples/InputData/InputFile_factorsList.csv \
                                        --configPath examples/InputData/config_minimal.yml \
                                        --networksPath examples/InputData/ \
                                        --seedsFile examples/InputData/seeds.txt \
                                        --sifFileName example1_resultsNetwork.sif

    .. group-tab:: detailed

        .. code-block:: bash

           python3 main.py multixrank   --factorList examples/InputData/InputFile_factorsList.csv \
                                        --directAssociation False \
                                        --nbPub 2 \
                                        --configPath examples/InputData/config_minimal.yml \
                                        --networksPath examples/InputData/ \
                                        --seedsFile examples/InputData/seeds.txt \
                                        --sifFileName example1_resultsNetwork.sif \
                                        --top 10 \
                                        --outputPath examples/OutputResults_example1/


Example 2 : data source from database files
---------------------------------------------

Required options
""""""""""""""""""""

-c, --CTD_file FILENAME
    It's a tab-separated file from CTD request (e.g. created with an up to date analysis). Refers to XXX to have more information about the format.

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
""""""""""""""""""""

--nbPub INTEGER
    In CTD, an interaction between a gene and a molecule can have references.
    The user can set a threshold on the number of publications needed to extract the interaction.
    [default: 2]

--top INTEGER
    Threshold used to create the SIF network results.

-o, --outputPath PATH
    Name of the folder where save the results
    [default: OutputResults]

Command lines
""""""""""""""""""""

.. tabs::

    .. group-tab:: short

        .. code-block:: bash

            python3 main.py multixrank  --CTD_file examples/InputData/InputFile_CTD_request_D014801_2022_07_01.tsv \
                                        --configPath examples/InputData/config_minimal.yml \
                                        --networksPath examples/InputData/ \
                                        --seedsFile examples/InputData/seeds.txt \
                                        --sifFileName example2_resultsNetwork.sif

    .. group-tab:: detailed

        .. code-block:: bash

            python3 main.py multixrank  --CTD_file examples/InputData/InputFile_CTD_request_D014801_2022_07_01.tsv \
                                        --nbPub 2 \
                                        --configPath examples/InputData/config_minimal.yml \
                                        --networksPath examples/InputData/ \
                                        --seedsFile examples/InputData/seeds.txt \
                                        --sifFileName example2_resultsNetwork.sif \
                                        --top 10 \
                                        --outputPath examples/OutputResults_example2/


Example 3 : custom data source
---------------------------------------

Required options
""""""""""""""""""""

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
""""""""""""""""""""

--top INTEGER
    Threshold used to create the SIF network results.

-o, --outputPath PATH
    Name of the folder where save the results
    [default: OutputResults]



Data from paper *(Ozisik, 2022)*
""""""""""""""""""""""""""""""""""""""""

.. tabs::

    .. group-tab:: short

        .. code-block:: bash

            python3 main.py multixrank  --geneList examples/InputData/InputFromPaper/VitA-Balmer2002-Genes.txt \
                                        --configPath examples/InputData/config_minimal.yml \
                                        --networksPath examples/InputData/ \
                                        --seedsFile examples/InputData/seeds.txt \
                                        --sifFileName example3_resultsNetwork.sif

    .. group-tab:: detailed

        .. code-block:: bash

            python3 main.py multixrank  --geneList examples/InputData/InputFromPaper/VitA-Balmer2002-Genes.txt \
                                        --configPath examples/InputData/config_minimal.yml \
                                        --networksPath examples/InputData/ \
                                        --seedsFile examples/InputData/seeds.txt \
                                        --sifFileName example3_resultsNetwork.sif \
                                        --top 10 \
                                        --outputPath examples/OutputResults_example3/

