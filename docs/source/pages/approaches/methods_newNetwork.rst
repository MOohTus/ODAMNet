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
-----------------------

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






Target genes %A% il faudra qu'on fasse un point sémantique: target genes, gene data, factor, environmental factor ... Pour être le plus génériques possibles
-----------------------------------------------------------------------------------------------------------------------------------------------------------------

Gene data information may come from three different source :

.. tabs::

    .. group-tab:: CTD request

        .. warning::

            The CTD database is updated every month (`updates page <https://ctdbase.org/about/changes/>`_).
            For reproducibility, one might want to produce its own data version.

        Give a list of **environmental factors**. CTD is requested and returns a list of target genes associated with the input list of environmental factors. %A% je suis pas sure du mot "environmental" en fait, je sais pas si on peut dire par exemple qu'un médicament c'est un facteur environmental, ou alors en tous cas je suis pas sure que tout le monde considère ca du même point de vue.

    .. group-tab:: CTD file

        Give a **tsv file** with the data from **CTD** database. The gene list will be extracted from this file.

    .. group-tab:: Genes file

        Give a **list of genes** directly.

For more details about the :ref:`query` format.

Pathways
---------

Pathways can be extracted from two different sources :

.. tabs::

    .. group-tab:: WP request

        .. warning::

            WP is updated regularly (`updates page <https://www.wikipathways.org/index.php/WikiPathways:Updates>`_).
            It could be interesting to provide its own version of data for reproducibility.

        By default, **Rare Disease pathways** are extracted from **WikiPathways** [4]_. The corresponding background genes are
        extracted in the same time (all human genes in WP). The background genes is necessary to calculate statistics.

    .. group-tab:: GMT file

        Give a **GMT file** with pathways. It could be

            - rare diseases pathways from WP for a specific version
            - a custom GMT file with **pathways of interest**. Pathways can come from different sources.
              Corresponding backgrounds genes are needed.

For more details about the :ref:`pathways` format.

Examples %A% Use-cases?
------------------------------

We performed an analysis to study the relationships between vitamin A and Rare Diseases. We illustrate the different
possibilities of data extraction from different sources through three examples :

    - :ref:`example1`
    - :ref:`example2`
    - :ref:`example3`

.. tip::

    You can mix input types. For instance, you can request CTD and give a custom GMT file of pathways of interest.
    **Every combination is possible!**



Use case 1 : automatic request of CTD and WikiPathways
---------------------------------------------------------

By default, CTD and WikiPathways are automatically requested. You have to provide in input a list of chemicals.
A list of genes that are targeted by these chemicals are extracted. An overlap analysis is performed between these
target genes and the Rare Diseases pathways.

Required input files
^^^^^^^^^^^^^^^^^^^^^^

--chemicalsFile FILENAME
    Contains a list of chemicals. They have to be in **MeSH** identifiers (e.g. D014801).
    You can give several chemicals in the same line : they will be grouped for the analysis.
    [:ref:`FORMAT <chemicalsFile>`]

Optional input files
^^^^^^^^^^^^^^^^^^^^^

--directAssociation BOOLEAN
    | If ``TRUE``, only the genes targeted by the factors are extracted.
    | If ``FALSE``, the genes targeted by the factors and all the descendant molecules are extracted.
    | ``[default: True]``

--nbPub INTEGER
    In CTD, an interaction between a gene and a molecule can have references.
    You can set a threshold on the number of publications needed to extract the interaction.
    ``[default: 2]``

-o, --outputPath PATH
    Name of the folder where to save the results.
    ``[default: OutputResults]``

.. tip::

    For reproducibility, you can provided your version of the CTD and WikiPathways data. You can provide the CTD file
    using the ``--CTD_file`` parameter and WikiPathways files using the ``--GMT`` and ``--backgroundFile`` parameters.

    -c, --CTD_file FILENAME
            Tab-separated file from CTD request. [:ref:`FORMAT <CTDFile>`]

    --GMT FILENAME
            Tab-delimited file that describes gene sets of Rare Disease pathways (from WP).
            [:ref:`FORMAT <pathways>`]

    --backgroundFile FILENAME
            List of the different background source file name. Each background genes source is a GMT file.
            It should be in the same order than the GMT file. Here, the background GMT file contains
            all Rare Disease pathways.
            [:ref:`FORMAT <pathways>`]


Use case 2 : input files provided by the user
----------------------------------------------

You can provide your own target genes file (``--targetGenesFile``) and GMT file (``--GMT``) with your pathways/processes
of interest.

Required input files
^^^^^^^^^^^^^^^^^^^^^^

-g, --targetGenesFile FILENAME
    List of genes of interest. One gene per line. [:ref:`FORMAT <genesList>`]

