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

*For more details, see the paper* [1]_

Usage
-------

By default, data are extracted directly by request databases (:numref:`RWRUsageFig`: *data extracted from requests*).
You give the ``--chemicalsFile`` and the **target genes** are extracted from **CTD**.

You can provide your own **target genes file** (:numref:`RWRUsageFig`: *data extracted from users*) with ``--targetGenesFile``.

.. _RWRUsageFig:
.. figure:: ../../pictures/multixrank_graph.png
    :alt: RWR analysis
    :align: center

    : Input and output files of Random Walk with Restart analysis

    There is two ways to extract target genes : from request (pink boxes) or provided by the user (green boxes).
    Required files/parameters have solid border line and optional files/parameters have dash border line.
    Output files in pink are created only if the input data are extracted from requests.

Input parameters for RWR analysis
----------------------------------------

To extract target genes from **CTD**, see parameters on the ``Data extracted from requests`` tab.
To provide **your own** target genes, see parameters on the ``Data extracted from user`` tab.

.. tabs::

    .. group-tab:: Data extracted from requests

        -c, --chemicalsFile FILENAME
            Contains a list of chemicals. They have to be in **MeSH** identifiers (e.g. D014801).
            You can give several chemicals in the same line : they will be grouped for the analysis.
            [:ref:`FORMAT <chemicalsFile>`] **[required]**

        --directAssociation BOOLEAN
            | ``TRUE`` : extract chemicals data, which are in the chemicalsFile, from CTD
            | ``FALSE``: extract chemicals and their child molecules data from CTD
            | ``[default: True]``

        --nbPub INTEGER
            References can be associated with chemical interactions.
            You can define a threshold to filter target genes extraction based on the number of publications.
            ``[default: 2]``

    .. group-tab:: Data extracted from user

        -t, --targetGenesFile FILENAME
            Contains a list of target genes. One gene per line. [:ref:`FORMAT <genesList>`]
            **[required]**

--configPath PATH
    MultiXrank needs a configuration file. It could be short (only file names) or very details (file names + parameters).
    The file contains at least paths of networks, bipartite and seed files. **[required]**

    | For more details : [:ref:`FORMAT <configFile>`] - :octicon:`mark-github;1em` `GitHub <https://github.com/anthbapt/multixrank>`_ :octicon:`book;1em` `ReadTheDocs <https://multixrank-doc.readthedocs.io/en/latest/>`_

--networksPath PATH
    Repository path where networks are saved. **[required]**

--seedsFile FILENAME
    Path name file to store seed list. This file contains the list of genes (i.e. target genes). They will be used as seed
    on the Random Walk analysis. [:ref:`FORMAT <simpleFile>`] **[required]**

--sifFileName FILENAME
    Output file name to save the result into a SIF file. **[required]**

--top INTEGER
    Top nodes that will be saved into the output network (into SIF file).

-o, --outputPath PATH
    Name of the folder where to save the results.
    ``[default: OutputResults]``

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

This kind of network can be build using the ``networkCreation`` method.

By default, the network is build using Rare Diseases pathways extracted automatically from WP.

--networksPath PATH
    Output repository name where the network disease will be saved.

--bipartitePath PATH
    Output repository name where the bipartite gene-disease will be saved.

--networksName FILENAME
    You can give a name to the network disease. It's a SIF file but each disease/pathway is link to itself.
    ``[default: WP_RareDiseasesNetwork.sif]``

--bipartiteName FILENAME
    You can give a name to the bipartite. It's a tab-separated file.
    ``[default: Bipartite_WP_RareDiseases_geneSymbols.tsv]``

-o, --outputPath PATH
    Name of the folder where to save complementary results (i.e. request results)
    ``[default: OutputResults]``

Moreover, you can provide your own pathways/processes of interest file using ``--GMT`` parameter.

This kind of network can be build from Rare Diseases pathways (WP) or from your own pathways/processes of interest
with ``networkCreation`` method.

.. tabs::

    .. group-tab:: Data extracted from requests

        .. code-block:: bash

            python3 main.py

    .. group-tab:: Data extracted from user

        .. code-block:: bash

            python3 main.py

Disease-disease network
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Explanation of how I did when I would have done it.

.. tip::

    | You can use any multilayer and networks that you want.
    | :octicon:`alert;1em` Be careful with the configuration file and the gene IDs used


Use-cases command line
------------------------

.. tabs::

    .. group-tab:: Data extracted from requests

        .. code-block:: bash

            python3 main.py multixrank  --chemicalsFile useCases/InputData/chemicalsFile.csv \
                                        --directAssociation FALSE \
                                        --nbPub 2 \
                                        --configPath useCases/InputData/config_minimal_useCase1.yml \
                                        --networksPath useCases/InputData/ \
                                        --seedsFile useCases/InputData/seeds.txt \
                                        --sifFileName resultsNetwork_useCase1.sif \
                                        --top 10 \
                                        --outputPath useCases/OutputResults_useCase1/

    .. group-tab:: Data extracted from user

        .. code-block:: bash

            python3 main.py multixrank  --targetGenesFile useCases/InputData/VitA-Balmer2002-Genes.txt \
                                        --configPath useCases/InputData/config_minimal_useCase2.yml \
                                        --networksPath useCases/InputData/ \
                                        --seedsFile useCases/InputData/seeds.txt \
                                        --sifFileName resultsNetwork_useCase2.sif \
                                        --top 10 --outputPath \
                                        --outputPath useCases/OutputResults_useCase2/

References
------------

.. [1] Baptista, A., Gonzalez, A., & Baudot, A. (2022). Universal multilayer network exploration by random walk with restart. Communications Physics, 5(1), 1-9.