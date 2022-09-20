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

This section presents you how to perform the approaches that we proposed.

.. _useCase1_overlap:
Overlap analysis
=====================

This approach calculates the overlap between list of genes, targeted by vitamin A, and Rare Diseases pathways
(see :doc:`../approaches/methods_overlap` section for more details).

Running overlap analysis with data extracted automatically from databases
----------------------------------------------------------------------------

The **chemicalsFile.csv** file [:ref:`FORMAT <chemicalsFile>`] contains the MeSH ID of vitamin A. We want to extract genes that are targeted by vitamin A
and by its descendant molecules. So, the ``--directAssociation`` parameter is set to ``False``.
We keep only the interaction which has at least to paper as references (``--nbPub 2``).
Results files are saved into ``useCases/OutputResults_useCase1/`` folder.

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

    +------------------------+-----------------+------------------+------------------+
    |                        | Pathways number | Min genes number | Max genes number |
    +========================+=================+==================+==================+
    | Rare Diseases Pathways |       104       |         3        |        436       |
    +------------------------+-----------------+------------------+------------------+
    | All Human WikiPathways |      1 281      |         1        |        484       |
    +------------------------+-----------------+------------------+------------------+

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

This approach identifies Active Modules (AM) through a Protein-Protein Interaction (PPI) network. Then it performs an
overlap analysis between each AM identified and Rare Diseases pathways frm WP.
For more detail, see :doc:`../approaches/methods_AMI` section.

Running active modules identification with data extracted automatically from databases
-----------------------------------------------------------------------------------------

.. warning::

   :octicon:`alert;2em` Results of DOMINO can't be reproduced when using their server.

As before, we want to extract genes that are targeted by vitamin A and its child molecules. The **chemicalsFile.csv** file
[:ref:`FORMAT <chemicalsFile>`] contains the MeSH ID of vitamin A and we set ``--directAssociation`` parameter to ``False``.
We keep only the interaction which has at least to paper as references (``--nbPub 2``).

We will identify AM using a Protein-Protein Interaction (PPI) network named ``PPI_network_2016.sif`` [:ref:`FORMAT <SIF>`].

Results files are saved into ``useCases/OutputResults_useCase1/`` folder.

.. code-block:: bash

        python3 main.py domino  --chemicalsFile useCases/InputData/chemicalsFile.csv \
                                --directAssociation FALSE \
                                --nbPub 2 \
                                --networkFile useCases/InputData/PPI_network_2016.sif \
                                --outputPath useCases/OutputResults_useCase1/

Several files are generated :

- ``CTD_request_D014801_2022_09_07.tsv`` and ``CTD_requestFiltered_D014801_2022_09_07.tsv`` :
  the first file contains results from CTD request and the second one contains the filtered (by paper number) results.

- ``WP_RareDiseases_request_2022_09_07.gmt`` and ``WP_allPathways_request_2022_09_07.gmt`` :
  the first file contains all the **human rare diseases pathways** from WikiPathways request
  and the second file **background source file names**.

- ``DOMINO_inputGeneList_D014801.txt`` : list of genes (targeted by vitamin A) used for the AM identification.

- ``Overlap_AM_*_D014801_withRDWP.csv`` : results of the overlap analysis between target genes and Rare Diseases pathways.
  One file for each AM.

- ``DOMINO_D014801_activeModulesNetwork.txt``, ``DOMINO_D014801_overlapAMresults4Cytoscape.txt``, ``DOMINO_D014801_activeModules.txt``
  , ``DOMINO_D014801_activeModulesNetworkMetrics.txt`` and ``DOMINO_D014801_signOverlap.txt`` : some metrics are
  calculated and saved into files. Theses files are useful for visualisation.

For more details about these file, see :doc:`../formats/Output` page (:ref:`requestOutput`, :ref:`overlapOutput`, :ref:`AMIOutput`)

Results of active module identification with data extracted automatically from databases
-------------------------------------------------------------------------------------------

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

    +------------------------+-----------------+------------------+------------------+
    |                        | Pathways number | Min genes number | Max genes number |
    +========================+=================+==================+==================+
    | Rare Diseases Pathways |       104       |         3        |        436       |
    +------------------------+-----------------+------------------+------------------+
    | All Human WikiPathways |      1 281      |         1        |        484       |
    +------------------------+-----------------+------------------+------------------+

