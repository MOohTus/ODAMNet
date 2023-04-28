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

Active Module Identification (AMI)
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

Then, we perform an Overlap analysis between identified active modules (21) and pathways/processes related to CAKUT
(13). We obtained significant overlap between **6 idantified active modules** and **6 pathways/processes**
(pAdjusted <= 0.05). Results are presented in :ref:`Table 17 <useCase2_AMIOverlap>`

Duplicates between active modules results are removed and we keep the more significant ones.

.. _useCase2_AMIOverlap:
.. table:: - Significant overlaps between identified active modules and pathways/processes related to CAKUT
    :align: center

    +------------------------+-------------------------------------------+--------------+
    | Pathway IDs            | Pathway Names                             | pAdjusted    |
    +========================+===========================================+==============+
    | GO:0072001             | renal system development                  | 2.66e-03     |
    +------------------------+-------------------------------------------+--------------+
    | GO:0001822             | kidney development                        | 2.66e-03     |
    +------------------------+-------------------------------------------+--------------+
    | GO:0060993             | kidney morphogenesis                      | 2.66e-03     |
    +------------------------+-------------------------------------------+--------------+
    | **REAC:R-HSA-8853659** | **RET signaling**                         | **5.19e-03** |
    +------------------------+-------------------------------------------+--------------+
    | WP:WP5053              | Development of ureteric collection system | 3.21e-02     |
    +------------------------+-------------------------------------------+--------------+
    | **REAC:R-HSA-195721**  | **Signaling by WNT**                      | **3.47e-02** |
    +------------------------+-------------------------------------------+--------------+

The *RET signaling* and *Signaling by WNT* reactome pathways were not identified with the overlap approach in the
previous study [1]_ neither with the ODAMNet Overlap analysis.

.. cssclass:: italic

    See ``DOMINO_genesList_signOverlap.txt`` file for more details.

Visualisation of AMI results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We created a visualisation of AMI results (:numref:`useCase1_AMIFig`) using Cytoscape [9]_.

We found a significant overlap between **6 active modules** and **6 pathways/processes** related to CAKUT. For sake of
visualisation, we selected only three of them (:numref:`useCase2_AMIFig`). You can find the entire visualisation in the
cytoscape project called ``AMI_visualisation.cys`` in GitHub_.

.. _useCase2_AMIFig:
.. figure:: ../../pictures/UseCase2/UseCase2_AMI.png
   :alt: useCase2_AMIFig
   :align: center
   :scale: 50

   : Visualisation of 3 active modules and their associated pathways/processes related to CAKUT

   Genes are represented by nodes. Grey nodes are target genes, white nodes are non-target genes. Overlap results
   between active modules and rare disease pathways are displayed using donuts color around nodes. Each color
   corresponds to a rare disease pathways. Creation steps are explained in the :ref:`cytoscape_AMI` section.

Module topology is different between modules and associated rare diseases pathways also vary
(:numref:`useCase2_AMIFig`).

The first active module (left in the :numref:`useCase2_AMIFig`) is very connected and contains genes involved in
several pathways and processes related to CAKUT. Association between vitamin A and *RET signaling* reactome pathway is
indirect. Indeed, genes involved in this pathway are not genes targeted by vitamin A. That explains why we didn't found
this pathways with the Overlap analysis (see :ref:`Use-case 2 overlap results <useCase2_overlap>`).

The second active module (middle in the :numref:`useCase2_AMIFig`) is also highly connected but its contains genes
involved only in one pathways/processes related to CAKUT (*Development of ureteric collection system*).

The third active module (right in the :numref:`useCase2_AMIFig`) is sparser. It contains target genes and non-target
genes involved in *kidney morphogenesis* and *Signaling by WNT*.

.. _useCase2_RWR:

Random Walk with Restart (RWR)
===============================

The Random Walk with Restart (RWR) approach mesures proximities between vitamin A target genes and pathways/processes
related to CAKUT. To calculate these proximities (RWR scores), we used multiXrank [10]_ and multilayer networks. See
:doc:`../approaches/methods_RWR` page for more details.

The multilayer network is composed of three gene networks and one pathways/processes related to CAKUT network. Genes
nodes are connected to pathways/processes nodes if they are involved in. See :doc:`../network/NetworkUsed` page for
more details.

Running RWR with data provided by user
-----------------------------------------

Target genes file is given using ``--targetGenesFile`` parameter. IT contains list of vitamin A target genes
[:ref:`FORMAT <targetGenesFile>`].

