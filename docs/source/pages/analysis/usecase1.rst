.. _usecase1:

============================================================
Use-case 1: data are extracted automatically with requests
============================================================

.. note::

    This analysis is inspired by the study carried out by Ozisik *et al.,* [1]_ .

We want to study the relationship between chemicals (hormones, vitamins etc.) and Rare Diseases.

**Genes**, that are targeted by the interested chemicals, are extracted **directly** from **CTD database**.
**Rare Diseases pathways** are extracted from **WikiPathways** website.
We choose to use as chemical of interest, the **vitamin A**.

This section presents you how perform this such analysis.

.. _useCase1_overlap:
Overlap analysis
=====================

Method : :ref:`overlap`

Chemicals file : :ref:`chemicalsFile`

Running overlap analysis with data extracted automatically from databases
----------------------------------------------------------------------------

The **chemicalsFile.csv** file contains the MeSH ID of vitamin A. We want to extract genes that are targeted by vitamin A
and by its descendant molecules. So, the ``--directAssociation`` parameter is set to ``False``.
We keep only the interaction which has at least to paper as references (``--nbPub 2``).
Results files are saved into ``examples/OutputResults_example1/`` folder.

.. code-block:: bash

        python3 main.py overlap --chemicalsFile useCases/InputData/chemicalsFile.csv \
                                --directAssociation FALSE \
                                --nbPub 2 \
                                --outputPath useCases/OutputResults_useCase1/

Several files are generated :

- ``CTD_request_D014801_2022_09_07.tsv`` and ``CTD_requestFiltered_D014801_2022_09_07.tsv`` :
  the first file contains results from CTD request and the second one contains the filtered (by paper number) results.

- ``WP_RareDiseases_request_2022_09_07.gmt`` and ``WP_allPathways_request_2022_09_07.gmt`` :
  the first file contains all the **human rare diseases pathways** from WikiPathways request
  and the second file **background source file names**.

- ``Overlap_D014801_withRDWP.csv`` : results of the overlap analysis between targeted genes and rare diseases pathways.

For more details about these file, see :doc:`../formats/Output` page.

Results of overlap analysis with data extracted automatically from databases
-------------------------------------------------------------------------------

*request on the 07th of September 2022*

CTD request results
~~~~~~~~~~~~~~~~~~~~~

We extracted genes that are targeted by **vitamin A** and by its child molecules.

.. table:: Request result metrics
    :align: center

    +----------------------------------+---------------------+-----------------+
    |                                  | Number of molecules | Number of genes |
    +==================================+=====================+=================+
    |          Request result          |          8          |      7 765      |
    +----------------------------------+---------------------+-----------------+
    | After filtering by papers number |          7          |      2 143      |
    +----------------------------------+---------------------+-----------------+

WikiPathways request results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All pathways labeled as Rare Diseases are extracted from WikiPathways.

.. table:: WikiPathways metrics
    :align: center

    +------------------------+--------------------+---------------------+---------------------+
    |                        | Number of pathways | Min number of genes | Max number of genes |
    +========================+====================+=====================+=====================+
    | Rare Diseases Pathways |         104        |          3          |         436         |
    +------------------------+--------------------+---------------------+---------------------+
    | All Human WikiPathways |        1 281       |          1          |         484         |
    +------------------------+--------------------+---------------------+---------------------+

Overlap analysis results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Target genes overlap significantly ``28 Rare Diseases pathways`` (pAdjusted <= 0.05). Top 5 of results are presented in
:ref:`Table 4 <useCase1OverlapTop5>`.

.. _useCase1OverlapTop5:
.. table:: The top 5 of RD pathways significantly overlaped by target genes
    :align: center

    +------------+--------------------------------------------------+--------------+------------------+
    | PathwayIDs |                   PathwayNames                   |   pAdjusted  | IntersectionSize |
    +============+==================================================+==============+==================+
    |   WP5087   | Malignant pleural mesothelioma                   |   3.77e-24   |        146       |
    +------------+--------------------------------------------------+--------------+------------------+
    |   WP4298   | Acute viral myocarditis                          |   9.38e-16   |        45        |
    +------------+--------------------------------------------------+--------------+------------------+
    |   WP2447   | Amyotrophic lateral sclerosis (ALS)              |   1.04e-11   |        25        |
    +------------+--------------------------------------------------+--------------+------------------+
    | **WP5053** | **Development of ureteric collection system**    | **2.61e-08** |      **28**      |
    +------------+--------------------------------------------------+--------------+------------------+
    |   WP4879   | Overlap between signal transduction pathways ... |   7.80e-07   |        25        |
    +------------+--------------------------------------------------+--------------+------------------+

Ozisik *et al.,* [1]_ identified four pathways, related to CAKUT disease. All of them are significantly overlaped by vitamin A
target genes. We retrieve one of them in the top 5 (**WP5053**). Two others are significantly overlaped in our analysis
(:ref:`Table 5 <useCase1OverlapCAKUT>`) :

.. _useCase1OverlapCAKUT:
.. table:: The CAKUT pathways results
    :align: center

    +------------+-----------------------------------------------+--------------+------------------+
    | PathwayIDs |                  PathwayNames                 |   pAdjusted  | IntersectionSize |
    +============+===============================================+==============+==================+
    | **WP5053** | **Development of ureteric collection system** | **2.61e-08** |      **28**      |
    +------------+-----------------------------------------------+--------------+------------------+
    | **WP4830** | **GDNF/RET signaling axis**                   | **1.99e-05** |      **13**      |
    +------------+-----------------------------------------------+--------------+------------------+
    | **WP4823** | **Genes controlling nephrogenesis**           | **8.72e-05** |      **18**      |
    +------------+-----------------------------------------------+--------------+------------------+
    |   WP5052   | Nephrogenesis                                 |     0.09     |         6        |
    +------------+-----------------------------------------------+--------------+------------------+

The WP5052 pathway is not significant anymore (compare to Ozisik *et al.,* [1]_ results) because the number of genes between
target genes and pathways are smaller. It affects the pvalue calculation.


.. _useCase1_AMI:
AMI
=====================

.. _useCase1_RWR:
RWR
=====================

References
============
.. [1] Ozisik, O., Ehrhart, F., Evelo, C. T., Mantovani, A., & Baudot, A. (2021). Overlap of vitamin A and vitamin D target genes with CAKUT-related processes. F1000Research, 10.
