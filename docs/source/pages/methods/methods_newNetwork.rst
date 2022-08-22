==================================================
Network creation
==================================================

Principle
============

Parameters
============

To create a network diseases (disconnected one) from WikiPathway Rare Disease pathways.
Create a SIF (Simple interaction file) with three columns : source node, interaction type and target node.
It's a tab-separated file.

Up to date analysis - WP disease network :
==============================================

Required options :
^^^^^^^^^^^^^^^^^^^

--networksPath PATH
    The output repository name where the network disease (disconnected) is saved. The network disease is created using
    the data from WikiPathway.

--bipartitePath PATH
    The output repository name where the bipartite gene-disease is saved. The bipartite is created using the data from
    WikiPathway.

Optionals options :
^^^^^^^^^^^^^^^^^^^

--networksName FILENAME
    The user can give a name to the network disease. It's a SIF file. It's a disconnected network, so to allow the
    analysis using RWR, each disease is link to itself.
    [default: WP_RareDiseasesNetwork.sif]

--bipartiteName FILENAME
    The user can give a name to the bipartite. It's a tab-separated file.
    [default: Bipartite_WP_RareDiseases_geneSymbols.tsv]

-o, --outputPath PATH
    Name of the folder where save complementary results (i.e. request results)
    [default: OutputResults]

Command line :
^^^^^^^^^^^^^^^^^^^

.. tabs::

    .. group-tab:: short

        .. code-block:: bash

            python3 main.py networkCreation --networksPath examples/InputData/multiplex/2/ \
                                            --bipartitePath examples/InputData/bipartite/

    .. group-tab:: detailed

        .. code-block:: bash

            python3 main.py networkCreation --networksPath examples/InputData/multiplex/2/ \
                                            --networksName WP_RareDiseasesNetwork_2022_08.sif \
                                            --bipartitePath examples/InputData/bipartite/ \
                                            --bipartiteName Bipartite_WP_RareDiseases_geneSymbols_2022_08.tsv \
                                            --outputPath examples/OutputResults_example1/


Specific version - WP disease network :
=========================================

Required options :
^^^^^^^^^^^^^^^^^^^

--networksPath PATH
    The output repository name where the network disease (disconnected) is saved. The network disease is created using
    the data from WikiPathway.

--bipartitePath PATH
    The output repository name where the bipartite gene-disease is saved. The bipartite is created using the data from
    WikiPathway.

--WP_GMT FILENAME
    Pathways file name that the user want to extract the genes to build the network

Optionals options :
^^^^^^^^^^^^^^^^^^^

--networksName FILENAME
    The user can give a name to the network disease. It's a SIF file. It's a disconnected network, so to allow the
    analysis using RWR, each disease is link to itself.
    [default: WP_RareDiseasesNetwork.sif]

--bipartiteName FILENAME
    The user can give a name to the bipartite. It's a tab-separated file.
    [default: Bipartite_WP_RareDiseases_geneSymbols.tsv]

.. tabs::

    .. group-tab:: short

        .. code-block:: bash

            python3 main.py networkCreation --networksPath examples/InputData/multiplex/2/ \
                                            --bipartitePath examples/InputData/bipartite/ \
                                            --WP_GMT InputData/WP_allPathways_request_2022_08_01.gmt

    .. group-tab:: detailed

        .. code-block:: bash

            python3 main.py networkCreation --networksPath examples/InputData/multiplex/2/ \
                                            --networksName WP_RareDiseasesNetwork_2022_08_01.sif \
                                            --bipartitePath examples/InputData/bipartite/ \
                                            --bipartiteName Bipartite_WP_RareDiseases_geneSymbols_2022_08_01.tsv \
                                            --WP_GMT examples/InputData/WP_RareDiseases_request_2022_08_01.gmt \
                                            --outputPath examples/OutputResults_example2/

Global analysis - Data as you want :
======================================

Required options :
^^^^^^^^^^^^^^^^^^^

--networksPath PATH
    The output repository name where the network disease (disconnected) is saved. The network disease is created using
    the data from WikiPathway.

--bipartitePath PATH
    The output repository name where the bipartite gene-disease is saved. The bipartite is created using the data from
    WikiPathway.

--WP_GMT FILENAME
    Pathways file name that the user want to extract the genes to build the network

Optionals options :
^^^^^^^^^^^^^^^^^^^

--networksName FILENAME
    The user can give a name to the network disease. It's a SIF file. It's a disconnected network, so to allow the
    analysis using RWR, each disease is link to itself.
    [default: WP_RareDiseasesNetwork.sif]

--bipartiteName FILENAME
    The user can give a name to the bipartite. It's a tab-separated file.
    [default: Bipartite_WP_RareDiseases_geneSymbols.tsv]

.. tabs::

    .. group-tab:: detailed

        .. code-block:: bash

            python3 main.py networkCreation --networksPath examples/InputData/multiplex/2/ \
                                            --networksName WP_RareDiseasesNetwork_fromVitaminPaper.sif \
                                            --bipartitePath examples/InputData/bipartite/ \
                                            --bipartiteName Bipartite_WP_RareDiseases_geneSymbols_fromVitaminPaper.tsv \
                                            --WP_GMT examples/InputData/InputFromPaper/PathwaysOfInterest.gmt \
                                            --outputPath examples/OutputResults_example3/