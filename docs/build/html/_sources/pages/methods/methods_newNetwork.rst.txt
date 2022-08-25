.. _newNet:

==================================================
Network creation
==================================================

Principle
------------

| Create automatically a disconnected diseases network using your pathways of interest.
| A SIF (Simple interaction file) with three columns is created [:ref:`FORMAT <net>`]

Display a picture to explain how it's work (bipartite for the link and the disconnected network).

Required arguments
--------------------

.. tabs::

    .. group-tab:: Request

        .. note::

            Network and its bipartite are creating using Rare Disease pathways request from WikiPathways.

        --networksPath PATH
            Output repository name where the network disease will be saved.

        --bipartitePath PATH
            Output repository name where the bipartite gene-disease will be saved.

    .. group-tab:: GMT file

        .. note::

            Network and its bipartite are creating using pathways from your GMT file given as an input.

        --networksPath PATH
            Output repository name where the network disease will be saved.

        --bipartitePath PATH
            Output repository name where the bipartite gene-disease will be saved.

        --GMT FILENAME
            GMT file name that contains composition of pathways of interest.

Optionals arguments
--------------------

--networksName FILENAME
    You can give a name to the network disease. It's a SIF file but each disease/pathway is link to itself.
    ``[default: WP_RareDiseasesNetwork.sif]``

--bipartiteName FILENAME
    You can give a name to the bipartite. It's a tab-separated file.
    ``[default: Bipartite_WP_RareDiseases_geneSymbols.tsv]``

-o, --outputPath PATH
    Name of the folder where to save complementary results (i.e. request results)
    ``[default: OutputResults]``

Command line examples
------------------------

.. tabs::

    .. group-tab:: Request

        .. code-block:: bash

            python3 main.py networkCreation --networksPath examples/InputData/multiplex/2/ \
                                            --networksName WP_RareDiseasesNetwork_fromRequest.sif \
                                            --bipartitePath examples/InputData/bipartite/ \
                                            --bipartiteName Bipartite_WP_RareDiseases_geneSymbols_fromRequest.tsv \
                                            --outputPath examples/OutputResults_example1/

    .. group-tab:: GMT file

        .. code-block:: bash

            python3 main.py networkCreation --networksPath examples/InputData/multiplex/2/ \
                                            --networksName WP_RareDiseasesNetwork_fromFile.sif \
                                            --bipartitePath examples/InputData/bipartite/ \
                                            --bipartiteName Bipartite_WP_RareDiseases_geneSymbols_fromFile.tsv \
                                            --GMT examples/InputData/WP_RareDiseases_request_2022_08_24.gmt \
                                            --outputPath examples/OutputResults_example2/
