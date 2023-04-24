.. _usecase1:

============================================================
Use-case 1: data are retrieved automatically with requests
============================================================

.. note::

    This analysis is inspired by the study carried out by Ozisik *et al.,* [1]_.

In this use-case, we want to study the molecular relationship between **vitamin A** and **rare diseases**.

Vitamin A **target genes** are retrieved **directly** from the |ctd|_ [2]_ (CTD).
**Rare disease pathways** are retrieved from |wp|_ [3]_.

This section presents you how to apply the three different approaches proposed.

.. _useCase1_overlap:

Overlap analysis
=====================

The Overlap analysis searches interesting genes between vitamin A target genes and genes involved in rare disease
pathways (see :doc:`../approaches/methods_overlap` section for more details).

Running Overlap analysis with data retrieved automatically from databases
----------------------------------------------------------------------------

The **chemicalsFile.csv** file [:ref:`FORMAT <chemicalsFile>`] contains the MeSH ID of vitamin A (D014801). We retrieved
from CTD, genes targeted by the vitamin A and its descendant chemicals (``--directAssociation FALSE``). We keep only
vitamin A - gene interactions which have at least two associated publications (``--nbPub 2``).

Results files are saved into ``useCases/OutputResults_useCase1/`` folder.

.. code-block:: bash

        odamnet overlap --chemicalsFile useCases/InputData/chemicalsFile.csv \
                        --directAssociation FALSE \
                        --nbPub 2 \
                        --outputPath useCases/OutputResults_useCase1/

Several files are generated:

- ``CTD_request_D014801_2022_09_07.tsv`` and ``CTD_requestFiltered_D014801_2022_09_07.tsv``:
  the first file contains **results from CTD** request and the second one contains the results filtered using the
  publication number.

- ``WP_RareDiseases_request_2022_09_07.gmt`` and ``WP_allPathways_request_2022_09_07.gmt``:
  the first file contains **human rare disease pathways** and the second file contains **all human pathways** retrieved
  in WikiPathways.

- ``Overlap_D014801_withRDWP.csv``: results of the Overlap analysis between vitamin A target genes and rare disease
  pathways.

.. cssclass:: italic

    For more details about these files, see the :doc:`../formats/Output` page.

Results of overlap analysis with data retrieved automatically from databases
-------------------------------------------------------------------------------

*Requests made on September 7th, 2022*

CTD request results
~~~~~~~~~~~~~~~~~~~~~

We retrieved 7,765 genes targeted by 10 chemicals (vitamin A + nine descendant chemicals) in CTD
(:ref:`Table 2 <useCase1OverlapCTD>`). Chemical - gene associations are kept if they have at least two publications for
human. After filtering, we have 2,143 vitamin A target genes for 7 chemicals (vitamin A + its descendant molecules).

.. _useCase1OverlapCTD:
.. table:: Vitamin A target genes retrieved from CTD
    :align: center

    +---------------------------------------------------+---------------------+------------------------+
    |                                                   | Number of chemicals | Number of target genes |
    +===================================================+=====================+========================+
    |          Request result                           |          10         |      7,765             |
    +---------------------------------------------------+---------------------+------------------------+
    | After filtering by associated publications number |          7          |      2,143             |
    +---------------------------------------------------+---------------------+------------------------+

WikiPathways request results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All human pathways labeled as "rare disease" are retrieved from WikiPathways. We retrieved 104 rare disease pathways
(:ref:`Table 3 <useCase1OverlapWP>`). All human pathways are also retrieved from WikiPathways
(:ref:`Table 3 <useCase1OverlapWP>`). We use these pathways to create background gene sets that are used for statistical
analysis.

.. _useCase1OverlapWP:
.. table:: Pathways retrieval from WikiPathways
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
:ref:`Table 4 <useCase1OverlapTop5>`.

.. _useCase1OverlapTop5:
.. table:: Top 5 of the significant overlaps between the vitamin A target genes and rare disease pathways
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

