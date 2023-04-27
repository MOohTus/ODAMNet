=====================================================
Use-case 2: data are provided by the user
=====================================================

Context
==========

In Ozisik *et al.*, 2021 [1]_ paper, an overlap analysis is performed between vitamin A and D target genes and processes
related to Congenital Anomalies of the Kidney and Urinary Tract (CAKUT).

In this use-case, we illustrate how to use ODAMNet with data provided by user. We use data from Ozisik *et al.*,
2021 [1]_ paper. Results are compared with those found in the Ozisik *et al.*, 2021 [1]_ paper.

**Vitamin A target genes** are coming from Balmer and Blomhoff [3]_ paper and **pathways/processes** related to CAKUT
are coming from |wiki|_ [4]_, |reac|_ [5]_ and |go|_ (GO) [6]_:sup:`,` [7]_. Biological networks used are presented in
the :doc:`../network/NetworkUsed` page and are coming from the |NDEx|_ (NDEx) [11]_. Input data are available in |git|_.

.. _useCase2_overlap:

Overlap analysis
=====================

The Overlap analysis searches intersecting genes between vitamin A target genes and genes involved in pathways/processes
related to CAKUT pathways (see :doc:`../approaches/methods_overlap` page for more details).

Running Overlap analysis with data provided by user
----------------------------------------------------------

Target genes file is given using the ``--targetGenesFile`` parameter. It contains the list of vitamin A target genes
[:ref:`FORMAT <targetGenesFile>`].

Pathways/processes related to CAKUT are given using the ``--GMT`` parameter [:ref:`FORMAT <pathways>`]. Background genes
of each source of pathways/processes is required (``--backgroundFile`` parameter). The file contains the list of
background file names.

Results files are saved into ``useCases/OutputResults_useCase2/`` folder.

.. code-block:: bash

        odamnet overlap --targetGenesFile useCases/InputData/VitA-Balmer2002-Genes.txt \
                        --GMT useCases/InputData/PathwaysOfInterest.gmt \
                        --backgroundFile useCases/InputData/PathwaysOfInterestBackground.txt \
                        --outputPath useCases/OutputResults_useCase2

``Overlap_genesList_withpathOfInterest.csv`` file is created. It contains results of the overlap analysis between
vitamin A target genes and CAKUT related pathways/processes.

.. cssclass:: italic

    For more details about this output file, see :ref:`overlapOutput` section.

Results of Overlap analysis with data provided by user
---------------------------------------------------------

Data provided by user overview
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Target genes are coming from Balmer and Blomhoff [3]_. Pathways of interests are coming from Reactome [5]_ and
WikiPathways [4]_ and processes of interest are coming from Biological Process (GO) [6]_:sup:`,` [7]_.
Data are presented in the :ref:`Table 13 <useCase2_OverlapDataOverview>`.

.. _useCase2_OverlapDataOverview:
.. table:: - Overview of data provided by user
    :align: center

    +-------------------------------------+--------+
    |                                     | Number |
    +=====================================+========+
    |     Vitamin A target genes          |   521  |
    +-------------------------------------+--------+
    | Pathways/processes related to CAKUT |   13   |
    +-------------------------------------+--------+
    |        Pathways/processes sources   |    3   |
    +-------------------------------------+--------+

Overlap analysis results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We performed an Overlap analysis between vitamin A target genes (521) and pathways/processes related to CAKUT (13). We
obtained significant overlap between target genes and **7 pathways/processes** related to CAKUT (pAdjusted <= 0.05).
Results are presented in the :ref:`Table 14 <useCase2_OverlapResults>`.

Top 5 of the significant overlaps between the vitamin A target genes and rare disease pathways

