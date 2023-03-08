.. _usecase2:

=====================================================
Use-case 2: data are provided by the user
=====================================================

Context
==========

This use-case illustrates how to use ODAMNet with data provided by users.

We use data from Ozisik *et al.*, 2021 [1]_. Results from paper and results found with ODAMNet are compared.

**Vitamin A target genes** are coming from Balmer and Blomhoff [3]_ paper and **pathways/processes** related to CAKUT
are coming from |wiki|_ [4]_, |reac|_ [5]_ and |go|_ (GO) [6]_:sup:`,` [7]_. Input data are available in |git|_.

.. _wiki: https://www.wikipathways.org/
.. |wiki| replace:: WikiPathways
.. _reac: https://reactome.org/
.. |reac| replace:: Reactome
.. _go: http://geneontology.org/
.. |go| replace:: Gene Ontology
.. _git: https://github.com/MOohTus/ODAMNet/tree/main/useCases/InputData
.. |git| replace:: GitHub


Overlap analysis
=====================

This approach calculates the overlap between genes targeted by vitamin A, and the pathways/processes related to CAKUT.

.. cssclass:: italic

    For more details, see :doc:`../approaches/methods_overlap` section.

Running overlap analysis with data provided by users
----------------------------------------------------------

Target genes file is given using the ``--targetGenesFile`` parameter. It contains the list of vitamin A target genes
[:ref:`FORMAT <targetGenesFile>`].

Pathways/processes related to CAKUT are given using the ``--GMT`` parameter [:ref:`FORMAT <pathways>`]. Background genes
of each source of pathways/processes is required (``--backgroundFile`` parameter). The file contains the list of
background files.

Results files are saved into ``useCases/OutputResults_useCase2/`` folder.

.. code-block:: bash

        odamnet overlap --targetGenesFile useCases/InputData/VitA-Balmer2002-Genes.txt \
                        --GMT useCases/InputData/PathwaysOfInterest.gmt \
                        --backgroundFile useCases/InputData/PathwaysOfInterestBackground.txt \
                        --outputPath useCases/OutputResults_useCase2/

``Overlap_genesList_withpathOfInterest.csv`` file is created. It contains results of the overlap analysis between
target genes and CAKUT related pathways/processes.

.. cssclass:: italic

    For more details about this file, see :doc:`../formats/Output` page.

Results of overlap analysis with data provided by users
---------------------------------------------------------

*Request made the 07th of September 2022*

Data provided by users overview
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Target genes are coming from Balmer and Blomhoff [3]_. Pathways of interests are coming from Reactome [5]_ and
WikiPathways [4]_ and processes of interest are coming from Biological Process (GO) [6]_:sup:`,` [7]_.

Details of input data are presented in the :ref:`Table 13 <useCase2DataOverview>`.

.. _useCase2DataOverview:
.. table:: Overview of data provided by users
    :align: center

    +----------------------+--------+
    |                      | Number |
    +======================+========+
    |     Target genes     |   521  |
    +----------------------+--------+
    | Pathways of interest |   12   |
    +----------------------+--------+
    |        Sources       |    3   |
    +----------------------+--------+

Overlap analysis results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ODAMNet found significant overlap between target genes and ``8 pathways/processes`` related to CAKUT disease (pAdjusted <= 0.05).
Results are presented in the :ref:`Table 14 <useCase2Overlap>`.

.. _useCase2Overlap:
.. table:: Results of overlap analysis between target genes and CAKUT disease
    :align: center

    +-----------------------+----------------------------------------+-----------+------------------+
    |       PathwayIDs      |                  PathwayNames          |  pValue   | IntersectionSize |
    +=======================+========================================+===========+==================+
    |       GO:0072001      |            renal system development    |  6.65e-18 |        43        |
    +-----------------------+----------------------------------------+-----------+------------------+
    |       GO:0001822      |               kidney development       |  7.90e-17 |        41        |
    +-----------------------+----------------------------------------+-----------+------------------+
    |       GO:0060993      |              kidney morphogenesis      |  1.92e-12 |        20        |
    +-----------------------+----------------------------------------+-----------+------------------+
    |       WP:WP5053       | Development of ureteric collection ... | 2.278e-08 |        15        |
    +-----------------------+----------------------------------------+-----------+------------------+
    |       WP:WP4823       |     Genes controlling nephrogenesis    |  1.11e-04 |        10        |
    +-----------------------+----------------------------------------+-----------+------------------+
    | PMC5748921-PMC6115658 |               CAKUT causal genes       | 1.06e-03  |         6        |
    +-----------------------+----------------------------------------+-----------+------------------+
    |       WP:WP4830       |            GDNF/RET signalling axis    | 8.30e-03  |         5        |
    +-----------------------+----------------------------------------+-----------+------------------+
    |   REAC:R-HSA-2022377  | Metabolism of Angiotensinogen to ...   |     0.04  |         3        |
    +-----------------------+----------------------------------------+-----------+------------------+

