.. _overlap:

==================================================
Overlap analysis
==================================================

Principle
------------


The overlap analysis calculates the **overlap** between chemicals **target genes** and **rare disease pathways**. In
other words, it looks for target genes that are part of rare disease pathways, i.e. **direct overlap**
(:numref:`overviewFig` - left part). This approach is presented in Ozisik *et al.,* [1]_ for a specific use case.

First, an **overlap** between target genes and all the rare disease pathways is computed. Then, a **statistical significance**
is calculated using an **hypergeometric test**. Finally, a **Benjamini-Hochberg** (BH adjusted) correction is applied
to correct the pvalues.

Usage
-------

By default, data are directly retrieved from databases using queries (:numref:`overlapUsageFig`: section *data retrieved*
*by queries*). **Chemical target genes** are retrieved from the |ctd|_ [2]_ (CTD) using ``--chemicalsFile`` parameter.
All **rare disease pathways** are retrieved from |wp|_ [3]_ automatically.

In addition, the user can provide their own **target genes** and **pathways/processes of interest**
(:numref:`overlapUsageFig`: section *data provided by user*) using ``--targetGenesFile`` and ``--GMT``,
``--backgroundFile``.

The ``--outputPath`` parameter is used whatever how data are retrieved.

.. _overlapUsageFig:
.. figure:: ../../pictures/Approaches/Overlap_Overwiew.png
    :alt: overlapUsageFig
    :align: center

    : Input and output of overlap analysis

    (Left part) - Chemical target genes and rare disease pathways are retrieved using automatic queries. The user can
    also provide their own data. Required input are represented with pink and green solid border line boxes whereas
    optional input are represented with dashed border line boxes.
    (Right part) - Output files that are in pink are created only if the input data are retrieved by queries.

Input parameters for the overlap analysis
-------------------------------------------

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

-o, --outputPath PATH
    Folder name to save results.
    ``[default: OutputResults]``

Use-cases command lines
-------------------------

Examples of command lines with ``Data retrieved by queries`` and ``Data provided by user``.

.. tabs::

    .. group-tab:: Data retrieved by queries

        .. code-block:: bash

            odamnet overlap --chemicalsFile useCases/InputData/chemicalsFile.csv \
                            --directAssociation FALSE \
                            --nbPub 2 \
                            --outputPath useCases/OutputResults_useCase1/

    .. group-tab:: Data provided by user

        .. code-block:: bash

            odamnet overlap --targetGenesFile useCases/InputData/VitA-Balmer2002-Genes.txt \
                            --GMT useCases/InputData/PathwaysOfInterest.gmt \
                            --backgroundFile useCases/InputData/PathwaysOfInterestBackground.txt \
                            --outputPath useCases/OutputResults_useCase2

References
------------

.. [1] Ozisik O, Ehrhart F, Evelo C *et al.*. Overlap of vitamin A and vitamin D target genes with CAKUT-related processes. F1000Research. 2021.
.. [2] Davis AP, Grondin CJ, Johnson RJ *et al.*. The Comparative Toxicogenomics Database: update 2021. Nucleic acids research. 2021.
.. [3] Martens M, Ammar A, Riutta A *et al.*. WikiPathways: connecting communities. Nucleic acids research. 2021.

.. _ctd: http://ctdbase.org/
.. |ctd| replace:: **the Comparative Toxicogenomics Database**
.. _wp: https://www.wikipathways.org/
.. |wp| replace:: **WikiPathways**