.. _useCase2_OverlapResults:
.. table:: - Significant overlap results between vitamin A target genes and pathways/processes related tp CAKUT
    :align: center

    +-----------------------+----------------------------------------+-----------+------------------+
    |       PathwayIDs      |                  PathwayNames          |  pAdjusted| IntersectionSize |
    +=======================+========================================+===========+==================+
    |       GO:0072001      |            renal system development    |  8.64e-17 |        43        |
    +-----------------------+----------------------------------------+-----------+------------------+
    |       GO:0001822      |               kidney development       |  5.14e-16 |        41        |
    +-----------------------+----------------------------------------+-----------+------------------+
    |       GO:0060993      |              kidney morphogenesis      |  8.33e-12 |        20        |
    +-----------------------+----------------------------------------+-----------+------------------+
    |       WP:WP5053       | Development of ureteric collection ... |  7.37e-08 |        15        |
    +-----------------------+----------------------------------------+-----------+------------------+
    |       WP:WP4823       |     Genes controlling nephrogenesis    |  2.88e-04 |        10        |
    +-----------------------+----------------------------------------+-----------+------------------+
    | PMC5748921-PMC6115658 |               CAKUT causal genes       | 2.30e-03  |         6        |
    +-----------------------+----------------------------------------+-----------+------------------+
    |       WP:WP4830       |            GDNF/RET signalling axis    | 1.54e-02  |         5        |
    +-----------------------+----------------------------------------+-----------+------------------+

Ozisik *et al.,* [1]_ identified 7 pathways/processes related to CAKUT disease over 13. ODAMNet found the same 7
pathways/processes.

.. _useCase2_AMI:

Active Modules Identification (AMI)
====================================

The Active Module Identification (AMI) approach identifies active module that contains high number of vitamin A target
genes using a protein-protein interaction (PPI) network. AMI is performed using DOMINO [8]_. Then, an Overlap analysis
is applied between identified active modules and CAKUT pathways/processes. See :doc:`../approaches/methods_AMI` page for
more details.

Running AMI with data provided by user
------------------------------------------

.. warning::

   :octicon:`alert;2em` When using DOMINO server, **results cannot be identically reproduced**. Indeed, DOMINO server doesn't allow to set the random seed. This random seed changes every new analysis.

Target genes file is given using the ``--targetGenesFile`` parameter. It contains the list of vitamin A target genes
[:ref:`FORMAT <targetGenesFile>`].

Pathways/processes related to CAKUT are given using the ``--GMT`` parameter [:ref:`FORMAT <pathways>`]. Background genes
of each source of pathways/processes is required (``--backgroundFile`` parameter). The file contains the list of
background file names.

We used a PPI network [:ref:`FORMAT <SIF>`] previously downloaded from NDEx [11]_. The PPI network file is provided
using ``--networkFile`` parameter. See :doc:`../network/NetworkDownloading` section. Network name should have
**.sif** extension.

Results files are saved into ``useCases/OutputResults_useCase2/`` folder.

.. code-block:: bash

    odamnet domino  --targetGenesFile useCases/InputData/VitA-Balmer2002-Genes.txt \
                    --GMT useCases/InputData/PathwaysOfInterest.gmt \
                    --backgroundFile useCases/InputData/PathwaysOfInterestBackground.txt \
                    --networkFile useCases/InputData/PPI_HiUnion_LitBM_APID_gene_names_190123.sif \
                    --outputPath useCases/OutputResults_useCase2

Several files are generated:

- ``DOMINO_inputGeneList_genesList.txt``: vitamin A target genes list used for the active module identification.

- ``Overlap_AM_*_genesList_withpathOfInterest.csv``: results of the Overlap analysis between identified active modules
  genes and pathways/processes of related to CAKUT. There is one file per active module.

- ``DOMINO_genesList_activeModulesNetwork.txt``, ``DOMINO_genesList_overlapAMresults4Cytoscape.txt``,
  ``DOMINO_genesList_activeModules.txt``, ``DOMINO_genesList_activeModulesNetworkMetrics.txt`` and
  ``DOMINO_genesList_signOverlap.txt``: some statistics are calculated and saved into files. Theses files are useful
  for visualisation.

.. cssclass:: italic

    For more details about these files, see :doc:`../formats/Output` page (:ref:`overlapOutput` and :ref:`AMIOutput`)

Results of AMI with data provided by user
---------------------------------------------

