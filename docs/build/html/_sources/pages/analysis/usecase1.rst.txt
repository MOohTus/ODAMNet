============================================================
Use-case 1: data are retrieved automatically by queries
============================================================

.. note::

    This analysis is inspired by the study carried out by Ozisik *et al.,* [1]_.

In this use-case, we want to study the molecular relationship between **vitamin A** and **rare diseases**.

Vitamin A **target genes** are retrieved **directly** from the |ctd|_ [2]_ (CTD). **Rare disease pathways** are
retrieved from |wp|_ [3]_. Biological **networks** used are also downloaded automatically from |ndex|_ [4]_.

|input|_ and |output|_ are available in GitHub.

This section presents you how to apply the three different approaches proposed.

.. _useCase1_overlap:

Overlap analysis
=====================

The Overlap analysis searches intersecting genes between vitamin A target genes and genes involved in rare disease
pathways. See :doc:`../approaches/methods_overlap` page for more details.

Running Overlap analysis with data retrieved automatically from databases
----------------------------------------------------------------------------

The **chemicalsFile.csv** file [:ref:`FORMAT <chemicalsFile>`] contains the MeSH ID of vitamin A (D014801). We retrieved
from CTD, genes targeted by the vitamin A and its descendant chemicals (``--directAssociation FALSE``). We keep only
vitamin A - gene interactions which have at least two associated publications (``--nbPub 2``).

**Rare disease pathways** are retrieved automatically from WikiPathways.

Results files are saved into ``useCases/OutputResults_useCase1/`` folder.

.. code-block:: bash

        odamnet overlap --chemicalsFile useCases/InputData/chemicalsFile.csv \
                        --directAssociation FALSE \
                        --nbPub 2 \
                        --outputPath useCases/OutputResults_useCase1/

Several files are generated:

- ``CTD_request_D014801_2022_09_07.tsv`` and ``CTD_requestFiltered_D014801_2022_09_07.tsv``:
  the first file contains **results from CTD** query and the second one contains the results filtered using the
  publication number.

- ``WP_RareDiseases_request_2022_09_07.gmt`` and ``WP_allPathways_request_2022_09_07.gmt``:
  the first file contains **human rare disease pathways** and the second file contains **all human pathways** retrieved
  in WikiPathways.

- ``Overlap_D014801_withRDWP.csv``: results of the Overlap analysis between vitamin A target genes and rare disease
  pathways.

.. cssclass:: italic

    For more details about these files, see :ref:`queryOutput` and :ref:`overlapOutput` sections.

Results of Overlap analysis with data retrieved automatically from databases
-------------------------------------------------------------------------------

*Queries made on September 7th, 2022*

CTD query results
~~~~~~~~~~~~~~~~~~~~~

We retrieved 7,765 genes targeted by 10 chemicals (vitamin A + nine descendant chemicals) in CTD
(:ref:`Table 2 <useCase1_OverlapCTD>`). Chemical - gene associations are kept if they have at least two publications for
human. After filtering, we have **2,143 vitamin A target genes** for 7 chemicals (vitamin A + its descendant molecules).

.. _useCase1_OverlapCTD:
.. table:: - Vitamin A target genes retrieved from CTD
    :align: center

    +---------------------------------------------------+---------------------+------------------------+
    |                                                   | Number of chemicals | Number of target genes |
    +===================================================+=====================+========================+
    |          Query result                             |          10         |      7,765             |
    +---------------------------------------------------+---------------------+------------------------+
    | After filtering by associated publications number |          7          |      2,143             |
    +---------------------------------------------------+---------------------+------------------------+

WikiPathways query results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All human pathways labeled as "rare disease" are retrieved from WikiPathways. We retrieved **104 rare disease pathways**
(:ref:`Table 3 <useCase1_OverlapWP>`). All human pathways are also retrieved from WikiPathways
(:ref:`Table 3 <useCase1_OverlapWP>`). We use these pathways to create background gene sets used for statistical
analysis.

.. _useCase1_OverlapWP:
.. table:: - Pathways retrieval from WikiPathways
    :align: center

    +------------------------+-----------------+------------------+------------------+
    |                        | Pathways number | Min genes number | Max genes number |
    +========================+=================+==================+==================+
    | Rare Disease Pathways  |       104       |         3        |        436       |
    +------------------------+-----------------+------------------+------------------+
    | All Human WikiPathways |      1,281      |         1        |        484       |
    +------------------------+-----------------+------------------+------------------+