Ozisik *et al.,* [1]_ identified 7 pathways/processes related to CAKUT disease over 12. ODAMNet found these 7
pathways/processes and another one (REAC:R-HSA-2022377).

.. _useCase2_AMI:

Active Modules Identification (AMI)
====================================

ODAMNet identifies active modules using a protein-protein interaction (PPI) network with DOMINO [8]_. Then, it performs
an overlap analysis between each identified active module and pathways/processes related to CAKUT.

.. cssclass:: italic

    For more detail, see :doc:`../approaches/methods_AMI` section.

Running active modules identification with data provided by users
-------------------------------------------------------------------

As before, users provide target genes (``--targetGenesFile``) and pathways/processes of interest
(``--GMT`` and ``--backgroundFile`` - [:ref:`FORMAT <pathways>`]).

We will identify active modules using a protein-protein interaction (PPI) network named ``PPI_network_2016.sif`` [:ref:`FORMAT <SIF>`].

Results files are saved into ``useCases/OutputResults_useCase2/`` folder.

.. code-block:: bash

        odamnet domino  --targetGenesFile useCases/InputData/VitA-Balmer2002-Genes.txt \
                                --GMT useCases/InputData/PathwaysOfInterest.gmt \
                                --backgroundFile useCases/InputData/PathwaysOfInterestBackground.txt \
                                --networkFile useCases/InputData/PPI_network_2016.sif \
                                --outputPath useCases/OutputResults_useCase2

Several files are generated :

- ``DOMINO_inputGeneList_D014801.txt``: genes targeted by vitamin A, used for the active module identification.

- ``Overlap_AM_*_genesList_withpathOfInterest.csv``: results of the overlap analysis between target genes and pathways/processes of
  interest provided by the user. One file per active module.

- ``DOMINO_genesList_activeModulesNetwork.txt``, ``DOMINO_genesList_overlapAMresults4Cytoscape.txt``, ``DOMINO_genesList_activeModules.txt``
  , ``DOMINO_genesList_activeModulesNetworkMetrics.txt`` and ``DOMINO_genesList_signOverlap.txt``: some statistics are
  calculated and saved into files. Theses files are useful for visualisation.

For more details about these file, see :doc:`../formats/Output` page (:ref:`requestOutput`, :ref:`overlapOutput`, :ref:`AMIOutput`).

Results of active module identification with data provided by users
--------------------------------------------------------------------

*Request made the 07th of September 2022*

Data provided by users description
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Data come from the Ozisik *et al.*, 2021 [1]_ paper. Details of the data are presented in the :ref:`Table 15 <useCase2DataOverviewAMI>`.

.. _useCase2DataOverviewAMI:
.. table:: Input data overview
    :align: center

    +--------------------------------+--------+
    |                                | Number |
    +================================+========+
    |     Target genes               |   521  |
    +--------------------------------+--------+
    | Pathways/processes of interest |   12   |
    +--------------------------------+--------+
    |        Sources                 |    3   |
    +--------------------------------+--------+

Pathways of interests are coming from Reactome and WikiPathways and processes of interest are coming from Biological
Process (Gene Ontology).

Active Modules Identification results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. warning::

   :octicon:`alert;2em` DOMINO [8]_ server doesn't allow to set the random seed. That why, results cannot be reproduced
    identically.

Target genes are defined as **active genes** by DOMINO. We give **521 active genes** as input. DOMINO found
**18 Active Modules** (:ref:`Table 16 <useCase2AMIResults>`).