In a previous analysis [1]_, significant overlaps were identified between 4 CAKUT pathways and vitamin A target genes.
With updated target genes data proposed here, we also retrieved significant overlap for 3 of these 4 CAKUT pathways
(:ref:`Table 5 <useCase1OverlapCAKUT>`).

.. _useCase1OverlapCAKUT:
.. table:: Overlap analysis results between vitamin A target genes and CAKUT pathways
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
It can be explained by the fact that one of the two missing genes is not related to human. So it cannot be retrieved by
the request. And the other gene has only one publication that relates association with vitamin A. So it is not kept
during filtering.

.. _useCase1_AMI:

Active Module Identification (AMI)
======================================

The Active Module Identification (AMI) approach identifies active module that contains high number of vitamin A target
genes using a Protein-Protein interaction (PPI) network. AMI is performed using DOMINO [4]_. Then, an Overlap analysis
is applied between identified active modules and rare disease pathways. See see :doc:`../approaches/methods_AMI`
section for more details.

Running Active Module Identification with data retrieved automatically from databases
-----------------------------------------------------------------------------------------

.. warning::

   :octicon:`alert;2em` Results of DOMINO cannot be reproduced when using the DOMINO's server. Indeed, DOMINO server
    doesn't allow to set the random seed. This random seed is changed every new analysis.

The **chemicalsFile.csv** file [:ref:`FORMAT <chemicalsFile>`] contains the MeSH ID of vitamin A (D014801). We retrieved
from CTD, genes targeted by the vitamin A and its descendant chemicals (``--directAssociation FALSE``). We keep only
vitamin A - gene interactions which have at least two associated publications (``--nbPub 2``).

We download automatically a PPI network [:ref:`FORMAT <SIF>`] from NDEx [5]_ using the ``--netUUID`` parameter
(UUID bfac0486-cefe-11ed-a79c-005056ae23aa, version 1.0). We named the PPI network `PPI_HiUnion_LitBM_APID_gene_names_190123.tsv`
(``--networkFile``).

Results files are saved into ``useCases/OutputResults_useCase1/`` folder.

.. code-block:: bash

        odamnet domino  --chemicalsFile useCases/InputData/chemicalsFiles.csv \
                        --directAssociation FALSE \
                        --nbPub 2 \
                        --networkFile useCases/InputData/PPI_HiUnion_LitBM_APID_gene_names_190123.tsv \
                        --netUUID bfac0486-cefe-11ed-a79c-005056ae23aa \
                        --outputPath useCases/OutputResults_useCase1


Several files are generated:

- ``CTD_request_D014801_2022_09_07.tsv`` and ``CTD_requestFiltered_D014801_2022_09_07.tsv``:
  the first file contains **results from CTD** request and the second one contains the results filtered using the
  publication number.

- ``WP_RareDiseases_request_2022_09_07.gmt`` and ``WP_allPathways_request_2022_09_07.gmt``:
  the first file contains **human rare disease pathways** and the second file contains **all human pathways** retrieved
  in WikiPathways.

- ``DOMINO_inputGeneList_D014801.txt``: vitamin A target genes list used for the active module identification.

- ``Overlap_AM_*_D014801_withRDWP.csv``: results of the Overlap analysis between identified active modules genes and
  rare disease pathways. There is one file per active module.

- ``DOMINO_D014801_activeModulesNetwork.txt``, ``DOMINO_D014801_overlapAMresults4Cytoscape.txt``, ``DOMINO_D014801_activeModules.txt``
  , ``DOMINO_D014801_activeModulesNetworkMetrics.txt`` and ``DOMINO_D014801_signOverlap.txt``: some statistics are
  calculated and saved into files. Theses files are useful for visualisation.

.. cssclass:: italic

    For more details about these files, see :doc:`../formats/Output` page (:ref:`requestOutput`, :ref:`overlapOutput`,
    :ref:`AMIOutput`)

