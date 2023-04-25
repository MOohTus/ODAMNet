.. _netCreation:

_pathwaysOfInterestNet:

================================
Networks creation
================================

Principle
===========

The ``networkCreation`` function available in ODAMNet creates two files: a disconnected **network** (with self loop) and
a **bipartite network**.

Input parameters for network creation
========================================

By default, the ``networkCreation`` creates a rare disease pathways network (data are retrieved from WikiPathways [1]_
automatically). The created network is disconnected and contains only self loop (i.e. rare disease pathways link to
themself). The bipartite network connects genes nodes to rare disease pathway nodes.

You can also provided your own pathways/processes of interest using ``--GMT`` parameter.

--networksPath PATH
    Output repository name where the pathways/processes network will be saved **[requiered]**

--networksName FILENAME
    File name to save the pathways/processes network. The created file will be in SIF file format.
    ``[default: WP_RareDiseasesNetwork.sif]``

--bipartitePath PATH
    Output repository name where the bipartite genes-pathways/processes is saved **[requiered]**

--bipartiteName FILENAME
    File name to save the bipartite. It's a tab-separated file.
    ``[default: Bipartite_WP_RareDiseases_geneSymbols.tsv]``

-o, --outputPath PATH
    Name of the folder to save complementary results (i.e. request results)
    ``[default: OutputResults]``

Use-case command lines
========================

.. tabs::

    .. group-tab:: Data retrieved by requests

        .. code-block:: bash

            odamnet networkCreation --networksPath useCases/InputData/multiplex/2/ \
                                    --networksName WP_RareDiseasesNetwork_fromRequest.sif \
                                    --bipartitePath useCases/InputData/bipartite/ \
                                    --bipartiteName Bipartite_WP_RareDiseases_geneSymbols_fromRequest.tsv \
                                    --outputPath useCases/OutputResults_useCase1

    .. group-tab:: Data provided by users

        .. code-block:: bash

            odamnet networkCreation --networksPath useCases/InputData/multiplex/2/ \
                                    --networksName pathwaysOfInterestNetwork_fromPaper.sif \
                                    --bipartitePath useCases/InputData/bipartite/ \
                                    --bipartiteName Bipartite_pathOfInterest_geneSymbols_fromPaper.tsv \
                                    --GMT useCases/InputData/PathwaysOfInterest.gmt \
                                    --outputPath useCases/OutputResults_useCase2

References
============

.. [1] Martens, M., Ammar, A., Riutta, A., Waagmeester, A., Slenter, D. N., Hanspers, K., ... & Kutmon, M. (2021). WikiPathways: connecting communities. Nucleic acids research, 49(D1), D613-D621.