.. _useCase2AMIResults:
.. table:: Composition of active modules found by DOMINO
    :align: center

    +--------------+------------+------------+
    |              | Min number | Max number |
    +==============+============+============+
    |     Edges    |     5      |     157    |
    +--------------+------------+------------+
    |     Nodes    |     5      |     79     |
    +--------------+------------+------------+
    | Active Genes |     3      |     21     |
    +--------------+------------+------------+

*See DOMINO_genesList_activeModulesNetworkMetrics.txt file for more details.*

Overlap analysis results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Then, we perform an overlap analysis between active modules and pathways/processes of interest. We found **7 pathways/processes**
that are significantly overlapped by **6 active modules** (padjusted <= 0.05).

.. _useCase2AMIOverlap:
.. table:: Overlap analysis between active module and pathways/processes of interest provided by users
    :align: center

    +------------------------+-------------------------------------------+
    | termID                 | termTitle                                 |
    +========================+===========================================+
    | GO:0001822             | kidney development                        |
    +------------------------+-------------------------------------------+
    | GO:0060993             | kidney morphogenesis                      |
    +------------------------+-------------------------------------------+
    | GO:0072001             | renal system development                  |
    +------------------------+-------------------------------------------+
    | **REAC:R-HSA-8853659** | **RET signaling**                         |
    +------------------------+-------------------------------------------+
    | WP:WP4823              | Genes controlling nephrogenesis           |
    +------------------------+-------------------------------------------+
    | WP:WP4830              | GDNF/RET signalling axis                  |
    +------------------------+-------------------------------------------+
    | WP:WP5053              | Development of ureteric collection system |
    +------------------------+-------------------------------------------+

We found a pathway that was not found with the overlap approach (**REAC:R-HSA-8853659**).

Visualisation of active module identification results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We visualised the result using a network representation (:numref:`dominoUsage2Fig`). To know how to create this figure,
see the :ref:`networkAMI` section.

.. _dominoUsage2Fig:
.. figure:: ../../pictures/useCase2_DOMINO_network.png
   :alt: usecase2 AMI
   :align: center

   : Network visualisation of Active modules which are enriched in CAKUT disease pathways/processes

Some network are enriched with the same pathways/processes whereas other contain genes involved in different pathways/processes. Target genes
(i.e. active genes, grey spheres) could be part of pathways/processes as non-target genes (white spheres).

.. _useCase2_RWR:

Random Walk with Restart (RWR)
===============================

The third approach, Random Walk with Restart (RWR), is applied into two different multilayer compositions:

1. Multiplex (PPI + Complex + Reactome) and pathways/processes of interest network connected to genes nodes
2. Multiplex (PPI + Complex + Reactome) and Disease-Disease similarity network linked with a bipartite

*For more details about RWR, see* :doc:`../approaches/methods_RWR`.

Running Random Walk analysis with data provided by users
-----------------------------------------------------------

| To know how to create the pathways/processes of interest network: see :ref:`pathwaysOfInterestNet`.
| To know how to create the disease-disease similarity network: see :ref:`DDnet`.

Whatever the network used, target genes file is provided by users using ``--targetGenesFile`` [:ref:`FORMAT <targetGenesFile>`].

MultiXrank needs a configuration file (``--configPath``) and the networks path (``--networksPath``). We run the analysis with
default parameters.

The target genes are set as seeds for the walk and saved into a file ``--seedsFile examples/InputData/seeds.txt``.
You need to give the SIF file name (``--sifFileName``) to save the network results and the top number of results too
(``--top 10``).

Results files are saved into ``useCases/OutputResults_useCase2/`` folder.

If you need more details about the input format files, see :ref:`GR` and :ref:`configFile` parts.

