.. _overlap:

==================================================
Overlap analysis
==================================================

Principle
------------

.. note::

    This approach is the one implemented in Ozisik *et al.,* [1]_ .

This method calculates the **overlap** between **target genes** and **pathways of interest**.
In other words, it looks for genes that are part of pathways, i.e. **direct overlap**
(:numref:`overviewFig` - left part).

First, an **overlap** between target genes and all the pathways is computed. Then, a **statistical significance**
is calculated using an **hypergeometric test**. Finally, a **Benjamini-Hochberg** (BH adjusted) correction is applied
to correct the pvalues.

Usage
-------

By default, data are extracted directly by request databases (:numref:`overlapFig`: *data from requests*).
You give the ``--chemicalsFile`` and the **target genes** are extracted from **CTD**. **Rare Disease pathways** are
extracted from **WP** automatically too. You can give some optional parameters to custom the selection of target genes.


You can provide your own **target genes file** and **pathways/processes of interest** (:numref:`overlapFig`: *data from users*)
with ``--targetGenesFile`` and ``--GMT``, ``--backgroundFile``.

.. _overlapFig:
.. figure:: ../../pictures/OverlapAnalysis_graph.png
    :alt: overlap analysis
    :align: center

    : Input and output files of overlap analysis

    There is two ways to extract target genes : from request (pink boxes) or provided by the user (green boxes).
    Required files/parameters have solid border line and optional files/parameters have dash border line.
    Output files in pink are created only if the input data are extracted from requests.

Input parameters for overlap analysis
----------------------------------------

To extract target genes from **CTD** and RD pathways from **WP**, see parameters on the ``Data extracted from requests`` tab.
To provide **your own** target genes and pathways/processes files, see parameters on the ``Data extracted from user`` tab.

The ``--outputPath`` parameter is use for both data extraction.

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

-o, --outputPath PATH
    Name of the folder where to save the results.
    ``[default: OutputResults]``

Use-cases command line
------------------------

.. tabs::

    .. group-tab:: Data extracted from requests

        .. code-block:: bash

            python3 main.py overlap --chemicalsFile useCases/InputData/chemicalsFile.csv \
                                    --directAssociation FALSE \
                                    --nbPub 2 \
                                    --outputPath useCases/OutputResults_useCase1/

    .. group-tab:: Data extracted from user

        .. code-block:: bash

            python3 main.py overlap --targetGenesFile useCases/InputData/VitA-Balmer2002-Genes.txt \
                                    --GMT useCases/InputData/PathwaysOfInterest.gmt \
                                    --backgroundFile useCases/InputData/PathwaysOfInterestBackground.txt \
                                    --outputPath useCases/OutputResults_useCase2/

References
------------

.. [1] Ozisik, O., Ehrhart, F., Evelo, C. T., Mantovani, A., & Baudot, A. (2021). Overlap of vitamin A and vitamin D target genes with CAKUT-related processes. F1000Research, 10.