MultiXrank needs as input a configuration file (``--configPath``) that contains path of networks and analysis
parameters. We used multiXrank with default parameters.

We provided a name file to save vitamin A target genes (i.e. seeds) ``--sifFileName useCases/InputData/seeds.txt`` and
also a SIF file name (``--sifFileName``) to save the top nodes based on RWR score (``--top 20``).

Results files are saved into ``useCases/OutputResults_useCase2/`` folder.

.. code-block:: bash

    odamnet multixrank      --targetGenesFile useCases/InputData/VitA-Balmer2002-Genes.txt \
                            --configPath useCases/InputData/config_minimal_useCase2.yml \
                            --networksPath useCases/InputData/ \
                            --seedsFile useCases/InputData/seeds.txt \
                            --sifFileName UseCase2_RWR_network.sif \
                            --top 5 \
                            --outputPath useCases/OutputResults_useCase2

.. tip::

    | - Downloading of multiplex network from NDEx: :doc:`../network/NetworkUsed` + :doc:`../network/NetworkDownloading`
    | - Creation of the pathways/processes network: :doc:`../network/NetworkUsed` +  :doc:`../network/NetworkCreation`
    | - Configuration file explanation and example: :ref:`configFile` section

Several files are generated into ``RWR_genesList/`` folder:

- ``config_minimal_useCase2.yml`` and ``seeds.txt``: copies of the input files

- ``multiplex_1.tsv`` and ``multiplex_2.tsv``: RWR scores for each multilayer. 1 is the genes multilayer network RWR
  scores and 2 is the pathways/processes related to CAKUT network RWR scores.

- ``UseCase2_RWR_network.sif``: SIF file name that contains the network result

- ``RWR_topX.txt``: Top X of pathways/processes related to CAKUT

.. cssclass:: italic

    For more details about these file, see :doc:`../formats/Output` page.

Results of RWR with data provided by user
-----------------------------------------------

Data provided by user overview
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Target genes are coming from Balmer and Blomhoff [3]_. There are **521 vitamin A target genes**.

RWR results
~~~~~~~~~~~~~~

Analysis with pathways/processes related to CAKUT network
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

We used a multilayer network composed of three gene networks and one pathways/processes related to CAKUT network
(:numref:`multilayerCompo` - left, :ref:`genesMultilayerNet` and :ref:`Rare disease pathways network<pathwaysOfInterestNet>`).

multiXrank defined vitamin A target genes as seeds. Over the 521 target genes, 480 are found in the multilayer and
used as seeds. Using the RWR scores (i.e. proximity score with the target genes), pathways/processes related to CAKUT
are prioritized. We selected the top 5 (:ref:`Table 18 <useCase2_RWRpathOfInt>`).

.. _useCase2_RWRpathOfInt:
.. table:: - Pathways/processes related to CAKUT prioritization using RWR score. The top 5 is displayed.
    :align: center
    :widths: 25 50 25

    +-----------------------+-------------------------------------------+--------------+
    | Nodes (pathway IDs)   | Pathway Names                             | RWR scores   |
    +=======================+===========================================+==============+
    | GO:0072001            | renal system development                  | 2.12e-03     |
    +-----------------------+-------------------------------------------+--------------+
    | GO:0001822            | kidney development                        | 1.86e-03     |
    +-----------------------+-------------------------------------------+--------------+
    | **REAC:R-HSA-195721** | **Signaling by WNT**                      | **1.69e-03** |
    +-----------------------+-------------------------------------------+--------------+
    | **REAC:R-HSA-157118** | **Signaling by NOTCH**                    | **1.19e-03** |
    +-----------------------+-------------------------------------------+--------------+
    | WP:WP5053             | Development of ureteric collection system | 6.46e-04     |
    +-----------------------+-------------------------------------------+--------------+

We created a visualisation of the results (:numref:`useCase2_RWRWPFig`) using Cytoscape [9]_. You can retrieved it in
the cytoscape project called ``RWR_visualisation.cys`` in GitHub_. The :numref:`useCase2_RWRWPFig` presents the top 5
of pathways/processes related to CAKUT, ordered by RWR score.

.. _useCase2_RWRpathOfIntFig:
.. figure:: ../../pictures/UseCase2/UseCase2_RWR_top5.png
   :alt: useCase2_RWRpathOfIntFig
   :align: center
   :scale: 70

   : Top 5 of the pathways/processes related to CAKUT prioritized using RWR score using a (disconnected)
   pathways/processes related to CAKUT network

   Pathways/processes related to CAKUT are in pink triangles. Target genes are in grey and non-target genes are in
   white. Creation steps are explained in the :ref:`cytoscape_RWR` section.