--GMT FILENAME
    Tab-delimited file that describes gene sets of pathways of interest.
    Pathways can come from several sources (e.g. WP and GO\:BP).
    [:ref:`FORMAT <pathways>`]

--backgroundFile FILENAME
    List of the different background source file name. Each background genes source is a GMT file.
    It should be in the same order than the GMT file.
    [:ref:`FORMAT <pathways>`]

Optional input files
^^^^^^^^^^^^^^^^^^^^^

-o, --outputPath PATH
    Name of the folder where to save the results.
    ``[default: OutputResults]``


Use cases command line
------------------------

.. tabs::

    .. group-tab:: Automatic requests

        .. code-block:: bash

            python3 main.py overlap --factorList examples/InputData/InputFile_factorsList.csv \
                                    --directAssociation FALSE \
                                    --nbPub 2 \
                                    --outputPath examples/OutputResults_useCase1/

    .. group-tab:: User files

        .. code-block:: bash

            python3 main.py overlap --geneList examples/InputData/InputFromPaper/VitA-CTD-Genes.txt \
                                    --WP_GMT examples/InputData/InputFromPaper/PathwaysOfInterest.gmt \
                                    --backgroundFile examples/InputData/InputFromPaper/PathwaysOfInterestBackground.txt \
                                    --outputPath examples/OutputResults_useCase2/






Required input data files
----------------------------

By default, CTD and WikiPathways are **automatically requested**. You have to provide in input a **list of chemicals**.
From these chemicals, a list of target genes is extracted. An overlap analysis is performed between these target genes
and the Rare Diseases pathways.

.. tip::

    For reproducibility, you can provided your version of the CTD and WikiPathways data. You can provide the CTD file
    using the ``--CTD_file`` parameter and WikiPathways files using the ``--GMT`` and ``--backgroundFile`` parameters.

    -c, --CTD_file FILENAME
            Tab-separated file from CTD request. [:ref:`FORMAT <CTDFile>`]

    --GMT FILENAME
            Tab-delimited file that describes gene sets of Rare Disease pathways (from WP).
            [:ref:`FORMAT <pathways>`]

    --backgroundFile FILENAME
            List of the different background source file name. Each background genes source is a GMT file.
            It should be in the same order than the GMT file. Here, the background GMT file contains
            all Rare Disease pathways.
            [:ref:`FORMAT <pathways>`]

You can provide your own target genes file (``--targetGenesFile``) and GMT file (``--GMT``) with your pathways/processes
of interest.

.. tabs::

    .. group-tab:: Automatic requests

        --chemicalsFile FILENAME
            Contains a list of chemicals. They have to be in **MeSH** identifiers (e.g. D014801).
            You can give several chemicals in the same line : they will be grouped for the analysis.
            [:ref:`FORMAT <chemicalsFile>`]

    .. group-tab:: User files

        -g, --targetGenesFile FILENAME
            List of genes of interest. One gene per line. [:ref:`FORMAT <genesList>`]

        --GMT FILENAME
            Tab-delimited file that describes gene sets of pathways of interest.
            Pathways can come from several sources (e.g. WP and GO\:BP).
            [:ref:`FORMAT <pathways>`]

        --backgroundFile FILENAME
            List of the different background source file name. Each background genes source is a GMT file.
            It should be in the same order than the GMT file.
            [:ref:`FORMAT <pathways>`]

Optional arguments
--------------------

--directAssociation BOOLEAN
    | If ``TRUE``, only the genes targeted by the factors are extracted.
    | If ``FALSE``, the genes targeted by the factors and all the descendant molecules are extracted.
    | ``[default: True]``

--nbPub INTEGER
    In CTD, an interaction between a gene and a molecule can have references.
    You can set a threshold on the number of publications needed to extract the interaction.
    ``[default: 2]``

-o, --outputPath PATH
    Name of the folder where to save the results.
    ``[default: OutputResults]``

Use cases command line
------------------------

.. tabs::

    .. group-tab:: Automatic requests

        .. code-block:: bash

            python3 main.py overlap --factorList examples/InputData/InputFile_factorsList.csv \
                                    --directAssociation FALSE \
                                    --nbPub 2 \
                                    --outputPath examples/OutputResults_useCase1/

    .. group-tab:: User files

        .. code-block:: bash

            python3 main.py overlap --geneList examples/InputData/InputFromPaper/VitA-CTD-Genes.txt \
                                    --WP_GMT examples/InputData/InputFromPaper/PathwaysOfInterest.gmt \
                                    --backgroundFile examples/InputData/InputFromPaper/PathwaysOfInterestBackground.txt \
                                    --outputPath examples/OutputResults_useCase2/



.. [4] Martens, M., Ammar, A., Riutta, A., Waagmeester, A., Slenter, D. N., Hanspers, K., ... & Kutmon, M. (2021). WikiPathways: connecting communities. Nucleic acids research, 49(D1), D613-D621.
