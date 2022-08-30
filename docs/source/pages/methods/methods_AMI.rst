.. _AMI:

==================================================
Active Module Identification
==================================================

Principle
------------

.. note::

    | We are using DOMINO [1]_ for Active Module identification and running the analysis on their server [2]_
    | :octicon:`mark-github;1em` `GitHub <https://github.com/Shamir-Lab/domino_web>`_ :octicon:`globe;1em` `website <http://domino.cs.tau.ac.il/>`_


Target genes are defined as ``Active Genes``. DOMINO is looking for **active modules** in a network
(e.g. Protein-Protein Interaction (PPI) network) (:numref:`overviewFig` - middle part).

Active modules (AM) are composed of active genes and other associated genes and would ideally represent distinct functional modules.

We finally perform an **overlap analysis** between each AM and the pathways of interest. This approach is a kind of
**network extension** analysis, **indirect associations** with diseases are search.

The :numref:`dominoFig` is an overview of the DOMINO algorithm :

| **A -** The network is clustered into disjoint and highly connected subnetworks (slices) with the Louvain algorithm, based on modularity optimization.
| **B -** The relevant slices (where active genes are over-represented) are detected using the Hypergeometric test. Pvalue are corrected with the FDR method.
| **C -** The most active sub-slice is identified on each relevant slices.
| **D -** The sub-slices are split into putative Active Modules (AM) using the Newmann-Girvan modularity algorithm.
| **E -** The final set of AM is identified (under a threshold)

.. _dominoFig:
.. figure:: ../../pictures/DOMINO_method.jpg
    :alt: DOMINO method
    :align: center

    : Schematic illustration of DOMINO (Fig3 from DOMINO's paper [1]_)

*For more details, see to the paper DOMINO publication* [1]_

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

        --GMT FILENAME
            Tab-delimited file that describes gene sets of Rare Disease pathways (from WP).
            [:ref:`FORMAT <pathways>`]

        --backgroundFile FILENAME
            List of the different background source file name. Each background genes source is a GMT file.
            It should be in the same order than the GMT file. Here, the background GMT file contains
            all Rare Disease pathways.
            [:ref:`FORMAT <pathways>`]

    .. group-tab:: Custom Files

        -g, --geneList FILENAME
            List of genes of interest. One gene per line. [:ref:`FORMAT <genesList>`]

        --GMT FILENAME
            Tab-delimited file that describes gene sets of pathways of interest.
            Pathways can come from several sources (e.g. WP and GO\:BP).
            [:ref:`FORMAT <pathways>`]

        --backgroundFile FILENAME
            List of the different background source file name. Each background genes source is a GMT file.
            It should be in the same order than the GMT file.
            [:ref:`FORMAT <pathways>`]

-n, --networkFile FILENAME
    Network file name (e.g. PPI network) in SIF format (tab-delimited).
    The file contains 3 columns with the source node, the interaction type and the target node.
    [:ref:`FORMAT <net>`]

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

--netUUID TEXT
    You can use a network extracted automatically from `NDEx <https://www.ndexbio.org/#/>`_ [3]_. You have to provide
    the UUID of the network (e.g. ``079f4c66-3b77-11ec-b3be-0ac135e8bacf``).

-o, --outputPath PATH
    Name of the folder where to save the results.
    ``[default: OutputResults]``

Command line examples
------------------------

.. tabs::

    .. group-tab:: Request

        .. code-block:: bash

            python3 main.py domino  --factorList examples/InputData/InputFile_factorsList.csv \
                                    --directAssociation FALSE \
                                    --nbPub 2 \
                                    --networkFile examples/InputData/PPI_network_2016.sif \
                                    --outputPath examples/OutputResults_example1/

    .. group-tab:: Request Files

        .. code-block:: bash

            python3 main.py domino  --CTD_file examples/InputData/CTD_request_D014801_2022_08_24.tsv \
                                    --nbPub 2 \
                                    --WP_GMT examples/InputData/WP_RareDiseases_request_2022_08_24.gmt \
                                    --backgroundFile examples/InputData/backgroundsFiles.tsv \
                                    --networkFile examples/InputData/PPI_network_2016.sif \
                                    --outputPath examples/OutputResults_example2/

    .. group-tab:: Custom Files

        .. code-block:: bash

            python3 main.py domino  --geneList examples/InputData/InputFromPaper/VitA-CTD-Genes.txt \
                                    --WP_GMT examples/InputData/InputFromPaper/PathwaysOfInterest.gmt \
                                    --backgroundFile examples/InputData/InputFromPaper/PathwaysOfInterestBackground.txt \
                                    --networkFile examples/InputData/PPI_network_2016.sif \
                                    --outputPath examples/OutputResults_example3/

Available Interaction Networks
-----------------------------------

.. warning::

    Be careful when using networks from NDEx: gene IDs format are not always consistent between networks and data from
    CTD or other input gene lists and pathways.
    For instance, CTD returns gene symbols (i.e. HGNC). If CTD data are used, the network need to contains gene symbols
    and not ensembl IDs or any other gene name format. The rule applies on GMT files too.

Protein-Protein Interaction network
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We provide with the script a PPI network (from the Valdeolivas *et al.,* paper [4]_, November 2016). The gene name format is
**gene symbols**, you can give it to the script using the required argument ``-n, --networkFile``.

It contains 66 971 interactions (edges) and 12 621 genes (nodes). The following part gives you an overview of the file :

.. code-block::

    node_1	link	node_2
    AAMP	ppi	VPS52
    AAMP	ppi	BHLHE40
    AAMP	ppi	AEN
    AAMP	ppi	C8orf33
    AAMP	ppi	TK1


Personal network
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. caution::

    :octicon:`alert;2em;sd-text-info` gene IDs need to correspond with the target genes list and GMT files !!

You can use any network that you want or have. It has to be in :ref:`SIF format <net>` and you can give it to
the script using the required argument ``-n, --networkFile``.


Request NDEx database
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. caution::

    :octicon:`alert;2em;sd-text-info` gene IDs need to correspond with the target genes list and GMT files !!

You can directly request NDEx [3]_ `website <https://www.ndexbio.org/>`_ and extract the network that you want to use
(REST API [3]_:sup:`,` [5]_ :sup:`,` [6]_). You need to specify the network UUID using the optional argument
``--netUUID``. The network will be save into a :ref:`SIF file <net>`.


References
------------

.. [1] Levi, H., Elkon, R., & Shamir, R. (2021). DOMINO: a network‐based active module identification algorithm with reduced rate of false calls. Molecular systems biology, 17(1), e9593.
.. [2] Levi, H., Rahmanian, N., Elkon, R., & Shamir, R. (2022). The DOMINO web-server for active module identification analysis. Bioinformatics, 38(8), 2364-2366.
.. [3] Pratt et al. NDEx, the Network Data Exchange. Cell Systems, Vol. 1, Issue 4: 302-305 (2015).
.. [4] Valdeolivas, A., Tichit, L., Navarro, C., Perrin, S., Odelin, G., Levy, N., ... & Baudot, A. (2019). Random walk with restart on multiplex and heterogeneous biological networks. Bioinformatics, 35(3), 497-505.
.. [5] Pillich et al. NDEx: A Community Resource for Sharing and Publishing of Biological Networks. Methods Mol Biol, 1558: 271-301 (2017).
.. [6] Pratt et al. NDEx 2.0: A Clearinghouse for Research on Cancer Pathways. Cancer Res. Nov 1;77(21):e58-e61 (2017).