Overlap analysis results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We performed an Overlap analysis between vitamin A target genes (2,143) and rare disease pathways (104). We obtained
significant overlap between target genes and **28 rare disease pathways** (pAdjusted <= 0.05). The top 5 is presented in
:ref:`Table 4 <useCase1_OverlapTop5>`.

.. _useCase1_OverlapTop5:
.. table:: - Top 5 of the significant overlaps between the vitamin A target genes and rare disease pathways
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
    |   WP5053   | Development of ureteric collection system        |   2.61e-08   |        28        |
    +------------+--------------------------------------------------+--------------+------------------+
    |   WP4879   | Overlap between signal transduction pathways ... |   7.80e-07   |        25        |
    +------------+--------------------------------------------------+--------------+------------------+

In a previous analysis [1]_, an overlap analysis was performed between vitamin A and Congenital Anomalies of the Kidney
and Urinary Tract (CAKUT). Four pathways related to CAKUT were identified in WikiPathways. Significant overlaps were
identified between these four CAKUT pathways and vitamin A target genes.

With updated target genes data proposed here, we also retrieved significant overlap for 3 of these 4 CAKUT pathways
(:ref:`Table 5 <useCase1_OverlapCAKUT>`).

.. _useCase1_OverlapCAKUT:
.. table:: - Overlap analysis results between vitamin A target genes and CAKUT pathways
    :align: center

    +-----------+---------------------------------------+-------------------+---------------------+
    |           |                                       |  Current analysis |Ozisik *et al.*, 2021|
    +-----------+---------------------------------------+------------+------+------------+--------+
    |PathwayIDs |Pathway Names                          | pAdjusted  |Inter | pAdjusted  | Inter  |
    +===========+=======================================+============+======+============+========+
    |  WP5053   |Development of ureteric collection ... |**2.61e-08**|28    |**1.59e-05**|    16  |
    +-----------+---------------------------------------+------------+------+------------+--------+
    |  WP4830   |GDNF/RET signaling axis                |**1.99e-05**|13    |**1.57e-03**|     8  |
    +-----------+---------------------------------------+------------+------+------------+--------+
    |  WP4823   |Genes controlling nephrogenesis        |**8.72e-05**|18    |**1.84e-05**|    15  |
    +-----------+---------------------------------------+------------+------+------------+--------+
    |  WP5052   |Nephrogenesis                          |    0.09    |6     |**1.90e-04**|     8  |
    +-----------+---------------------------------------+------------+------+------------+--------+

The increase of the intersection size (*Inter column*) can be explained by the target gene size. In the previous work
[1]_, we retrieved 1,086 target genes and in this current work we retrieved 2,143 target genes.

The overlap between *Nephrogenesis* pathway and target genes is not found significant anymore. Number of target genes
shared with the pathway is smaller. It affects the p-value and decreases it below the 0.05 threshold.

The smaller number of shared genes can be explained by the fact that one of the target gene is not related to human so
it's not selected and the other one has only one publication associated and we keep those with at least two publications.

.. _useCase1_AMI:

Active Module Identification (AMI)
======================================

The Active Module Identification (AMI) approach identifies active module that contains high number of vitamin A target
genes using a protein-protein interaction (PPI) network. AMI is performed using DOMINO [5]_. Then, an Overlap analysis
is applied between identified active modules and rare disease pathways. See :doc:`../approaches/methods_AMI` page for
more details.

Running AMI with data retrieved automatically from databases
--------------------------------------------------------------

.. warning::

   :octicon:`alert;2em` When using DOMINO server, **results cannot be identically reproduced**. Indeed, DOMINO server doesn't allow to set the random seed. This random seed changes every new analysis.

The **chemicalsFile.csv** file [:ref:`FORMAT <chemicalsFile>`] contains the MeSH ID of vitamin A (D014801). We retrieved
from CTD, genes targeted by the vitamin A and its descendant chemicals (``--directAssociation FALSE``). We keep only
vitamin A - gene interactions which have at least two associated publications (``--nbPub 2``).

