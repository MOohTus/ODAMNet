.. _RWR:

==================================================
Random Walk with Restart
==================================================

Principle
------------

.. note::

    The Random Walk is performed using multiXrank [1]_ --
    :octicon:`mark-github;1em` `GitHub <https://github.com/anthbapt/multixrank>`_ :octicon:`book;1em` `ReadTheDocs <https://multixrank-doc.readthedocs.io/en/latest/>`_

This method measures the **proximity** of every gene within a multilayer to the target genes. Every gene from the list is
define as a **seed**. The walk starts with a seed, selected **randomly**. The proximity is represented by a score that could be use
for multiple analyse. More the score is high, more the node is closed to the seed.

It's a kind of **diffusion analysis** from the genes through different molecular interactions (:numref:`overviewFig` - right part).

*For more details, go to the paper* [1]_

Required arguments
--------------------

.. tip::

    You can mix input types. For instance, you can request CTD and give a custom GMT file of pathways of interest.
    **Every combination is possible!**

.. tabs::

    .. group-tab:: Request

        -f, --factorList FILENAME
            Contains a list of chemicals. They have to be in **MeSH** identifiers (e.g. D014801).
            You can give several chemicals in the same line : they will be grouped for the analysis.
            [:ref:`FORMAT <factorList>`]

    .. group-tab:: Request Files

        -c, --CTD_file FILENAME
            Tab-separated file from CTD request. [:ref:`FORMAT <CTDFile>`]

    .. group-tab:: Custom Files

        -g, --geneList FILENAME
            List of genes of interest. One gene per line. [:ref:`FORMAT <genesList>`]

--configPath PATH
    MultiXrank needs a configuration file as input. It could be short (file names) or very details (i.e with input
    parameters). The file contains at least paths of networks, bipartite and seed files.

    | For more details : [:ref:`FORMAT <configFile>`] - :octicon:`mark-github;1em` `GitHub <https://github.com/anthbapt/multixrank>`_ - :octicon:`book;1em` `ReadTheDocs <https://multixrank-doc.readthedocs.io/en/latest/>`_

--networksPath PATH
    Repository path where networks are saved.

--seedsFile FILENAME
    Path name of the seed file. This file contains the list of genes (i.e. target genes). They will be used as seed
    on the Random Walk analysis. [:ref:`FORMAT <simpleFile>`]

--sifFileName FILENAME
    Output file name to save the result into a SIF file.

Optionals arguments
--------------------

--directAssociation BOOLEAN
    | If ``TRUE``, only the genes targeted by the factors are extracted.
    | If ``FALSE``, the genes targeted by the factors and all the descendant molecules are extracted.
    | ``[default: True]``

--nbPub INTEGER
    In CTD, an interaction between a gene and a molecule can have references.
    You can set a threshold on the number of publications needed to extract the interaction.
    ``[default: 2]``

--top INTEGER
    Top nodes that will be saved into the output network (into SIF file).

-o, --outputPath PATH
    Name of the folder where to save the results.
    ``[default: OutputResults]``


Command line examples
------------------------

.. tabs::

    .. group-tab:: Request

        .. code-block:: bash

            python3 main.py multixrank  --factorList examples/InputData/InputFile_factorsList.csv \
                                        --directAssociation False \
                                        --nbPub 2 \
                                        --configPath examples/InputData/config_minimal_example1.yml \
                                        --networksPath examples/InputData/ \
                                        --seedsFile examples/InputData/seeds.txt \
                                        --sifFileName example1_resultsNetwork.sif \
                                        --top 10 \
                                        --outputPath examples/OutputResults_example1/

    .. group-tab:: Request Files

        .. code-block:: bash

            python3 main.py multixrank  --CTD_file examples/InputData/CTD_request_D014801_2022_08_24.tsv \
                                        --nbPub 2 \
                                        --configPath examples/InputData/config_minimal_example2.yml \
                                        --networksPath examples/InputData/ \
                                        --seedsFile examples/InputData/seeds.txt \
                                        --sifFileName example2_resultsNetwork.sif \
                                        --top 10 \
                                        --outputPath examples/OutputResults_example2/

    .. group-tab:: Custom Files

        .. code-block:: bash

            python3 main.py multixrank  --geneList examples/InputData/InputFromPaper/VitA-CTD-Genes.txt \
                                        --configPath examples/InputData/config_minimal_example3.yml \
                                        --networksPath examples/InputData/ \
                                        --seedsFile examples/InputData/seeds.txt \
                                        --sifFileName example3_resultsNetwork.sif \
                                        --top 10 \
                                        --outputPath examples/OutputResults_example3/

Networks available
--------------------

.. note::

    We use the biological multilayer network from multiXrank's paper [1]_.

We propose to run two walks through two different network compositions :

- molecular multilayer with three layers + disconnected disease network (:numref:`RWRFig` - left part)
- molecular multilayer with three layers + disease-disease network associated by their shared phenotype (:numref:`RWRFig` - right part)

.. _RWRFig:
.. figure:: ../../pictures/RWR_method.png
    :alt: RWR networks
    :align: center

    : Random Walk into two different networks conformations

Molecular multilayer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Details of layers (number of nodes, edges, nature of association and source).

Disconnected disease network
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can build this network with your pathways of interest - see :ref:`newNet`

Disease-disease network
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Explanation of how I did when I would have done it.

.. tip::

    | You can use any multilayer and networks that you want.
    | :octicon:`alert;1em` Be careful with the configuration file and the gene IDs used


References
------------

.. [1] Baptista, A., Gonzalez, A., & Baudot, A. (2022). Universal multilayer network exploration by random walk with restart. Communications Physics, 5(1), 1-9.