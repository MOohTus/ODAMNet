.. _newNet:

==================================================
Network creation
==================================================

Principle
------------

| Create automatically a disconnected diseases network using rare disease pathways from WikiPathways.
| A SIF (Simple interaction file) with three columns is created : source node, interaction type and target node.
| It's a tab-separated file.

Display a picture to explain how it's work (bipartite for the link and the disconnected network).

Required options
--------------------

.. tabs::

    .. group-tab:: Request

        --networksPath PATH
            The output repository name where the network disease (disconnected) is saved. The network disease is created using
            the data from WikiPathway.

        --bipartitePath PATH
            The output repository name where the bipartite gene-disease is saved. The bipartite is created using the data from
            WikiPathway.

    .. group-tab:: GMT file

        --networksPath PATH
            The output repository name where the network disease (disconnected) is saved. The network disease is created using
            the data from WikiPathway.

        --bipartitePath PATH
            The output repository name where the bipartite gene-disease is saved. The bipartite is created using the data from
            WikiPathway.

        --WP_GMT FILENAME
            Pathways file name that the user want to extract the genes to build the network

Optionals options
--------------------

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


Command line examples
------------------------

.. tabs::

    .. group-tab:: Request

        .. code-block:: bash

            python3 main.py networkCreation --networksPath examples/InputData/multiplex/2/ \
                                            --networksName WP_RareDiseasesNetwork_2022_08.sif \
                                            --bipartitePath examples/InputData/bipartite/ \
                                            --bipartiteName Bipartite_WP_RareDiseases_geneSymbols_2022_08.tsv \
                                            --outputPath examples/OutputResults_example1/

    .. group-tab:: GMT file

        .. code-block:: bash

            python3 main.py networkCreation --networksPath examples/InputData/multiplex/2/ \
                                            --networksName WP_RareDiseasesNetwork_2022_08_01.sif \
                                            --bipartitePath examples/InputData/bipartite/ \
                                            --bipartiteName Bipartite_WP_RareDiseases_geneSymbols_2022_08_01.tsv \
                                            --WP_GMT examples/InputData/WP_RareDiseases_request_2022_08_01.gmt \
                                            --outputPath examples/OutputResults_example2/