Data provided by user overview
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Target genes are coming from Balmer and Blomhoff [3]_. Pathways of interests are coming from Reactome [5]_ and
WikiPathways [4]_ and processes of interest are coming from Biological Process (GO) [6]_:sup:`,` [7]_.
Data are presented in the :ref:`Table 15 <useCase2_AMIDataOverview>`.

.. _useCase2_AMIDataOverview:
.. table:: Overview of data provided by user
    :align: center

    +-------------------------------------+--------+
    |                                     | Number |
    +=====================================+========+
    |     Vitamin A target genes          |   521  |
    +-------------------------------------+--------+
    | Pathways/processes related to CAKUT |   13   |
    +-------------------------------------+--------+
    |        Pathways/processes sources   |    3   |
    +-------------------------------------+--------+

The PPI network is downloaded from |NDExPPI|_ (see :ref:`PPInet`). It was build from 3 datasets: Lit-BM, Hi-Union and
APID. It contains 15,390 nodes and 131,087 edges.

AMI results
~~~~~~~~~~~~~

DOMINO defines vitamin A target genes as active genes and searches active modules enriched in active genes. Over the
521 target genes, 468 are found in the PPI and used as active genes by DOMINO. DOMINO identified
**21 active modules** enriched in vitamin A target genes (:ref:`Table 16 <useCase2_AMIResults>`).

.. _useCase2_AMIResults:
.. table:: - Composition of the active modules identified enriched in vitamin A target genes by DOMINO
    :align: center
    :widths: 60 25 25

    +--------------+------------+------------+
    |              | Min number | Max number |
    +==============+============+============+
    |     Edges    |     3      |     223    |
    +--------------+------------+------------+
    |     Nodes    |     4      |     99     |
    +--------------+------------+------------+
    | Target genes |     3      |     19     |
    +--------------+------------+------------+

.. cssclass:: italic

    See ``DOMINO_genesList_activeModulesNetworkMetrics.txt`` file for more details.

Overlap analysis results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After identification of active modules, ODAMNet performs an overlap analysis between each identified active modules and
pathways/processes related to CAKUT. Significant overlaps are found between **6 active modules** and **7 pathways/processes**
related to CAKUT (padjusted <= 0.05).

.. _useCase2_AMIOverlap:
.. table:: Overlap analysis between active modules and pathways/processes related to CAKUT
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

The **REAC:R-HSA-8853659** Reactome pathway was not identified with the overlap approach used in the Ozisik
*et al.* [1]_ paper.

Visualisation of active module identification results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Visualization can help to identify overlap between active modules and pathways/processes related to CAKUT. The
:numref:`useCase2_AMIFig` presents active modules that have a significant overlap with pathways/processes related to
CAKUT. For better visualization, only 3 over the 6 identified active modules are displayed. You can retrieve the complete
figure in the |gitAMI|_.

.. _useCase2_AMIFig:
.. figure:: ../../pictures/useCase2_DOMINO_network.png
   :alt: useCase2_AMIFig
   :align: center
   :scale: 50


   : Visualization of 3 active modules that have a significant overlap with pathways/processes related to CAKUT.
   This figure is created using Cytoscape [9]_. Target genes are in grey.

As you can see in the :numref:`useCase2_AMIFig`, topology of modules is different and associated pathways/processes
varies. Target genes are in grey and others are in white.

The first active module (left in the :numref:`useCase2_AMIFig`) is very connected and contains genes involved in
only one pathway related to CAKUT (*RET signaling*). Here, the connection between target genes and CAKUT disease is
indirect. Indeed, genes involved in the pathway are not genes targeted by vitamin A. That why we didn't found this
pathways with the overlap approach (see :ref:`Use-case 2 overlap results <useCase2_overlap>`).

The second active module (middle in the :numref:`useCase2_AMIFig`) is sparse and contains genes involved in several
pathways/processes related to CAKUT (all the 7 pathways/processes identified). Some genes are targeted by vitamin A,
others don't. Three genes seem to play key roles because they are part of several pathways/processes as **RET**, **STAT1**
or **GDNF** that is not a target gene (white node).

The third active module (right in the :numref:`useCase2_AMIFig`) contains target genes and genes involved essentially
in kidney development.

