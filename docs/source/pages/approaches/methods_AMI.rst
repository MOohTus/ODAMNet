.. _AMI:

==================================================
Active Module Identification
==================================================

Principle
------------

.. note::

    | Active Module Identification (AMI) is performed using DOMINO [1]_. The analysis is running on their server [2]_.
    | :octicon:`mark-github;1em` `DOMINO web GitHub <https://github.com/Shamir-Lab/domino_web>`_ -- :octicon:`globe;1em` `DOMINO server <http://domino.cs.tau.ac.il/>`_

DOMINO is looking for **active modules** in a network (e.g. protein-protein interaction (PPI) network) (:numref:`overviewFig` - middle part).

First, DOMINO defines target genes as **active genes**. Then DOMINO tries to **identify active modules**.

Active modules are **subnetworks** identified as relevant and composed of active genes (i.e. target genes) and other associated genes.
Ideally, they will represent **functional modules** and can thereby reveal biological processes involved in a specific condition.

Finally, we performed an **overlap analysis** between each identified active module by DOMINO and pathways/processes
of interest.

Overview of the DOMINO algorithm
-----------------------------------

The :numref:`dominoMethodFig` is an overview of the DOMINO algorithm.

.. _dominoMethodFig:
.. figure:: ../../pictures/DOMINO_method.jpg
    :alt: DOMINO method
    :align: center

    : Schematic illustration of DOMINO (Fig3 from DOMINO's paper [1]_)

| **A - Step 0:** The network is clustered into disjoint and highly connected subnetworks (slices) with the Louvain algorithm, based on modularity optimization.
| **B - Step 1:** The relevant slices (where active genes are over-represented) are detected using the Hypergeometric test. Pvalue are corrected with the FDR method.
| **C - Step 2a:** The most active sub-slice is identified on each relevant slices.
| **D - Step 2b:** The sub-slices are split into putative active modules  using the Newmann-Girvan modularity algorithm.
| **E - Step 3:** The final set of active module is identified (under a threshold of Bonferroni qval<=0.05).

*For more details, see to the DOMINO's publication* [1]_.

Usage
-------

By default, data are extracted directly by requesting databases (:numref:`dominoUsageFig`: section *data extracted from requests*).
You give the ``--chemicalsFile`` and the **target genes** are extracted from the **Comparative Toxicogenomics Database** (CTD).
**Rare disease pathways** are extracted from **WikiPathways** automatically too.
You can give some optional parameters to custom the selection of target genes.

You can provide your own **target genes file** and **pathways/processes of interest**
(:numref:`dominoUsageFig`: section *data provided by users*) with ``--targetGenesFile`` and ``--GMT``, ``--backgroundFile``.

.. _dominoUsageFig:
.. figure:: ../../pictures/Overview_AMI.png
    :alt: domino analysis
    :align: center

    : Input and output of Active Modules Identification (AMI)

    (Left part) - Target genes and rare disease pathways can be extracted using automatic request. The users can also
    provide their own data. Required input are represented with pink and green solid border line boxes whereas optional
    input are represented with dashed border line boxes.
    (Right part) - Output files that are in pink are created only if the input data are extracted from request.

Input parameters for the Active Modules Identification
--------------------------------------------------------

.. warning::

    - Gene IDs have to be **consistent** between input data *(target genes, GMT and networks)*
    - When data are retrieved by requests, **HGNC** IDs are used.

| To extract target genes from **CTD** and rare disease pathways from **WikiPathways**, see parameters on the ``Data extracted from requests`` tab.
| To provide **your own** target genes and pathways/processes files, see parameters on the ``Data provided by users`` tab.

The network file is required ``--networkFile`` whereas ``--netUUID`` and ``--outputPath`` are optional.

.. tabs::

    .. group-tab:: Data extracted from requests

        -c, --chemicalsFile FILENAME
            Contains a list of chemicals. They have to be in **MeSH** identifiers (e.g. D014801).
            Each line contains one or several chemical IDs, separated by ";".
            [:ref:`FORMAT <chemicalsFile>`] **[required]**

        --directAssociation BOOLEAN
            | ``TRUE``: extract chemicals data, which are in the chemicalsFile, from CTD
            | ``FALSE``: extract chemicals and their descendant chemicals data from CTD
            | ``[default: True]``

        --nbPub INTEGER
            Each interaction between target gene and chemical can be associated with publications.
            You can filter these interactions according the number of publication associated.
            You can define a minimum number of publications.
            ``[default: 2]``

    .. group-tab:: Data provided by users

        -t, --targetGenesFile FILENAME
            Contains a list of target genes. One target gene per line. [:ref:`FORMAT <targetGenesFile>`]
            **[required]**

        --GMT FILENAME
            Tab-delimited file that describes gene sets of pathways/processes of interest.
            Pathways/processes can come from several sources (e.g. WikiPathways and GO\:BP).
            [:ref:`FORMAT <pathways>`]
            **[required]**

        --backgroundFile FILENAME
            List of the different background source file name. Each background genes source is a GMT file.
            It should be in the same order than the GMT file.
            [:ref:`FORMAT <pathways>`]
            **[required]**

-n, --networkFile FILENAME
    Network file name. The file is in SIF format [:ref:`FORMAT <SIF>`] **[required]**

--netUUID TEXT
    You can use a network extracted automatically from `NDEx <https://www.ndexbio.org/#/>`_ [3]_. You have to provide
    the UUID of the network (e.g. ``079f4c66-3b77-11ec-b3be-0ac135e8bacf``).

-o, --outputPath PATH
    Name of the folder to save results.
    ``[default: OutputResults]``

Use-cases command lines
-------------------------

.. tabs::

    .. group-tab:: Data extracted from requests

        .. code-block:: bash

            odamnet domino  --chemicalsFile useCases/InputData/chemicalsFile.csv \
                                    --directAssociation FALSE \
                                    --nbPub 2 \
                                    --networkFile useCases/InputData/PPI_network_2016.sif \
                                    --outputPath useCases/OutputResults_useCase1/

    .. group-tab:: Data provided by users

        .. code-block:: bash

            odamnet domino  --targetGenesFile useCases/InputData/VitA-Balmer2002-Genes.txt \
                                    --GMT useCases/InputData/PathwaysOfInterest.gmt \
                                    --backgroundFile useCases/InputData/PathwaysOfInterestBackground.txt \
                                    --networkFile useCases/InputData/PPI_network_2016.sif \
                                    --outputPath useCases/OutputResults_useCase2/

References
------------

.. [1] Levi, H., Elkon, R., & Shamir, R. (2021). DOMINO: a network‐based active module identification algorithm with reduced rate of false calls. Molecular systems biology, 17(1), e9593.
.. [2] Levi, H., Rahmanian, N., Elkon, R., & Shamir, R. (2022). The DOMINO web-server for active module identification analysis. Bioinformatics, 38(8), 2364-2366.
.. [3] Pratt et al. NDEx, the Network Data Exchange. Cell Systems, Vol. 1, Issue 4: 302-305 (2015).