Extra : analysis with disease-disease similarity network
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

.. tip::

    :octicon:`alert;1.5em` Same command line, but you need to change :ref:`configuration file <configFile>`.

We also propose to run an RWR approach using a **disease-disease similarity network**. In this network, rare diseases
are linked together according their phenotype similarity whereas in the previous network they were not at all connected.

We used a multilayer network composed of three genes network and one disease-disease similarity network
(:numref:`multilayerCompo` - right, :ref:`genesMultilayerNet`, :ref:`similarityNet`).

multiXrank defined vitamin A target genes as seeds. Over the 521 target genes retrieved from CTD, 480 are found in
the multilayer and used as seeds. Using the RWR scores (i.e. proximity score with the target genes), rare disease are
prioritized. We selected the top 20 and presented the top 5 (:ref:`Table 19 <useCase2_RWRSim>`).

.. _useCase2_RWRSim:
.. table:: - Rare disease prioritization using RWR score. The top 5 is displayed.
    :align: center

    +---------------------+-----------------------------------------+---------------+
    | Nodes (disease IDs) | Disease Names                           | RWR scores    |
    +=====================+=========================================+===============+
    | OMIM:178500         | Pulmonary fibrosis, idiopathic          | 3.47e-04      |
    +---------------------+-----------------------------------------+---------------+
    | OMIM:125853         | Diabetes mellitus, noninsulin-dependent | 3.13e-04      |
    +---------------------+-----------------------------------------+---------------+
    | OMIM:215600         | Cirrhosis, familial                     | 2.73e-04      |
    +---------------------+-----------------------------------------+---------------+
    | OMIM:613659         | Gastric cancer, somatic                 | 2.38e-04      |
    +---------------------+-----------------------------------------+---------------+
    | OMIM:104300         | Alzheimer disease                       | 2.34e-04      |
    +---------------------+-----------------------------------------+---------------+

We created a visualisation of the results (:numref:`useCase2_RWRSimFig`) using Cytoscape [9]_. You can retrieved it in
the cytoscape project called ``RWR_visualisation.cys`` in GitHub_. The :numref:`useCase2_RWRSimFig` presents the
top 5 of rare disease pathways, ordered by RWR score.

.. _useCase2_RWRSimFig:
.. figure:: ../../pictures/UseCase2/UseCase2_RWR_top5_sim.png
   :alt: useCase2_RWRSimFig
   :align: center
   :scale: 70

   : Top 5 of the rare disease prioritized using RWR score using disease-disease similarity network

    Rare disease are in pink triangles. Target genes are in grey and non-target genes are in white. Creation
    steps are explained in the :ref:`cytoscape_RWR` section.

Overlap, AMI and RWR results comparison
===========================================

We compare results obtained with the three different approaches: Overlap analysis, Active Module Identification (AMI)
and Random Walk with Restart (RWR). We used orsum [2]_, a Python package to filter and integrate enrichment analysis
from several analyses. The main result is a heatmap, presented in :numref:`useCase2_orsum`.

.. code-block:: bash

    orsum.py --gmt 00_Data/hsapiens_background.gmt \
             --files 00_Data/Overlap.4Orsum 00_Data/DOMINO.4Orsum 00_Data/RWR_top5.4Orsum \
             --fileAliases Overlap AMI RWR \
             --maxRepSize 0 \
             --outputFolder UseCase2_orsum

.. _useCase2_orsum:
.. figure:: ../../pictures/UseCase2/UseCase2_orsum.png
   :alt: useCase2_orsum
   :align: center
   :scale: 30

   : Overlap analysis (Overlap), Active module identification (AMI) and Random walk with restart (RWR) results integration and comparison using orsum

The ``--maxRepSize`` parameter is set to 0 to consider each term as is own representative term.

Some pathways/processes related to CAKUT are retrieved associated with vitamin A by all the three approaches such as
*renal system development* and *kidney development*. Some other are retrieved associated with vitamin A only by one
(*RET signaling*) or two (*Signaling by WNT*) approaches.

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
.. _NDExPPI: https://www.ndexbio.org/viewer/networks/bfac0486-cefe-11ed-a79c-005056ae23aa
.. |NDExPPI| replace:: NDEx
.. _GitHub: https://github.com/MOohTus/ODAMNet/tree/main/useCases/