.. tip::

    Whatever the networks used, the **command line is the same**. But you have to **change** the network name inside the
    **configuration file**.

    .. tabs::

        .. group-tab:: Pathways/processes of interest network

            .. code-block:: bash
                :emphasize-lines: 9,11

                 multiplex:
                     1:
                         layers:
                             - multiplex/1/Complexes_Nov2020.gr
                             - multiplex/1/PPI_Jan2021.gr
                             - multiplex/1/Reactome_Nov2020.gr
                     2:
                         layers:
                             - multiplex/2/pathwaysOfInterestNetwork_fromPaper.sif
                 bipartite:
                     bipartite/Bipartite_pathOfInterest_geneSymbols_fromPaper.tsv:
                         source: 2
                         target: 1
                 seed:
                     seeds.txt

        .. group-tab:: Disease-Disease similarity network

            .. code-block:: bash
               :emphasize-lines: 9,11

                multiplex:
                    1:
                        layers:
                            - multiplex/1/Complexes_Nov2020.gr
                            - multiplex/1/PPI_Jan2021.gr
                            - multiplex/1/Reactome_Nov2020.gr
                    2:
                        layers:
                            - multiplex/2/DiseaseSimilarity_network_2022_06_11.txt
                bipartite:
                    bipartite/Bipartite_genes_to_OMIM_2022_09_27.txt:
                        source: 2
                        target: 1
                seed:
                    seeds.txt


.. code-block:: bash

    odamnet multixrank  --targetGenesFile useCases/InputData/VitA-Balmer2002-Genes.txt \
                                --configPath useCases/InputData/config_minimal_useCase2.yml \
                                --networksPath useCases/InputData/ \
                                --seedsFile useCases/InputData/seeds.txt \
                                --sifFileName resultsNetwork_useCase2.sif \
                                --top 10 \
                                --outputPath useCases/OutputResults_useCase2/

Several files are generated into ``RWR_genesList/`` folder:

    - ``config_minimal_useCase2.yml`` and ``seeds.txt``: copies of the input files

    - ``multiplex_1.tsv`` and ``multiplex_2.tsv``: score for each feature. 1 corresponds to the multiplex and 2 to
      the disease network (depends of the network folder name).

    - ``resultsNetwork_useCase2.sif``: SIF file name that contains the network result

For more details about these file, see :doc:`../formats/Output` page.

Results of Random Walk analysis with data provided by users
-------------------------------------------------------------

We use the default parameters, whatever the networks used. For reminder, we have **521 target genes** provided by users.

Pathways/processes of interest network analysis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*In this part, we present results found for the first multiplex composition: multiplex + pathways/processes of interest.*

First, target genes are used as seed to start the walk: ``483/521`` genes are used.