.. cssclass:: italic

    To know how to create this figure, see the :ref:`cytoscape_AMI` section.

.. _useCase2_RWR:

Random Walk with Restart (RWR)
===============================

.. note::

    | **Multilayer** is a network with several layers where layers contain different nodes types
    | **Multiplex** is a network with several layers (multilayer) where layers contain same type of nodes

The third approach implemented in ODAMNet is a Random Walk with Restart analysis (RWR). RWR is applied using
multiXrank [10]_ through a multilayer composed of genes and diseases nodes.

We applied RWR using two different multilayer compositions:

- **Multilayer 1**: Multiplex + pathways/processes related to CAKUT network
- **Multilayer 2**: Multiplex + disease-disease similarity network

Used multilayers will be detailed in corresponding section results.

.. cssclass:: italic

    For more details about RWR, see :doc:`../approaches/methods_RWR`.

Running Random Walk analysis with data provided by user
-----------------------------------------------------------

Target genes files is given using ``--targetGenesFile`` parameter. The file contains list of genes targeted by vitamin
A [:ref:`FORMAT <targetGenesFile>`].

To perform RWR, multiXrank [10]_ needs a configuration file given using ``--configPath`` parameter. This configuration
file contains path of different networks and target genes files used. The configuration file might contains parameters
for RWR analysis. We run the RWR analysis with default parameters.

MultiXrank needs also the networks directory path given using ``--networksPath`` parameter. MultiXrank defines target
genes as seeds for the walk. Target genes will be saved into a file given using ``--seedsFile`` parameter.

Two others parameters are required: number to select top nodes in each layer (``--top``) and file name to saved result
network which contains top nodes of each layers and their relationships (``--sifFileName``).

Results files are saved into ``useCases/OutputResults_useCase2/`` folder.

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

- ``config_minimal_useCase2.yml`` and ``seeds.txt``: copies of the input configuration and seed files

- ``multiplex_1.tsv`` and ``multiplex_2.tsv``: result files that contain RWR score for each node. multiplex_1
  corresponds to the gene multiplex and multiplex_2 corresponds to the disease network

- ``resultsNetwork_useCase2.sif``: SIF file name that contains the network result

.. cssclass:: italic

    | For more details about the input files, see :ref:`GR` section.
    | For more details about the output files, see :doc:`../formats/Output` page.

Results of Random Walk analysis with data provided by user
-------------------------------------------------------------

Data provided by user overview
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Target genes are coming from Balmer and Blomhoff [3]_. There are **521 vitamin A target genes**.

**Multilayer 1** contains:

- multiplex network

    - PPI (14,703 nodes and 143,653 edges)
    - molecular complexes (8,537 nodes and 63,531 edges)
    - Reactome pathways (7,926 nodes and 194,500 edges)

- pathways/processes related to CAKUT network (13 nodes and 0 edges)

These two networks are linked using bipartite that contains 1,655 associations (866 genes and 13 pathways/processes).

.. cssclass:: italic

    For more details about the pathways/processes of interest network: see :ref:`pathwaysOfInterestNet`.

**Multilayer 2** contains:

- multiplex network

    - PPI (14,703 nodes and 143,653 edges)
    - molecular complexes (8,537 nodes and 63,531 edges)
    - Reactome pathways (7,926 nodes and 194,500 edges)

- disease-disease similarity network (8,264 nodes and 33,925 edges)

These two networks are linked using bipartite that contains 6,534 associations (4,483 genes and 5,878 diseases).

.. cssclass:: italic

    For more details about the disease-disease similarity network: see :ref:`DDnet`.

Multilayer 1 : Pathways/processes related to CAKUT network
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

    In this part, we present results found using the Multilayer 1: multiplex + pathways/processed related to CAKUT
    network

MultiXrank [10]_ defines **483** target genes over the 521 as seeds to start the walk. For each node (genes or
pathways/processes related to CAKUT), multiXrank calculates a RWR score. Based on this score, we selected the 10 top of
node scores.







*In this part, we present results found for the first multiplex composition: multiplex + pathways/processes of interest.*

First, target genes are used as seed to start the walk: ``483/521`` genes are used.