We download automatically a PPI network [:ref:`FORMAT <SIF>`] from NDEx [4]_ using the ``--netUUID`` parameter
(UUID bfac0486-cefe-11ed-a79c-005056ae23aa, version 1.0). We named the PPI network `PPI_HiUnion_LitBM_APID_gene_names_190123.sif`
(``--networkFile``). Network name should be with **.sif** extension.

Results files are saved into ``useCases/OutputResults_useCase1/`` folder.

.. code-block:: bash

        odamnet domino  --chemicalsFile useCases/InputData/chemicalsFiles.csv \
                        --directAssociation FALSE \
                        --nbPub 2 \
                        --networkFile useCases/InputData/PPI_HiUnion_LitBM_APID_gene_names_190123.sif \
                        --netUUID bfac0486-cefe-11ed-a79c-005056ae23aa \
                        --outputPath useCases/OutputResults_useCase1


Several files are generated:

- ``CTD_request_D014801_2022_09_07.tsv`` and ``CTD_requestFiltered_D014801_2022_09_07.tsv``:
  the first file contains **results from CTD** query and the second one contains the results filtered using the
  publication number.

- ``WP_RareDiseases_request_2022_09_07.gmt`` and ``WP_allPathways_request_2022_09_07.gmt``:
  the first file contains **human rare disease pathways** and the second file contains **all human pathways** retrieved
  in WikiPathways.

- ``DOMINO_inputGeneList_D014801.txt``: vitamin A target genes list used for the active module identification.

- ``Overlap_AM_*_D014801_withRDWP.csv``: results of the Overlap analysis between identified active modules genes and
  rare disease pathways. There is one file per active module.

- ``DOMINO_D014801_activeModulesNetwork.txt``, ``DOMINO_D014801_overlapAMresults4Cytoscape.txt``, ``DOMINO_D014801_activeModules.txt``
  , ``DOMINO_D014801_activeModulesMetrics.txt`` and ``DOMINO_D014801_signOverlap.txt``: some statistics are
  calculated and saved into files. Theses files are useful for visualisation.

.. cssclass:: italic

    For more details about these files, see :ref:`queryOutput` and :ref:`AMIOutput` sections.

Results of AMI with data retrieved automatically from databases
------------------------------------------------------------------

*Queries made on September 7th, 2022*

CTD query results
~~~~~~~~~~~~~~~~~~~~~

We retrieved 7,765 genes targeted by 10 chemicals (vitamin A + nine descendant chemicals) in CTD
(:ref:`Table 6 <useCase1_AMICTD>`). Chemical - gene associations are kept if they have at least two publications for
human. After filtering, we have **2,143 vitamin A target genes** for 7 chemicals (vitamin A + its descendant molecules).

.. _useCase1_AMICTD:
.. table:: - Vitamin A target genes retrieved from CTD
    :align: center

    +---------------------------------------+---------------------+-----------------+
    |                                       | Number of chemicals | Number of genes |
    +=======================================+=====================+=================+
    |          Query result                 |          10         |      7,765      |
    +---------------------------------------+---------------------+-----------------+
    | After filtering by publication number |          7          |      2,143      |
    +---------------------------------------+---------------------+-----------------+

WikiPathways query results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All human pathways labeled as "rare disease" are retrieved from WikiPathways. We retrieved **104 rare disease pathways**
(:ref:`Table 7 <useCase1_AMIWP>`). All human pathways are also retrieved from WikiPathways
(:ref:`Table 7 <useCase1_AMIWP>`). We use these pathways to create background gene sets used for statistical analysis.

.. _useCase1_AMIWP:
.. table:: - Pathways retrieval from WikiPathways
    :align: center

    +------------------------+-----------------+------------------+------------------+
    |                        | Pathways number | Min genes number | Max genes number |
    +========================+=================+==================+==================+
    | Rare Disease Pathways  |       104       |         3        |        436       |
    +------------------------+-----------------+------------------+------------------+
    | All Human WikiPathways |      1,281      |         1        |        484       |
    +------------------------+-----------------+------------------+------------------+

PPI network information
~~~~~~~~~~~~~~~~~~~~~~~~~~