Active Modules Identification results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Target genes are defined as Active genes by DOMINO (Active Modules identification tool). We give **2 143 active genes** as input.

We found **13 Active Modules** :

.. table:: DOMINO result metrics
    :align: center

    +--------------+------------+------------+
    |              | Min number | Max number |
    +==============+============+============+
    |     Edges    |     20     |     357    |
    +--------------+------------+------------+
    |     Nodes    |     17     |     93     |
    +--------------+------------+------------+
    | Active Genes |      8     |     35     |
    +--------------+------------+------------+

*See DOMINO_D014801_activeModulesNetworkMetrics.txt file for more details.*

Overlap analysis results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We found **16 pathways** that are significantly overlaped by **6 Active Modules** (padjusted <= 0.05).

.. table:: Overlap analysis between AM and RD pathways
    :align: center

    +------------+---------------------------------------------------------------------------------+
    | termID     | termTitle                                                                       |
    +============+=================================================================================+
    | WP2059     | Alzheimer's disease and miRNA effects                                           |
    +------------+---------------------------------------------------------------------------------+
    | WP2447     | Amyotrophic lateral sclerosis (ALS)                                             |
    +------------+---------------------------------------------------------------------------------+
    | WP3853     | ERK pathway in Huntington's disease                                             |
    +------------+---------------------------------------------------------------------------------+
    | WP4298     | Acute viral myocarditis                                                         |
    +------------+---------------------------------------------------------------------------------+
    | WP4541     | Hippo-Merlin signaling dysregulation                                            |
    +------------+---------------------------------------------------------------------------------+
    | WP4549     | Fragile X syndrome                                                              |
    +------------+---------------------------------------------------------------------------------+
    | WP4746     | Thyroid hormones production and peripheral downstream signaling effects         |
    +------------+---------------------------------------------------------------------------------+
    | **WP4823** | **Genes controlling nephrogenesis**                                             |
    +------------+---------------------------------------------------------------------------------+
    | **WP4830** | **GDNF/RET signaling axis**                                                     |
    +------------+---------------------------------------------------------------------------------+
    | WP4844     | Influence of laminopathies on Wnt signaling                                     |
    +------------+---------------------------------------------------------------------------------+
    | WP4879     | Overlap between signal transduction pathways contributing to LMNA laminopathies |
    +------------+---------------------------------------------------------------------------------+
    | WP4950     | 16p11.2 distal deletion syndrome                                                |
    +------------+---------------------------------------------------------------------------------+
    | WP5087     | Malignant pleural mesothelioma                                                  |
    +------------+---------------------------------------------------------------------------------+
    | WP5102     | Familial partial lipodystrophy                                                  |
    +------------+---------------------------------------------------------------------------------+
    | WP5124     | Alzheimer's disease                                                             |
    +------------+---------------------------------------------------------------------------------+
    | WP5269     | Genetic causes of PSVD/INCPH                                                    |
    +------------+---------------------------------------------------------------------------------+

**Two pathways** related to CAKUT disease are found with this approach.

Visualisation of AM results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We visualised the result using a network representation (:numref:`dominoUsage1Fig`). To know how to create this figure, see the :ref:`networkAMI` section.

.. _dominoUsage1Fig:
.. image:: ../../pictures/example1_DOMINO_AMnetwork.png
   :alt: usecase1 AMI

.. _useCase1_RWR:
RWR
=====================

Running Random Walk analysis with data extracted automatically from databases
--------------------------------------------------------------------------------

Results of Random Walk analysis with data extracted automatically from databases
-----------------------------------------------------------------------------------

*request on the 07th of September 2022*

CTD request results
~~~~~~~~~~~~~~~~~~~~~

Random Walk with Restart results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

References
============
.. [1] Ozisik, O., Ehrhart, F., Evelo, C. T., Mantovani, A., & Baudot, A. (2021). Overlap of vitamin A and vitamin D target genes with CAKUT-related processes. F1000Research, 10.
