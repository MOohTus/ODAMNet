================================
Network creation
================================

Principle
===========

The ``networkCreation`` function available in ODAMNet creates two files: a disconnected **network** (with self loop) and
a **bipartite network**.

Input parameters for network creation
========================================

By default, the ``networkCreation`` creates a rare disease pathways network (data are retrieved from WikiPathways [1]_
automatically). The created network is disconnected and contains only self loop (i.e. rare disease pathways linked to
themself). The bipartite network connects genes nodes to rare disease pathway nodes.

You can also provided your own pathways/processes of interest using ``--GMT`` parameter.

--networksPath PATH
    Output folder name where the pathways/processes network is saved **[requiered]**

--networksName FILENAME
    File name to save the pathways/processes network. The created network is in :ref:`GR format <GR>`.
    ``[default: WP_RareDiseasesNetwork.gr]``

--bipartitePath PATH
    Output folder name where the bipartite genes-pathways/processes is saved **[requiered]**

--bipartiteName FILENAME
    File name to save the bipartite network. The created network is in :ref:`GR format <GR>`.
    ``[default: Bipartite_WP_RareDiseases_geneSymbols.gr]``

--GMT FILENAME
    Tab-delimited file that describes gene sets of pathways/processes of interest.
    Pathways/processes can come from several sources *(e.g. WP and GO\:BP)*.
    [:ref:`FORMAT <GMTFile>`]

-o, --outputPath PATH
    Name of the folder to save complementary results (i.e. query results)
    ``[default: OutputResults]``

Use-case command lines
========================

.. tabs::

    .. group-tab:: Data retrieved by queries

        .. code-block:: bash

            odamnet networkCreation --networksPath useCases/InputData/multiplex/2/ \
                                    --networksName RareDiseasePathways_network_useCase1.gr \
                                    --bipartitePath useCases/InputData/bipartite/ \
                                    --bipartiteName Bipartite_RareDiseasePathways_geneSymbols_useCase1.gr \
                                    --outputPath useCases/OutputResults_useCase1

    .. group-tab:: Data provided by user

        .. code-block:: bash

            odamnet networkCreation --networksPath useCases/InputData/multiplex/2/ \
                                    --networksName PathwaysOfInterest_network_useCase2.gr \
                                    --bipartitePath useCases/InputData/bipartite/ \
                                    --bipartiteName Bipartite_pathOfInterest_geneSymbols_useCase2.gr \
                                    --GMT useCases/InputData/PathwaysOfInterest.gmt \
                                    --outputPath useCases/OutputResults_useCase2

References
============

.. [1] Martens M, Ammar A, Riutta A *et al.*. WikiPathways: connecting communities. Nucleic acids research. 2021.