The gene with the highest score is ``ASMT`` with ``score = 0.0006682735081574565`` (it's a seed). This score helps
us to select a list of pathways/processes. All pathways/processes with a score bigger than this score are extracted and considered as connected
with target genes (i.e. seeds).

According this highest score, **4 pathways/processes** are selected (:ref:`Table 18 <useCase2_RWRpathOfInt>`).

.. _useCase2_RWRpathOfInt:
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
You can visualise the results with a network as shown on the :numref:`useCase2_RWRpathOfIntFig`.

.. _useCase2_RWRpathOfIntFig:
.. figure:: ../../pictures/RWR_pathwaysNet_useCase2.png
   :alt: useCase2_RWRpathOfIntFig
   :align: center
   :scale: 70


   : Results from RWR through the molecular multilayer and pathways/processes of interest network

    Pathways/processes of interest are represented by triangle nodes in pink, genes are represented by white nodes and target genes by grey nodes.

Disease-Disease similarity network
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*In this part, we present results found for the second multiplex composition: multiplex + disease-disease network.*

First, target genes are used as seed to start the walk: ``483/521`` genes are used.

We selected the top 10 of diseases (:ref:`Table 19 <useCase2_RWRSim>`).

.. _useCase2_RWRSim:
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

You can represent the results with a network as shown in the :numref:`useCase2_RWRSimFig`.

.. _useCase2_RWRSimFig:
.. figure:: ../../pictures/RWR_pathwaysNet_useCase2_simNet.png
   :alt: useCase2_RWRSimFig
   :align: center
   :scale: 70


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
   :scale: 50

   : Comparison of use-case 2 results using orsum

References
============

.. [1] Ozisik O, Ehrhart F, Evelo C *et al.*. Overlap of vitamin A and vitamin D target genes with CAKUT-related processes. F1000Research. 2021.
.. [2] Davis AP, Grondin CJ, Johnson RJ *et al.*. The Comparative Toxicogenomics Database: update 2021. Nucleic acids research. 2021.
.. [3] Balmer JE & Blomhoff R. Gene expression regulation by retinoic acid. Journal of lipid research. 2002.
.. [4] Martens M, Ammar A, Riutta A *et al.*. WikiPathways: connecting communities. Nucleic acids research. 2021.
.. [5] Jassal B, Matthews L, Viteri G *et al.*. The reactome pathway knowledgebase. Nucleic acids research. 2020.
.. [6] Ashburner M, Ball CA, Blake JA *et al.*. Gene ontology: tool for the unification of biology. Nature Genetics. 2000.
.. [7] The Gene Ontology Consortium. The Gene Ontology resource: enriching a GOld mine. Nucleic acids research. 2021.
.. [8] Levi H, Rahmanian N, Elkon R *et al.*. The DOMINO web-server for active module identification analysis. Bioinformatics. 2022.
.. [9] Shannon P, Markiel A, Ozier O *et al.*. Cytoscape: a software environment for integrated models of biomolecular interaction networks. Genome research. 2003.
.. [10] Baptista A, Gonzalez A & Baudot A. Universal multilayer network exploration by random walk with restart. Communications Physics. 2022.
.. [11] Pratt D, Chen J, Welker *et al.*. NDEx, the Network Data Exchange. Cell Systems. 2015.


.. _NDEx: https://www.ndexbio.org/
.. |NDEx| replace:: Network Data Exchange
.. _git: https://github.com/MOohTus/ODAMNet/tree/main/useCases/InputData
.. |git| replace:: GitHub
.. _wiki: https://www.wikipathways.org/
.. |wiki| replace:: WikiPathways
.. _reac: https://reactome.org/
.. |reac| replace:: Reactome
.. _go: http://geneontology.org/
.. |go| replace:: Gene Ontology
.. _gitAMI: https://github.com/MOohTus/ODAMNet/tree/main/useCases/InputData
.. |gitAMI| replace:: GitHub page
.. _NDExPPI: https://www.ndexbio.org/viewer/networks/bfac0486-cefe-11ed-a79c-005056ae23aa
.. |NDExPPI| replace:: NDEx