The gene with the highest score is ``ASMT`` with ``score = 0.0006682735081574565`` (it's a seed). This score helps
us to select a list of pathways/processes. All pathways/processes with a score bigger than this score are extracted and considered as connected
with target genes (i.e. seeds).

According this highest score, **4 pathways/processes** are selected (:ref:`Table 18 <useCase2_pathwaysRWR>`).

.. _useCase2_pathwaysRWR:
.. table:: pathways/processes linked to target genes
    :align: center

    +-----------------------+--------------------------+--------------+
    | node                  | pathway                  | score        |
    +=======================+==========================+==============+
    | GO:0072001            | renal system development | 0.002101     |
    +-----------------------+--------------------------+--------------+
    | GO:0001822            | kidney development       | 0.001847     |
    +-----------------------+--------------------------+--------------+
    | **REAC:R-HSA-195721** | **Signaling by WNT**     | **0.001660** |
    +-----------------------+--------------------------+--------------+
    | **REAC:R-HSA-157118** | **Signaling by NOTCH**   | **0.001140** |
    +-----------------------+--------------------------+--------------+

Two pathways not found with the previous approaches, are link to target genes: ``REAC:R-HSA-195721`` and ``REAC:R-HSA-157118``.
You can visualise the results with a network as shown on the :numref:`useCase2_pathwaysNetworkRWR`.

.. _useCase2_pathwaysNetworkRWR:
.. figure:: ../../pictures/RWR_pathwaysNet_useCase2.png
   :alt: usecase 2 pathwaysNetworkRWR
   :align: center

   : Results from RWR through the molecular multilayer and pathways/processes of interest network

    Pathways/processes of interest are represented by triangle nodes in pink, genes are represented by white nodes and target genes by grey nodes.

Disease-Disease similarity network
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*In this part, we present results found for the second multiplex composition: multiplex + disease-disease network.*

First, target genes are used as seed to start the walk: ``483/521`` genes are used.

We selected the top 10 of diseases (:ref:`Table 19 <useCase2_diseasesRWR>`).

.. _useCase2_diseasesRWR:
.. table:: Diseases linked to target genes
    :align: center

    +-------------+-----------------------------------------+----------+
    | node        | Diseases                                | score    |
    +=============+=========================================+==========+
    | OMIM:178500 | Pulmonary fibrosis, idiopathic          | 0.000334 |
    +-------------+-----------------------------------------+----------+
    | OMIM:125853 | Diabetes mellitus, noninsulin-dependent | 0.000301 |
    +-------------+-----------------------------------------+----------+
    | OMIM:215600 | Cirrhosis, familial                     | 0.000255 |
    +-------------+-----------------------------------------+----------+
    | OMIM:613659 | Gastric cancer, somatic                 | 0.000235 |
    +-------------+-----------------------------------------+----------+
    | OMIM:211980 | Lung cancer, susceptibility to          | 0.000230 |
    +-------------+-----------------------------------------+----------+
    | OMIM:104300 | Alzheimer disease                       | 0.000224 |
    +-------------+-----------------------------------------+----------+
    | OMIM:168600 | Parkinson disease, late-onset           | 0.000192 |
    +-------------+-----------------------------------------+----------+
    | OMIM:601859 | Autoimmune lymphoproliferative syndrome | 0.000182 |
    +-------------+-----------------------------------------+----------+
    | OMIM:601665 | OBESITY                                 | 0.000181 |
    +-------------+-----------------------------------------+----------+
    | OMIM:171300 | PHEOCHROMOCYTOMA                        | 0.000145 |
    +-------------+-----------------------------------------+----------+

You can represent the results with a network as shown in the :numref:`useCase2_simNetworkRWR`.

.. _useCase2_simNetworkRWR:
.. figure:: ../../pictures/RWR_pathwaysNet_useCase2_simNet.png
   :alt: usecase 2 simNetworkRWR
   :align: center

   : Results from RWR through the molecular multilayer and disease-disease similarity network

    Diseases are represented by triangle pink nodes, genes are represented by white nodes and target genes by grey nodes.

Rare disease pathways identified
====================================

Approaches give us a list of CAKUT pathways/processes significantly connected to vitamin A target genes. To easily compare results,
we use orsum [2]_. Results are displayed into a heatmap in the :numref:`useCase2_orsum`.

.. code-block:: bash

    orsum.py    --gmt 00_Data/hsapiens_background.gmt \
                --files Overlap_genesList_withpathOfInterest.4Orsum DOMINO_genesList_signOverlap.4Orsum pathwaysResults.4Orsum \
                --fileAliases Overlap DOMINO multiXrank \
                --outputFolder useCase2Comparison/

.. _useCase2_orsum:
.. figure:: ../../pictures/useCase2_orsum.png
   :alt: usecase2 orsum
   :align: center

   : Comparison of use-case 2 results using orsum

References
============

.. [1] Ozisik, O., Ehrhart, F., Evelo, C. T., Mantovani, A., & Baudot, A. (2021). Overlap of vitamin A and vitamin D target genes with CAKUT-related processes. F1000Research, 10.
.. [2] Davis AP, Grondin CJ, Johnson RJ, Sciaky D, Wiegers J, Wiegers TC, Mattingly CJ The Comparative Toxicogenomics Database: update 2021. Nucleic Acids Res. 2021.
.. [3] Balmer, J. E., & Blomhoff, R. (2002). Gene expression regulation by retinoic acid. Journal of lipid research, 43(11), 1773-1808.
.. [4] Martens, M., Ammar, A., Riutta, A., Waagmeester, A., Slenter, D. N., Hanspers, K., ... & Kutmon, M. (2021). WikiPathways: connecting communities. Nucleic acids research, 49(D1), D613-D621.
.. [5] Jassal, B., Matthews, L., Viteri, G., Gong, C., Lorente, P., Fabregat, A., ... & D’Eustachio, P. (2020). The reactome pathway knowledgebase. Nucleic acids research, 48(D1), D498-D503.
.. [6] Ashburner et al. Gene ontology: tool for the unification of biology. Nat Genet. May 2000;25(1):25-9
.. [7] The Gene Ontology resource: enriching a GOld mine. Nucleic Acids Res. Jan 2021;49(D1):D325-D334
.. [8] Levi, H., Rahmanian, N., Elkon, R., & Shamir, R. (2022). The DOMINO web-server for active module identification analysis. Bioinformatics, 38(8), 2364-2366.
