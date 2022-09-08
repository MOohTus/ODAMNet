.. _AMI:

==================================================
Active Module Identification
==================================================

Principle
------------

.. note::

    | Active Modules (AM) identification is performed using DOMINO [1]_. The analysis is running on their server [2]_.
    | :octicon:`mark-github;1em` `DOMINO web GitHub <https://github.com/Shamir-Lab/domino_web>`_
    | :octicon:`globe;1em` `DOMINO server <http://domino.cs.tau.ac.il/>`_

DOMINO is looking for **Active Modules** (AM) in a network (e.g. Protein-Protein Interaction (PPI) network) (:numref:`overviewFig` - middle part).

First, target genes are defined as **Active Genes**. Then DOMINO tries to **identify active modules**.

Active modules are **subnetworks** identified as relevant and composed of active genes (i.e. target genes) and other associated genes.
Ideally, they will represent **distinct functional modules** and can reveal biological processes involved in a specific condition.

Finally, we performed an **overlap analysis** between each AM and pathways of interest.

DOMINO algorithm overview
----------------------------

The :numref:`dominoMethodFig` is an overview of the DOMINO algorithm :

.. _dominoMethodFig:
.. figure:: ../../pictures/DOMINO_method.jpg
    :alt: DOMINO method
    :align: center

    : Schematic illustration of DOMINO (Fig3 from DOMINO's paper [1]_)

| **A -** The network is clustered into disjoint and highly connected subnetworks (slices) with the Louvain algorithm, based on modularity optimization.
| **B -** The relevant slices (where active genes are over-represented) are detected using the Hypergeometric test. Pvalue are corrected with the FDR method.
| **C -** The most active sub-slice is identified on each relevant slices.
| **D -** The sub-slices are split into putative Active Modules (AM) using the Newmann-Girvan modularity algorithm.
| **E -** The final set of AM is identified (under a threshold of Bonferroni qval<=0.05)

*For more details, refer to the paper DOMINO publication* [1]_

Usage
-------

By default, data are extracted directly by request databases (:numref:`dominoUsageFig`: *data extracted from requests*).
You give the ``--chemicalsFile`` and the **target genes** are extracted from **CTD**. **Rare Disease pathways** are
extracted from **WP** automatically too. You can give some optional parameters to custom the selection of target genes.

You can provide your own **target genes file** and **pathways/processes of interest**
(:numref:`dominoUsageFig`: *data extracted from users*) with ``--targetGenesFile`` and ``--GMT``, ``--backgroundFile``.

.. _dominoUsageFig:
.. figure:: ../../pictures/DOMINO_graph.png
    :alt: domino analysis
    :align: center

    : Input and output files of Active Modules Identification

    There is two ways to extract target genes : from request (pink boxes) or provided by the user (green boxes).
    Required files/parameters have solid border line and optional files/parameters have dash border line.
    Output files in pink are created only if the input data are extracted from requests.

Input parameters for Active Modules Identification
----------------------------------------------------

To extract target genes from **CTD** and RD pathways from **WP**, see parameters on the ``Data extracted from requests`` tab.
To provide **your own** target genes and pathways/processes files, see parameters on the ``Data extracted from user`` tab.

The network file is required ``--networkFile`` whereas ``--netUUID`` and ``--outputPath`` are optional.

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

        --GMT FILENAME
            Tab-delimited file that describes gene sets of pathways/processes of interest.
            Pathways/processes can come from several sources (e.g. WP and GO\:BP).
            [:ref:`FORMAT <pathways>`]
            **[required]**

        --backgroundFile FILENAME
            List of the different background source file name. Each background genes source is a GMT file.
            It should be in the same order than the GMT file.
            [:ref:`FORMAT <pathways>`]
            **[required]**

-n, --networkFile FILENAME
    Network file name. It's SIF file [:ref:`FORMAT <SIF>`] **[required]**

--netUUID TEXT
    You can use a network extracted automatically from `NDEx <https://www.ndexbio.org/#/>`_ [3]_. You have to provide
    the UUID of the network (e.g. ``079f4c66-3b77-11ec-b3be-0ac135e8bacf``).

-o, --outputPath PATH
    Name of the folder where to save the results.
    ``[default: OutputResults]``


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
**gene symbols**, you can give it to the script using the required parameter ``-n, --networkFile``.

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
the script using the required parameter ``-n, --networkFile``.


Request NDEx database
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. caution::

    :octicon:`alert;2em;sd-text-info` gene IDs need to correspond with the target genes list and GMT files !!

You can directly request NDEx [3]_ `website <https://www.ndexbio.org/>`_ and extract the network that you want to use
(REST API [3]_:sup:`,` [5]_ :sup:`,` [6]_). You need to specify the network UUID using the optional parameter
``--netUUID``. The network will be save into a :ref:`SIF file <net>`.


Use-cases command line
------------------------

.. tabs::

    .. group-tab:: Data extracted from requests

        .. code-block:: bash

            python3 main.py domino  --chemicalsFile useCases/InputData/chemicalsFile.csv \
                                    --directAssociation FALSE \
                                    --nbPub 2 \
                                    --networkFile useCases/InputData/PPI_network_2016.sif \
                                    --outputPath useCases/OutputResults_useCase1/

    .. group-tab:: Data extracted from user

        .. code-block:: bash

            python3 main.py domino  --targetGenesFile useCases/InputData/VitA-Balmer2002-Genes.txt \
                                    --GMT useCases/InputData/PathwaysOfInterest.gmt \
                                    --backgroundFile useCases/InputData/PathwaysOfInterestBackground.txt \
                                    --networkFile useCases/InputData/PPI_network_2016.sif \
                                    --outputPath useCases/OutputResults_useCase2/

References
------------

.. [1] Levi, H., Elkon, R., & Shamir, R. (2021). DOMINO: a network‐based active module identification algorithm with reduced rate of false calls. Molecular systems biology, 17(1), e9593.
.. [2] Levi, H., Rahmanian, N., Elkon, R., & Shamir, R. (2022). The DOMINO web-server for active module identification analysis. Bioinformatics, 38(8), 2364-2366.
.. [3] Pratt et al. NDEx, the Network Data Exchange. Cell Systems, Vol. 1, Issue 4: 302-305 (2015).
.. [4] Valdeolivas, A., Tichit, L., Navarro, C., Perrin, S., Odelin, G., Levy, N., ... & Baudot, A. (2019). Random walk with restart on multiplex and heterogeneous biological networks. Bioinformatics, 35(3), 497-505.
.. [5] Pillich et al. NDEx: A Community Resource for Sharing and Publishing of Biological Networks. Methods Mol Biol, 1558: 271-301 (2017).
.. [6] Pratt et al. NDEx 2.0: A Clearinghouse for Research on Cancer Pathways. Cancer Res. Nov 1;77(21):e58-e61 (2017).