The PPI network is automatically downloaded from |NDExPPI|_. It was build from 3 datasets: Lit-BM, Hi-Union and APID. It
contains 15,390 nodes and 131,087 edges.

.. cssclass:: italic

    For more details about the PPI network, see :ref:`PPInet` section.

AMI results
~~~~~~~~~~~~~~

DOMINO defines vitamin A target genes as active genes and searches active modules enriched in active genes. Over the
2,143 target genes retrieved from CTD, 1,937 are found in the PPI and used as active genes by DOMINO. DOMINO identified
**12 active modules** enriched in vitamin A target genes (:ref:`Table 8 <useCase1_AMIResults>`).

.. _useCase1_AMIResults:
.. table:: - Composition of the active modules identified enriched in vitamin A target genes by DOMINO
    :align: center
    :widths: 60 25 25

    +--------------+------------+------------+
    |              | Min number | Max number |
    +==============+============+============+
    |     Edges    |     20     |     357    |
    +--------------+------------+------------+
    |     Nodes    |     17     |     93     |
    +--------------+------------+------------+
    | Target genes |      8     |     35     |
    +--------------+------------+------------+

.. cssclass:: italic

    See ``DOMINO_D014801_activeModulesNetworkMetrics.txt`` file for more details.

Overlap analysis results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Then, we perform an Overlap analysis between identified active modules (12) and rare disease pathways (104). We obtained
significant overlap between **6 active modules** and **19 rare disease pathways** (pAdjusted <= 0.05). The top 5 is
presented in :ref:`Table 9 <useCase1_AMIOverlap>`.

.. _useCase1_AMIOverlap:
.. table:: - Top 5 of the significant overlaps between identified active modules and rare disease pathways
    :align: center

    +------------+--------------------------------------------------------------------+----------+
    | Pathway IDs| Pathway Names                                                      | pAdjusted|
    +============+====================================================================+==========+
    | WP5087     | Malignant pleural mesothelioma                                     | 2.78e-25 |
    +------------+--------------------------------------------------------------------+----------+
    | WP4541     | Hippo-Merlin signaling dysregulation                               | 4.37e-07 |
    +------------+--------------------------------------------------------------------+----------+
    | WP4577     | Neurodegeneration with brain iron accumulation (NBIA) subtypes ... | 2.84e-06 |
    +------------+--------------------------------------------------------------------+----------+
    | WP5053     | Development of ureteric collection system                          | 1.23e-05 |
    +------------+--------------------------------------------------------------------+----------+
    | WP4540     | Hippo signaling regulation pathways                                | 1.55e-05 |
    +------------+--------------------------------------------------------------------+----------+

Duplicates between active modules results are removed and we keep the more significant ones.

.. cssclass:: italic

    See ``DOMINO_D014801_signOverlap.txt`` file for more details.

Visualisation of AMI results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We created a visualisation of AMI results (:numref:`useCase1_AMIFig`) using Cytoscape [6]_.

We found a significant overlap between **6 active modules** and **19 rare disease pathways**. For sake of visualisation,
we selected only three of them (:numref:`useCase1_AMIFig`). You can find the entire visualisation in the cytoscape
project called ``AMI_visualisation.cys`` in GitHub_.

.. _useCase1_AMIFig:
.. figure:: ../../pictures/UseCase1/UseCase1_AMI.png
   :alt: useCase1_AMIFig
   :align: center
   :scale: 45

   : Visualisation of 3 active modules and their associated rare disease pathways

    Genes are represented by nodes. Grey nodes are the target genes, white nodes are non-target genes. Overlap results
    between active modules and rare disease pathways are displayed using donuts color around nodes. Each color
    corresponds to a rare disease pathways. Creation steps are explained in the :ref:`cytoscape_AMI` section.

Module topology is different between modules and associated rare diseases pathways also vary (:numref:`useCase1_AMIFig`).
For instance, the module on the right is very connected and contains genes that are involved in a lot of rare disease
pathways. Genes, such as *PTEN*, are part of at least 5 pathways. The two other modules are sparser. The module in the
middle contains genes involved only in *Development of ureteric collection system*.

.. _useCase1_RWR:

Random Walk with Restart (RWR)
=================================

