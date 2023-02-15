.. _overlap:

==================================================
Overlap analysis
==================================================

Principle
------------

.. note::

    This approach is the one implemented in Ozisik *et al.,* [1]_ .

The overlap analysis calculates the **overlap** between **target genes** and **pathways of interest**.
In other words, it looks for target genes that are part of pathways, i.e. **direct overlap**
(:numref:`overviewFig` - left part).

First, an **overlap** between target genes and all the pathways is computed. Then, a **statistical significance**
is calculated using an **hypergeometric test**. Finally, a **Benjamini-Hochberg** (BH adjusted) correction is applied
to correct the pvalues.

Usage
-------

By default, the data are directly extracted by requests on databases (:numref:`overlapFig`: section *data extracted from requests*).
The user gives the ``--chemicalsFile`` and the **target genes** are extracted from **CTD**. The user can also provide
optional parameters to customize the selection of target genes.

All **Rare Disease pathways** are extracted from **WikiPathways** (WP) automatically.

In addition, the user can provide their own **target genes** and **pathways/processes of interest** files
(:numref:`overlapFig`: section *data extracted from users*) with ``--targetGenesFile`` and ``--GMT``, ``--backgroundFile``.

.. _overlapFig:
.. figure:: ../../pictures/OverlapAnalysis_graph.png
    :alt: overlap analysis
    :align: center

    : Input and output files/parameters of overlap analysis

    There are two ways to extract target genes: from automatic request (pink boxes) or provided by the user (green boxes).
    Required files/parameters have solid border line and optional files/parameters have dash border line.
    Output files in pink are created only if the input data are extracted from requests.

Input parameters for the overlap analysis
-------------------------------------------

| To extract target genes from **CTD** and RD pathways from **WP**, see parameters on the ``Data extracted from requests`` tab.
| To provide **your own** target genes and pathways/processes files, see parameters on the ``Data extracted from user`` tab.

The ``--outputPath`` parameter is used for both data extraction.

.. tabs::

    .. group-tab:: Data extracted from requests

        -c, --chemicalsFile FILENAME
            Contains a list of chemicals. They have to be in **MeSH** identifiers (e.g. D014801).
            You can give several chemicals in the same line : they will be grouped for the analysis.
            [:ref:`FORMAT <chemicalsFile>`] **[required]**

        --directAssociation BOOLEAN
            | ``TRUE``: extract chemicals data, which are in the chemicalsFile, from CTD
            | ``FALSE``: extract chemicals and their child molecules data from CTD
            | ``[default: True]``

        --nbPub INTEGER
            Publications can be associated with chemical interactions.
            You can define a minimum number of publications to keep target genes.
            ``[default: 2]``

    .. group-tab:: Data extracted from user

        -t, --targetGenesFile FILENAME
            Contains a list of target genes. One gene per line. [:ref:`FORMAT <targetGenesFile>`]
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

-o, --outputPath PATH
    Name of the folder to save results.
    ``[default: OutputResults]``

Use-cases command lines
-------------------------

.. tabs::

    .. group-tab:: Data extracted from requests

        .. code-block:: bash

            odamnet overlap --chemicalsFile useCases/InputData/chemicalsFile.csv \
                                    --directAssociation FALSE \
                                    --nbPub 2 \
                                    --outputPath useCases/OutputResults_useCase1/

    .. group-tab:: Data extracted from user

        .. code-block:: bash

            odamnet overlap --targetGenesFile useCases/InputData/VitA-Balmer2002-Genes.txt \
                                    --GMT useCases/InputData/PathwaysOfInterest.gmt \
                                    --backgroundFile useCases/InputData/PathwaysOfInterestBackground.txt \
                                    --outputPath useCases/OutputResults_useCase2/

References
------------

.. [1] Ozisik, O., Ehrhart, F., Evelo, C. T., Mantovani, A., & Baudot, A. (2021). Overlap of vitamin A and vitamin D target genes with CAKUT-related processes. F1000Research, 10.