Results of Active Module identification with data retrieved automatically from databases
-------------------------------------------------------------------------------------------

*Requests made on September 7th, 2022*

CTD request results
~~~~~~~~~~~~~~~~~~~~~

We retrieved 7,765 genes targeted by 10 chemicals (vitamin A + nine descendant chemicals) in CTD
(:ref:`Table 6 <useCase1AMICTD>`). Chemical - gene associations are kept if they have at least two publications for
human. After filtering, we have 2,143 vitamin A target genes for 7 chemicals (vitamin A + its descendant molecules).

.. _useCase1AMICTD:
.. table:: Vitamin A target genes retrieved from CTD
    :align: center

    +---------------------------------------+---------------------+-----------------+
    |                                       | Number of chemicals | Number of genes |
    +=======================================+=====================+=================+
    |          Request result               |          10         |      7,765      |
    +---------------------------------------+---------------------+-----------------+
    | After filtering by publication number |          7          |      2,143      |
    +---------------------------------------+---------------------+-----------------+

WikiPathways request results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All human pathways labeled as "rare disease" are retrieved from WikiPathways. We retrieved 104 rare disease pathways
(:ref:`Table 7 <useCase1AMIWP>`). All human pathways are also retrieved from WikiPathways (:ref:`Table 7 <useCase1AMIWP>`).
We use these pathways to create background gene sets that are used for statistical analysis.

.. _useCase1AMIWP:
.. table:: Pathways retrieval from WikiPathways
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

The PPI network is automatically downloaded from NDEx_. It was build from 3 datasets: Lit-BM, Hi-Union and APID. It
contains 15,390 nodes and 131,087 edges.