The Random Walk with Restart (RWR) approach mesures **proximities** between vitamin A target genes and rare disease
pathways. To calculate these proximities (RWR scores), we used multiXrank [7]_ and multilayer networks. See
:doc:`../approaches/methods_RWR` page for more details.

The multilayer network is composed of three gene networks and one rare disease pathways network. Genes nodes are
connected to disease nodes if they are involved in. See :doc:`../network/NetworkUsed` page for more details.

Running RWR with data retrieved automatically from databases
----------------------------------------------------------------

The **chemicalsFile.csv** file [:ref:`FORMAT <chemicalsFile>`] contains the MeSH ID of vitamin A (D014801). We retrieved
from CTD, genes targeted by the vitamin A and its descendant chemicals (``--directAssociation FALSE``). We keep only
vitamin A - gene interactions which have at least two associated publications (``--nbPub 2``).

multiXrank needs as input a configuration file (``--configPath``) that contains path of networks and analysis parameters.
We used multiXrank with default parameters.

We provide a name file to save vitamin A target genes (i.e. seeds) ``--seedsFile useCases/InputData/seeds.txt`` and
also a SIF file name (``--sifFileName``) to save the top nodes based on RWR scores (``--top 20``).

Results files are saved into ``useCases/OutputResults_useCase1/`` folder.

.. code-block:: bash

    odamnet multixrank  --chemicalsFile useCases/InputData/chemicalsFile.csv \
                        --directAssociation FALSE \
                        --nbPub 2 \
                        --configPath useCases/InputData/config_minimal_useCase1.yml \
                        --networksPath useCases/InputData/ \
                        --seedsFile useCases/InputData/seeds.txt \
                        --sifFileName UseCase1_RWR_network.sif \
                        --top 20 \
                        --outputPath useCases/OutputResults_useCase1/

.. tip::

    | - Downloading of multiplex network from NDEx: :doc:`../network/NetworkUsed` + :doc:`../network/NetworkDownloading`
    | - Creation of the rare disease pathways network: :doc:`../network/NetworkUsed` +  :doc:`../network/NetworkCreation`
    | - Configuration file explanation and example: :ref:`configFile` section


Several files are generated:

- ``CTD_request_D014801_2022_09_07.tsv`` and ``CTD_requestFiltered_D014801_2022_09_07.tsv``:
  the first file contains **results from CTD** query and the second one contains the filtered by publication number.

- ``RWR_D014801/`` folder with the RWR results:

    - ``config_minimal_useCase1.yml`` and ``seeds.txt``: copies of the input files

    - ``multiplex_1.tsv`` and ``multiplex_2.tsv``: RWR scores for each multilayer. 1 is the genes multilayer network RWR
      scores and 2 is the rare disease pathways network RWR scores.

    - ``UseCase1_RWR_network.sif``: SIF file name that contains the network result

    - ``RWR_topX.txt``: Top X of rare disease pathways

.. cssclass:: italic

    For more details about these files, see :ref:`queryOutput` and :ref:`RWROutput` sections.

Results of RWR with data retrieved automatically from databases
-----------------------------------------------------------------

*Queries made on September 7th, 2022*

CTD query results
~~~~~~~~~~~~~~~~~~~~~~~~

We retrieved 7,765 genes targeted by 10 chemicals (vitamin A + nine descendant chemicals) in CTD
(:ref:`Table 10 <useCase1_RWRCTD>`). Chemical - gene associations are kept if they have at least two publications for
human. After filtering, we have **2,143 vitamin A target genes** for 7 chemicals (vitamin A + its descendant molecules).

.. _useCase1_RWRCTD:
.. table:: - Vitamin A target genes retrieved from CTD
    :align: center

    +----------------------------------+---------------------+-----------------+
    |                                  | Number of chemicals | Number of genes |
    +==================================+=====================+=================+
    |          Request result          |          10         |      7,765      |
    +----------------------------------+---------------------+-----------------+
    | After filtering by papers number |          7          |      2,143      |
    +----------------------------------+---------------------+-----------------+

RWR results
~~~~~~~~~~~~~~

