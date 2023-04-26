.. _AMI:

==================================================
Active Module Identification
==================================================

Principle
------------

.. note::

    | Active Module Identification (AMI) is performed using DOMINO [1]_. The analysis is running on their server [2]_.
    | :octicon:`mark-github;1em` `DOMINO web GitHub <https://github.com/Shamir-Lab/domino_web>`_ -- :octicon:`globe;1em` `DOMINO server <http://domino.cs.tau.ac.il/>`_

DOMINO is looking for **active modules** in a network (e.g. protein-protein interaction (PPI) network)
(:numref:`overviewFig` - middle part).

First, DOMINO defines target genes as **active genes**. Then DOMINO tries to **identify active modules**.

Active modules are **subnetworks** identified as relevant and composed of active genes (i.e. target genes) and other
associated genes. Ideally, they will represent **functional modules** and can thereby reveal biological processes
involved in a specific condition.

Finally, we performed an **overlap analysis** between each identified active module by DOMINO and rare disease pathways.

Overview of the DOMINO algorithm
-----------------------------------

The :numref:`dominoMethodFig` is an overview of the DOMINO algorithm.

.. _dominoMethodFig:
.. figure:: ../../pictures/Approaches/AMI_DOMINO_method.jpg
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

By default, data are directly retrieved from databases using queries (:numref:`dominoUsageFig`: section *data retrieved*
*by queries*). **Chemical target genes** are retrieved from the |ctd|_ [3]_ (CTD) using ``--chemicalsFile`` parameter.
All **rare disease pathways** are retrieved from |wp|_ [4]_ automatically. The **biological network** is also downloaded
from the |ndex|_ [5]_ using ``--netUUID`` and ``--networkFile`` parameters.

You can provide your own **target genes**, **pathways/processes of interest** and **biological network**
(:numref:`dominoUsageFig`: section *data provided by user*) using ``--targetGenesFile``, ``--GMT``,
``--backgroundFile`` and ``--networkFile``.

The network file is required ``--networkFile`` whereas ``--outputPath`` is optional.

.. _dominoUsageFig:
.. figure:: ../../pictures/Approaches/AMI_Overwiew.png
    :alt: dominoUsageFig
    :align: center

    : Input and output of Active Modules Identification (AMI)

    (Left part) - Chemical target genes, rare disease pathways and biological networks are retrieved using automatic
    queries. The user can also provide their own data. Required input are represented with pink and green solid border
    line boxes whereas optional input are represented with dashed border line boxes.
    (Right part) - Output files that are in pink are created only if the input data are retrieved by queries.

Input parameters for the Active Modules Identification
--------------------------------------------------------

.. warning::

    - Gene IDs have to be **consistent** between input data *(target genes, GMT and networks)*
    - When data are retrieved by queries, **HGNC** IDs are used.

| To use data retrieved from databases, see parameters on the ``Data retrieved by queries`` tab.
| To provide **your own** data, see parameters on the ``Data provided by user`` tab.

.. tabs::

    .. group-tab:: Data retrieved by queries

        -c, --chemicalsFile FILENAME
            Contains a list of chemicals. They have to be in **MeSH** identifiers (e.g. D014801).
            Each line contains one or several chemical IDs, separated by ";"
            [:ref:`FORMAT <chemicalsFile>`] **[required]**

        --directAssociation BOOLEAN
            | ``TRUE``: retrieve genes targeted by chemicals, from CTD
            | ``FALSE``: retrieve genes targeted by chemicals and theirs descendant chemicals, from CTD
            | ``[default: True]``

        --nbPub INTEGER
            Each interaction between target gene and chemical can be associated with publications.
            You can filter these interactions according the number of publication associated.
            You can define a minimum number of publications to keep an association.
            ``[default: 2]``

        --netUUID TEXT
            Network UUID to download biological network from NDEx (e.g. ``079f4c66-3b77-11ec-b3be-0ac135e8bacf``)

    .. group-tab:: Data provided by user

        -t, --targetGenesFile FILENAME
            Contains a list of target genes. One target gene per line. [:ref:`FORMAT <targetGenesFile>`]
            **[required]**

        --GMT FILENAME
            Tab-delimited file that describes gene sets of pathways/processes of interest.
            Pathways/processes can come from several sources *(e.g. WP and GO\:BP)*.
            [:ref:`FORMAT <GMTFile>`]
            **[required]**

        --backgroundFile FILENAME
            List of the different background source file name. Each background genes source is a GMT file.
            It should be in the same order than the GMT file.
            [:ref:`FORMAT <bgFile>`]
            **[required]**

-n, --networkFile FILENAME
    Network file name that contains network or to save network.
    The file is in SIF format [:ref:`FORMAT <SIF>`] **[required]**

-o, --outputPath PATH
    Folder name to save results.
    ``[default: OutputResults]``

Use-cases command lines
-------------------------

Examples of command lines with ``Data retrieved by queries`` and ``Data provided by user``.

.. tabs::

    .. group-tab:: Data retrieved by queries

        .. code-block:: bash

            odamnet domino  --chemicalsFile useCases/InputData/chemicalsFiles.csv \
                            --directAssociation FALSE \
                            --nbPub 2 \
                            --networkFile useCases/InputData/PPI_HiUnion_LitBM_APID_gene_names_190123.tsv \
                            --netUUID bfac0486-cefe-11ed-a79c-005056ae23aa \
                            --outputPath useCases/OutputResults_useCase1

    .. group-tab:: Data provided by user

        .. code-block:: bash

            odamnet domino  --targetGenesFile useCases/InputData/VitA-Balmer2002-Genes.txt \
                            --GMT useCases/InputData/PathwaysOfInterest.gmt \
                            --backgroundFile useCases/InputData/PathwaysOfInterestBackground.txt \
                            --networkFile useCases/InputData/PPI_HiUnion_LitBM_APID_gene_names_190123.tsv \
                            --outputPath useCases/OutputResults_useCase2

References
------------

.. [1] Levi H, Elkon R & Shamir R. DOMINO: a network‐based active module identification algorithm with reduced rate of false calls. Molecular systems biology. 2021.
.. [2] Levi H, Rahmanian N, Elkon R *et al.*. The DOMINO web-server for active module identification analysis. Bioinformatics. 2022.
.. [3] Davis AP, Grondin CJ, Johnson RJ *et al.*. The Comparative Toxicogenomics Database: update 2021. Nucleic acids research. 2021.
.. [4] Martens M, Ammar A, Riutta A *et al.*. WikiPathways: connecting communities. Nucleic acids research. 2021.
.. [5] Pratt D, Chen J, Welker *et al.*. NDEx, the Network Data Exchange. Cell Systems. 2015.

.. _ctd: http://ctdbase.org/
.. |ctd| replace:: Comparative Toxicogenomics Database
.. _wp: https://www.wikipathways.org/
.. |wp| replace:: WikiPathways
.. _ndex: https://www.ndexbio.org/#/
.. |ndex| replace:: Network Data Exchange