[METTRE UNE REF SUR PLUS D'EXPLICATION ?]

Active Modules Identification results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

DOMINO defines vitamin A target genes as active genes and searches active modules enriched in active genes. Over the
2,143 target genes retrieved from CTD, 1,937 are found in the PPI and used as active genes by DOMINO. DOMINO identified
**12 active modules** enriched in vitamin A target genes (:ref:`Table 8 <useCase1AMIResults>`).

.. _useCase1AMIResults:
.. table:: Composition of the active modules identified enriched in vitamin A target genes by DOMINO
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

.. cssclass:: italic

    See ``DOMINO_D014801_activeModulesNetworkMetrics.txt`` file for more details.

Overlap analysis results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Then, we perform an Overlap analysis between identified active modules (12) and rare disease pathways (104). We obtained
significant overlap between **6 active modules** and **19 rare disease pathways** (pAdjusted <= 0.05). The top 5 is
presented in :ref:`Table 9 <useCase1AMIOverlap>`.

.. _useCase1AMIOverlap:
.. table:: Top 5 of the significant overlaps between identified active modules and rare disease pathways
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

Visualisation of active module identification results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We created a visualisation of active module identification results (:numref:`dominoUsage1Fig`) using Cytoscape [5]_.

We found a significant overlap between **6 active modules** and **19 rare disease pathways**. For sake of visualisation,
we selected only three of them (:numref:`dominoUsage1Fig`). You can find the entire visualisation in the cytoscape
project called ``AMI_visualisation.cys`` in GitHub_.

.. _dominoUsage1Fig:
.. figure:: ../../pictures/UseCase1/UseCase1_AMI.png
   :alt: usecase1 AMI
   :align: center

   : Visualisation of 3 active modules and their associated rare disease pathways

    Genes are represented by nodes. Grey nodes are the target genes, white nodes are non-target genes. Overlap results
    between active modules and rare disease pathways as displayed using donuts color around nodes. Each color
    corresponds to a rare disease.
    Creation steps are explained in the :ref:`networkAMI` section.

Module topology is different between modules and associated rare diseases pathways also vary (:numref:`dominoUsage1Fig`).
For instance, the module on the right is very connected and contains genes that are involved in a lot of rare disease
pathways. Genes, such as PTEN, are part of at least 5 pathways. The two other modules are sparser. The module in the
middle contains genes involved only in *Development of ureteric collection system*.

.. _useCase1_RWR:

Random Walk with Restart (RWR)
=================================

The Random Walk with Restart approach mesures proximities between vitamin A target genes and rare disease pathways. To
calculate these proximities (RWR scores), we used multiXrank [6]_ and multilayer networks. The multilayer network is
composed of three gene networks and one rare disease pathways network. Genes nodes are connected to disease nodes if
they are involved in.

.. cssclass:: italic

    For more details about RWR, multiXrank and multilayer network see :doc:`../approaches/methods_RWR`.

Running Random Walk analysis with data retrieved automatically from databases
--------------------------------------------------------------------------------

The **chemicalsFile.csv** file [:ref:`FORMAT <chemicalsFile>`] contains the MeSH ID of vitamin A (D014801). We retrieved
from CTD, genes targeted by the vitamin A and its descendant chemicals (``--directAssociation FALSE``). We keep only
vitamin A - gene interactions which have at least two associated publications (``--nbPub 2``).

MultiXrank needs as input a configuration file (``--configPath``) that contains path of networks and analysis parameters.
We used multiXrank with default parameters.

We provided a name file to store vitamin A target genes (i.e. seeds) ``--seedsFile examples/InputData/seeds.txt`` and
also a SIF file name (``--sifFileName``) to save the top nodes based on RWR score (``--top 20``).

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

    | - Multiplex network is downloaded directly from NDEx (:ref:`ICI`)
    | - Creation of the rare disease pathways network (:ref:`pathwaysOfInterestNet`)
    | - Configuration file explanation and example (:ref:`configFile`)


Several files are generated:

- ``CTD_request_D014801_2022_09_07.tsv`` and ``CTD_requestFiltered_D014801_2022_09_07.tsv``:
  the first file contains **results from CTD** request and the second one contains the filtered by publication number.

- ``RWR_D014801/`` folder with the RWR results:

    - ``config_minimal_useCase1.yml`` and ``seeds.txt``: copies of the input files

    - ``multiplex_1.tsv`` and ``multiplex_2.tsv``: RWR scores for each multilayer. 1 is multiplex network RWR scores
      and 2 is the rare disease pathways network RWR scores.

    - ``UseCase1_RWR_network.sif``: SIF file name that contains the network result

    - ``RWR_top20.txt``: Top 20 of rare disease pathways

.. cssclass:: italic

    For more details about these file, see :doc:`../formats/Output` page.

Results of Random Walk analysis with data retrieved automatically from databases
-----------------------------------------------------------------------------------

*Requests made on September 7th, 2022*

CTD request results
~~~~~~~~~~~~~~~~~~~~~~~~

We retrieved 7,765 genes targeted by 10 chemicals (vitamin A + nine descendant chemicals) in CTD
(:ref:`Table 10 <useCase1RWRCTD>`). Chemical - gene associations are kept if they have at least two publications for
human. After filtering, we have 2,143 vitamin A target genes for 7 chemicals (vitamin A + its descendant molecules).

.. _useCase1RWRCTD:
.. table:: Vitamin A target genes retrieved from CTD
    :align: center

    +----------------------------------+---------------------+-----------------+
    |                                  | Number of chemicals | Number of genes |
    +==================================+=====================+=================+
    |          Request result          |          10         |      7,765      |
    +----------------------------------+---------------------+-----------------+
    | After filtering by papers number |          7          |      2,143      |
    +----------------------------------+---------------------+-----------------+

Random Walk with Restart results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Analysis with rare disease pathways network
"""""""""""""""""""""""""""""""""""""""""""""

We used a multilayer network composed of three genes network and one rare disease pathways network
(:ref:`pathwaysOfInterestNet`).

multiXrank defined vitamin A target genes as seeds. Over the 2,143 target genes retrieved from CTD, 2,012 are found in
the multilayer and used as seeds. Using the RWR scores (i.e. proximity score with the target genes), rare disease
pathways are prioritized. We select the top 20 and present the top 5 (:ref:`Table 11 <useCase1_pathwaysRWR>`).

.. _useCase1_pathwaysRWR:
.. table:: Rare disease prioritization using RWR score. The top 5 is displayed.
    :align: center

    +------------+-----------------------------------------------------+--------------+
    | Node       | Pathway Names                                       |  RWR score   |
    +============+=====================================================+==============+
    | WP5087     | Malignant pleural mesothelioma                      | 2.85e-03     |
    +------------+-----------------------------------------------------+--------------+
    | WP4673     | Male infertility                                    | 9.02e-04     |
    +------------+-----------------------------------------------------+--------------+
    | WP2059     | Alzheimer's disease and miRNA effects               | 7.76e-04     |
    +------------+-----------------------------------------------------+--------------+
    | WP5124     | Alzheimer's disease                                 | 7.76e-04     |
    +------------+-----------------------------------------------------+--------------+
    | WP4298     | Acute viral myocarditis                             | 0.000731     |
    +------------+-----------------------------------------------------+--------------+

We created a visualisation of the results (:numref:`useCase1_pathwaysNetworkRWR`) using Cytoscape [5]_. You can
retrieved the cytoscape project called ``RWR_visualisation.cys`` in GitHub_. The :numref:`useCase1_pathwaysNetworkRWR`
presents the top 5 of rare disease pathways, ordered by RWR score.

.. _useCase1_pathwaysNetworkRWR:
.. figure:: ../../pictures/UseCase1/UseCase1_RWR_top5.png
   :alt: usecase 1 pathwaysNetworkRWR
   :align: center

   : Top 5 of the rare disease pathways prioritized using RWR score using a (disconnected) rare disease pathways network

    Rare disease pathways are in pink triangles. Target genes are in grey and non-target genes are in white.

Extra : analysis with disease-disease similarity network
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

.. tip::

    Same command line, but you need to change configuration file :octicon:`alert;2em`.

We also propose to run an RWR approach using a disease-disease similarity network. In this network, rare diseases are
linked together according their phenotype similarity whereas in the previous network they were not at all connected.

We used a multilayer network composed of three genes network and one disease-disease similarity network (:ref:`ICI`).

multiXrank defined vitamin A target genes as seeds. Over the 2,143 target genes retrieved from CTD, 2,012 are found in
the multilayer and used as seeds. Using the RWR scores (i.e. proximity score with the target genes), rare disease are
prioritized. We select the top 20 and present the top 5 (:ref:`Table 12 <useCase1_diseasesRWR>`).

.. _useCase1_diseasesRWR:
.. table:: Rare disease prioritization using RWR score. The top 5 is displayed.
    :align: center

    +-------------+-----------------------------------------+----------+
    | node        | Disease name                            | score    |
    +=============+=========================================+==========+
    | OMIM:601626 | Leukemia, acute myeloid                 | 1.68e-04 |
    +-------------+-----------------------------------------+----------+
    | OMIM:114500 | Colorectal cancer                       | 1.61e-04 |
    +-------------+-----------------------------------------+----------+
    | OMIM:125853 | Diabetes mellitus, noninsulin-dependent | 1.60e-04 |
    +-------------+-----------------------------------------+----------+
    | OMIM:114480 | Breast cancer                           | 1.20e-04 |
    +-------------+-----------------------------------------+----------+
    | OMIM:211980 | Lung cancer, susceptibility to          | 1.16e-04 |
    +-------------+-----------------------------------------+----------+

We created a visualisation of the results (:numref:`useCase1_simNetworkRWR`) using Cytoscape [5]_. You can retrieved
the cytoscape project called ``RWR_visualisation.cys`` in GitHub_. The :numref:`useCase1_simNetworkRWR` presents the
top 5 of rare disease pathways, ordered by RWR score.

.. _useCase1_simNetworkRWR:
.. figure:: ../../pictures/UseCase1/UseCase1_RWR_top5_sim.png
   :alt: usecase 1 simNetworkRWR
   :align: center

   : Top 5 of the rare disease prioritized using RWR score using disease-disease similarity network

    Rare disease are in pink triangles. Target genes are in grey and non-target genes are in white.

Overlap, AMI and RWR results comparison
===========================================

We compare results obtained with the three different approaches: Overlap analysis, Active Module Identification (AMI)
and Random Walk with Restart (RWR). We used orsum [4]_, a Python package to filter and integrate enrichment analysis
from several analyses. The main result is a heatmap, presented in :numref:`useCase1_orsum`.

.. code-block:: bash

    orsum.py --gmt 00_Data/WP_RareDiseases_request_2022_09_07.gmt \
             --files 00_Data/Overlap_D014801.4Orsum 00_Data/DOMINO_D014801.4Orsum 00_Data/RWR_D014801.4Orsum
             --fileAliases Overlap AMI RWR \
             --maxRepSize 0 \
             --outputFolder UseCase1_D014801_orsum

.. _useCase1_orsum:
.. figure:: ../../pictures/UseCase1/UseCase1_orsum.png
   :alt: usecase1 orsum
   :align: center

   : Overlap, AMI and RWR results integration and comparison using orsum

The ``--maxRepSize`` parameter is set to 0 to consider each term as is own representative term.

Some rare disease pathways are retrieved associated with vitamin A by all the three approaches such as
*Malignant pleural mesothelioma* or *Acute viral myocarditis*. Some other rare disease pathways are retrieved associated
with vitamin A only by one (*NBIA subtypes pathway*) or two (*Male infertility*).

References
============
.. [1] Ozisik, O., Ehrhart, F., Evelo, C. T., Mantovani, A., & Baudot, A. (2021). Overlap of vitamin A and vitamin D target genes with CAKUT-related processes. F1000Research, 10.
.. [2] Davis AP, Grondin CJ, Johnson RJ, Sciaky D, Wiegers J, Wiegers TC, Mattingly CJ The Comparative Toxicogenomics Database: update 2021. Nucleic Acids Res. 2021.
.. [3] Martens, M., Ammar, A., Riutta, A., Waagmeester, A., Slenter, D. N., Hanspers, K., ... & Kutmon, M. (2021). WikiPathways: connecting communities. Nucleic acids research, 49(D1), D613-D621.
.. [4] Levi, H., Rahmanian, N., Elkon, R., & Shamir, R. (2022). The DOMINO web-server for active module identification analysis. Bioinformatics, 38(8), 2364-2366.
.. [5] Shannon, P., Markiel, A., Ozier, O., Baliga, N. S., Wang, J. T., Ramage, D., ... & Ideker, T. (2003). Cytoscape: a software environment for integrated models of biomolecular interaction networks. Genome research, 13(11), 2498-2504.
.. [6] Baptista, A., Gonzalez, A., & Baudot, A. (2022). Universal multilayer network exploration by random walk with restart. Communications Physics, 5(1), 1-9.

.. [9] Ozisik, O., Térézol, M., & Baudot, A. (2022). orsum: a Python package for filtering and comparing enrichment analyses using a simple principle. BMC bioinformatics, 23(1), 1-12.


.. _ctd: http://ctdbase.org/
.. |ctd| replace:: **the Comparative Toxicogenomics Database**
.. _wp: https://www.wikipathways.org/
.. |wp| replace:: **WikiPathways**
.. _NDEx: https://www.ndexbio.org/viewer/networks/bfac0486-cefe-11ed-a79c-005056ae23aa
.. _GitHub: https://github.com/MOohTus/ODAMNet/tree/main/useCases/AMI_visualisation.cys