Analysis with rare disease pathways network
"""""""""""""""""""""""""""""""""""""""""""""

We used a multilayer network composed of **three gene networks** and one **rare disease pathways network**
(:numref:`multilayerCompo` - left, :ref:`genesMultilayerNet` and
:ref:`Rare disease pathways network<pathwaysOfInterestNet>`).

multiXrank defines vitamin A target genes as seeds. Over the 2,143 target genes retrieved from CTD, 2,012 are found in
the multilayer and used as seeds. Using the RWR scores (i.e. proximity score with the target genes), rare disease
pathways are prioritized. We selected the **top 20** and presented the top 5 (:ref:`Table 11 <useCase1_RWRWP>`).

.. _useCase1_RWRWP:
.. table:: - Rare disease pathways prioritization using RWR score. The top 5 is displayed.
    :align: center
    :widths: 25 50 25

    +---------------------+------------------------------------------+--------------+
    | Nodes (pathway IDs) | Pathway Names                            |  RWR scores  |
    +=====================+==========================================+==============+
    | WP5087              | Malignant pleural mesothelioma           | 2.85e-03     |
    +---------------------+------------------------------------------+--------------+
    | WP4673              | Male infertility                         | 9.02e-04     |
    +---------------------+------------------------------------------+--------------+
    | WP2059              | Alzheimer's disease and miRNA effects    | 7.76e-04     |
    +---------------------+------------------------------------------+--------------+
    | WP5124              | Alzheimer's disease                      | 7.76e-04     |
    +---------------------+------------------------------------------+--------------+
    | WP4298              | Acute viral myocarditis                  | 0.000731     |
    +---------------------+------------------------------------------+--------------+

We created a visualisation of the results (:numref:`useCase1_RWRWPFig`) using Cytoscape [6]_. You can retrieved it in the
cytoscape project called ``RWR_visualisation.cys`` in GitHub_. The :numref:`useCase1_RWRWPFig` presents the top 5 of rare
disease pathways, ordered by RWR score.

.. _useCase1_RWRWPFig:
.. figure:: ../../pictures/UseCase1/UseCase1_RWR_top5.png
   :alt: useCase1_RWRWPFig
   :align: center
   :scale: 70

   : Top 5 of the rare disease pathways prioritized using RWR score using a (disconnected) rare disease pathways network

    Rare disease pathways are in pink triangles. Target genes are in grey and non-target genes are in white. Creation
    steps are explained in the :ref:`cytoscape_RWR` section.

Extra : analysis with disease-disease similarity network
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

.. tip::

    :octicon:`alert;1.5em` Same command line, but needs to change **configuration file**.

We also propose to run an RWR approach using a **disease-disease similarity network**. In this network, rare diseases are
linked together according their **phenotype similarity** whereas in the previous network they were not at all connected.

We used a multilayer network composed of three genes network and one disease-disease similarity network
(:numref:`multilayerCompo` - right, :ref:`genesMultilayerNet`, :ref:`similarityNet`).

multiXrank defines vitamin A target genes as seeds. Over the 2,143 target genes retrieved from CTD, 2,012 are found in
the multilayer and used as seeds. Using the RWR scores (i.e. proximity score with the target genes), rare disease are
prioritized. We selected the **top 20** and presented the top 5 (:ref:`Table 12 <useCase1_RWRSim>`).

.. _useCase1_RWRSim:
.. table:: - Rare disease prioritization using RWR score. The top 5 is displayed.
    :align: center
    :widths: 25 50 25

    +---------------------+-----------------------------------------+------------+
    | Nodes (disease IDs) | Disease Names                           | RWR scores |
    +=====================+=========================================+============+
    | OMIM:601626         | Leukemia, acute myeloid                 | 1.68e-04   |
    +---------------------+-----------------------------------------+------------+
    | OMIM:114500         | Colorectal cancer                       | 1.61e-04   |
    +---------------------+-----------------------------------------+------------+
    | OMIM:125853         | Diabetes mellitus, noninsulin-dependent | 1.60e-04   |
    +---------------------+-----------------------------------------+------------+
    | OMIM:114480         | Breast cancer                           | 1.20e-04   |
    +---------------------+-----------------------------------------+------------+
    | OMIM:211980         | Lung cancer, susceptibility to          | 1.16e-04   |
    +---------------------+-----------------------------------------+------------+

We created a visualisation of the results (:numref:`useCase1_RWRSimFig`) using Cytoscape [6]_. You can retrieved it in
the cytoscape project called ``RWR_visualisation.cys`` in GitHub_. The :numref:`useCase1_RWRSimFig` presents the
top 5 of rare disease pathways, ordered by RWR score.

.. _useCase1_RWRSimFig:
.. figure:: ../../pictures/UseCase1/UseCase1_RWR_top5_sim.png
   :alt: useCase1_RWRSimFig
   :align: center
   :scale: 70

   : Top 5 of the rare disease prioritized using RWR score using disease-disease similarity network

    Rare disease are in pink triangles. Target genes are in grey and non-target genes are in white. Creation
    steps are explained in the :ref:`cytoscape_RWR` section.

Overlap, AMI and RWR results comparison
===========================================

We compare results obtained with the three different approaches: Overlap analysis, Active Module Identification (AMI)
and Random Walk with Restart (RWR). We used **orsum** [8]_, a Python package to filter and integrate enrichment analysis
from several analyses. The main result is a heatmap, presented in :numref:`useCase1_orsum`.

.. code-block:: bash

    orsum.py --gmt 00_Data/WP_RareDiseases_request_2022_09_07.gmt \
             --files 00_Data/Overlap_D014801.4Orsum 00_Data/DOMINO_D014801.4Orsum 00_Data/RWR_D014801.4Orsum \
             --fileAliases Overlap AMI RWR \
             --maxRepSize 0 \
             --outputFolder UseCase1_D014801_orsum

.. _useCase1_orsum:
.. figure:: ../../pictures/UseCase1/UseCase1_orsum.png
   :alt: useCase1_orsum
   :align: center
   :scale: 50

   : Overlap analysis (Overlap), Active module identification (AMI) and Random walk with restart (RWR) results integration and comparison using orsum

The ``--maxRepSize`` parameter is set to 0 to consider each term as is own representative term.

Some rare disease pathways are retrieved associated with vitamin A by all the three approaches such as
*Malignant pleural mesothelioma* or *Acute viral myocarditis*. Some other rare disease pathways are retrieved associated
with vitamin A only by one (*NBIA subtypes pathway*) or two (*Male infertility*) approaches.

References
============
.. [1] Ozisik O, Ehrhart F, Evelo C *et al.*. Overlap of vitamin A and vitamin D target genes with CAKUT-related processes. F1000Research. 2021.
.. [2] Davis AP, Grondin CJ, Johnson RJ *et al.*. The Comparative Toxicogenomics Database: update 2021. Nucleic acids research. 2021.
.. [3] Martens M, Ammar A, Riutta A *et al.*. WikiPathways: connecting communities. Nucleic acids research. 2021.
.. [4] Pratt D, Chen J, Welker *et al.*. NDEx, the Network Data Exchange. Cell Systems. 2015.
.. [5] Levi H, Rahmanian N, Elkon R *et al.*. The DOMINO web-server for active module identification analysis. Bioinformatics. 2022.
.. [6] Shannon P, Markiel A, Ozier O *et al.*. Cytoscape: a software environment for integrated models of biomolecular interaction networks. Genome research. 2003.
.. [7] Baptista A, Gonzalez A & Baudot A. Universal multilayer network exploration by random walk with restart. Communications Physics. 2022.
.. [8] Ozisik O, Térézol M & Baudot A. orsum: a Python package for filtering and comparing enrichment analyses using a simple principle. BMC bioinformatics. 2022.

.. _input: https://github.com/MOohTus/ODAMNet/tree/main/useCases/InputData
.. |input| replace:: Input data
.. _output: https://github.com/MOohTus/ODAMNet/tree/main/useCases/OutputResults_useCase1
.. |output| replace:: Output results data
.. _ctd: http://ctdbase.org/
.. |ctd| replace:: **the Comparative Toxicogenomics Database**
.. _wp: https://www.wikipathways.org/
.. |wp| replace:: **WikiPathways**
.. _ndex: https://www.ndexbio.org/
.. |ndex| replace:: **the Network Data Exchange**
.. _NDExPPI: https://www.ndexbio.org/viewer/networks/bfac0486-cefe-11ed-a79c-005056ae23aa
.. |NDExPPI| replace:: NDEx
.. _GitHub: https://github.com/MOohTus/ODAMNet/tree/main/useCases/
