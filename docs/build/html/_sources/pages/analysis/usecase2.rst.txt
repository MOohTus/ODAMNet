.. _usecase2:

=====================================================
Use-case 2: data are provided directly by the users
=====================================================

Context
==========

In the context of the EJP-RD project, an overlap analysis between a list of genes targeted by vitamins A&D and pathways
related to CAKUT disease was performed (Ozisik *et al.*, 2021 [1]_).

For the vitamin A analysis, data was retrieved from several sources:
the `Comparative Toxicogenomics Database (CTD) <https://ctdbase.org/>`_ [2]_ and the study of Balmer and
Blomhoff [3]_ for the target genes, and WikiPathways (WP) [4]_, Reactome [5]_ and Gene Ontology (GO) [6]_:sup:`,` [7]_
for the disease-associated genes.

For this use-case, we used data from this paper:

- target genes : list of genes from the study of Balmer and Blomhoff [3]_ (targeted by vitamin A),

- pathways of interest : list of pathways related to CAKUT disease.

.. _useCase2_overlap:
Overlap analysis
=====================

This approach calculates the overlap between list of genes, targeted by vitamin A, and the pathways of interest
(see :doc:`../approaches/methods_overlap` section for more details).

Running overlap analysis with data provided by the users
----------------------------------------------------------

The target genes file is provided by the ``--targetGenesFile`` parameter and contains a list of genes targeted
by the vitamin A. Pathways of interest (here, pathways or processes related to CAKUT disease) are given by the ``--GMT``
parameter [:ref:`FORMAT <pathways>`]. You need to provide the background of each source : give a file with the list of
those files using ``--backgroundFile`` parameter.

Results files are saved into ``useCases/OutputResults_useCase2/`` folder.

.. code-block:: bash

        python3 main.py overlap --targetGenesFile useCases/InputData/VitA-Balmer2002-Genes.txt \
                                --GMT useCases/InputData/PathwaysOfInterest.gmt \
                                --backgroundFile useCases/InputData/PathwaysOfInterestBackground.txt \
                                --outputPath useCases/OutputResults_useCase2/

`Overlap_genesList_withpathOfInterest.csv`` file is created. It contains the results of the overlap analysis between
target genes and CAKUT related pathways/processes.

For more details about these file, see :doc:`../formats/Output` page.

Results of overlap analysis with data provided by users
---------------------------------------------------------

*request on the 07th of September 2022*

Data provided by users description
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. table:: Input data overview
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

Target genes overlap significantly ``8 pathways/processes`` related to CAKUT disease (pAdjusted <= 0.05). Results are
presented in :ref:`Table <useCase2Overlap>`.

.. _useCase2Overlap:
.. table:: Results of overlap between target genes and CAKUT disease
    :align: center

    +-----------------------+-----------------------------------------------+------------------------+------------------+
    |       PathwayIDs      |                  PathwayNames                 |         pValue         | IntersectionSize |
    +=======================+===============================================+========================+==================+
    |       GO:0072001      |            renal system development           | 6.6466522973708825e-18 |        43        |
    +-----------------------+-----------------------------------------------+------------------------+------------------+
    |       GO:0001822      |               kidney development              |  7.902033475139651e-17 |        41        |
    +-----------------------+-----------------------------------------------+------------------------+------------------+
    |       GO:0060993      |              kidney morphogenesis             |  1.923496159451833e-12 |        20        |
    +-----------------------+-----------------------------------------------+------------------------+------------------+
    |       WP:WP5053       |   Development of ureteric collection system   |  2.267498907322398e-08 |        15        |
    +-----------------------+-----------------------------------------------+------------------------+------------------+
    |       WP:WP4823       |        Genes controlling nephrogenesis        | 0.00011080436286782238 |        10        |
    +-----------------------+-----------------------------------------------+------------------------+------------------+
    | PMC5748921-PMC6115658 |               CAKUT causal genes              |  0.001058584531139687  |         6        |
    +-----------------------+-----------------------------------------------+------------------------+------------------+
    |       WP:WP4830       |            GDNF/RET signalling axis           |  0.008297232288681322  |         5        |
    +-----------------------+-----------------------------------------------+------------------------+------------------+
    |   REAC:R-HSA-2022377  | Metabolism of Angiotensinogen to Angiotensins |   0.03748808186792299  |         3        |
    +-----------------------+-----------------------------------------------+------------------------+------------------+

Ozisik *et al.,* [1]_ identified seven pathways/processes related to CAKUT disease. All of them have been retrieved
on this analysis and one more (REAC:R-HSA-2022377).

.. _useCase2_AMI:
AMI
=====================

This approach identifies Active Modules (AM) through a Protein-Protein Interaction (PPI) network. Then it performs an
overlap analysis between each AM identified and Rare Diseases pathways frm WP.
For more detail, see :doc:`../approaches/methods_AMI` section.

Running active modules identification with data provided by users
-------------------------------------------------------------------

.. warning::

   :octicon:`alert;2em` Results of DOMINO can't be reproduced when using their server.

As before, target genes list is provided by the users (``--targetGenesFile``). Pathways of interest are provided by
the users too (``--GMT`` and ``--backgroundFile`` - [:ref:`FORMAT <pathways>`]).

We will identify AM using a Protein-Protein Interaction (PPI) network named ``PPI_network_2016.sif`` [:ref:`FORMAT <SIF>`].

Results files are saved into ``useCases/OutputResults_useCase2/`` folder.

.. code-block:: bash

        python3 main.py domino  --targetGenesFile useCases/InputData/VitA-Balmer2002-Genes.txt \
                                --GMT useCases/InputData/PathwaysOfInterest.gmt \
                                --backgroundFile useCases/InputData/PathwaysOfInterestBackground.txt \
                                --networkFile useCases/InputData/PPI_network_2016.sif \
                                --outputPath useCases/OutputResults_useCase2

Several files are generated :

- ``DOMINO_inputGeneList_D014801.txt`` : list of genes (targeted by vitamin A) used for the AM identification.

- ``Overlap_AM_*_genesList_withpathOfInterest.csv`` : results of the overlap analysis between target genes and pathways of
  interest provided by the users. One file for each AM.

- ``DOMINO_genesList_activeModulesNetwork.txt``, ``DOMINO_genesList_overlapAMresults4Cytoscape.txt``, ``DOMINO_genesList_activeModules.txt``
  , ``DOMINO_genesList_activeModulesNetworkMetrics.txt`` and ``DOMINO_genesList_signOverlap.txt`` : some metrics are
  calculated and saved into files. Theses files are useful for visualisation.

For more details about these file, see :doc:`../formats/Output` page (:ref:`requestOutput`, :ref:`overlapOutput`, :ref:`AMIOutput`)

Results of active module identification with data provided by users
--------------------------------------------------------------------

*request on the 07th of September 2022*

Data provided by users description
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. table:: Input data overview
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

Active Modules Identification results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Target genes are defined as Active genes by DOMINO (Active Modules identification tool). We give **521 active genes** as input.

We found **18 Active Modules** :

.. table:: DOMINO result metrics
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

We found **7 pathways/processes** that are significantly overlaped by **6 Active Modules** (padjusted <= 0.05).

.. table:: Overlap analysis between AM and pathways of interest provided by users
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

Visualisation of AM results
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

We visualised the result using a network representation (:numref:`dominoUsage2Fig`). To know how to create this figure,
see the :ref:`networkAMI` section.

.. _dominoUsage2Fig:
.. figure:: ../../pictures/useCase2_DOMINO_network.png
   :alt: usecase2 AMI
   :align: center

   : Network visualisation of Active modules which overlap significantly target genes

Some network are enriched with the same pathways whereas other contain genes involved in different pathways. Target genes
(i.e. active genes, grey spheres) could be part of pathways as non-target genes (white spheres).

.. _useCase2_RWR:
RWR
=====================

With this approach, a Random Walk with Restart (see :doc:`../approaches/methods_RWR` section for more details )
is apply into two different multilayer compositions:

1. Multiplex (PPI + Complex + Reactome) and pathways of interest network only connected to genes nodes
2. Multiplex (PPI + Complex + Reactome) and Disease-Disease similarity network

*For more details about networks used, see* :ref:`pathwaysOfInterestNet` *and* :ref:`DDnet`.

Running Random Walk analysis with data provided by users
-----------------------------------------------------------

For the first composition of network, we created the pathways of interest network : see :ref:`pathwaysOfInterestNet`.

The list of target genes is provided by the users using ``--targetGenesFile``.

MultiXrank needs a configuration file (``--configPath``) and the networks path (``--networksPath``). We run the analysis with
default parameters.
The target genes are set as seeds for the walk and saved into a file ``--seedsFile examples/InputData/seeds.txt``.
You need to give the SIF name (``--sifFileName``) to save the network results and the top number of results too
(``--top 10``).

Results files are saved into ``useCases/OutputResults_useCase2/`` folder.

If you need more details about the input format files, see :ref:`RWRinput` part.

.. tip::

    Whatever the networks used, the **command line is the same**. But you have to **change** the network name inside the
    **configuration file**.

    .. tabs::

        .. group-tab:: Pathways of interest network

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

    python3 main.py multixrank  --targetGenesFile useCases/InputData/VitA-Balmer2002-Genes.txt \
                                --configPath useCases/InputData/config_minimal_useCase2.yml \
                                --networksPath useCases/InputData/ \
                                --seedsFile useCases/InputData/seeds.txt \
                                --sifFileName resultsNetwork_useCase2.sif \
                                --top 10 \
                                --outputPath useCases/OutputResults_useCase2/

Several files are generated into ``RWR_genesList/`` folder:

    - ``config_minimal_useCase2.yml`` and ``seeds.txt`` : a copy of the input files

    - ``multiplex_1.tsv`` and ``multiplex_2.tsv`` : score for each feature. 1 corresponds to the multiplex and 2 to
      the disease network (depends of the folder name where networks are saved).

    - ``resultsNetwork_useCase2.sif`` : SIF file with the network result

For more details about these file, see :doc:`../formats/Output` page.

Results of Random Walk analysis with data provided by users
-------------------------------------------------------------

We use the default parameters, whatever the networks used. For reminder, we have **521 target genes** in the target genes file
provided by users.

Pathways of interest network analysis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Target genes are used as seed to start the walk : ``483/521`` genes are set.

The gene with the highest score is ``ASMT`` with ``score = 0.0006682735081574565`` (it's a seed). This score helps
us to select a list of pathways. All pathways with a score bigger than this score are extracted and considered as connected
with target genes (i.e. seeds).

There are **4 pathways** with a higher score (:ref:`Table <pathwaysRWRresults>`) :

.. _pathwaysRWRresults:
.. table:: Pathways linked to target genes
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

Two pathways not found with the previous approaches, are link to target genes : ``REAC:R-HSA-195721`` and ``REAC:R-HSA-157118``.

You can represent the results with a network as shown on the

.. _useCase2_pathwaysNetworkRWR:
.. figure:: ../../pictures/RWR_pathwaysNet_useCase2.png
   :alt: usecase 2 pathwaysNetworkRWR
   :align: center

   : Results from RWR through the molecular multilayer and pathways of interest network

Disease-Disease similarity network
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Target genes are used as seed to start the walk : ``483/521`` genes are set.

We selected the top 10 of diseases (:ref:`Table <diseasesRWRresults>`).

.. _diseasesRWRresults:
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

You can represent the results with a network as shown on the

.. _useCase2_simNetworkRWR:
.. figure:: ../../pictures/RWR_pathwaysNet_useCase2_simNet.png
   :alt: usecase 2 simNetworkRWR
   :align: center

   : Results from RWR through the molecular multilayer and disease-disease similarity network

Rare disease pathways identified
====================================

To compare results from the different approaches, we use orsum [2]_.

.. code-block:: bash

    orsum.py    --gmt 00_Data/hsapiens_background.gmt \
                --files Overlap_genesList_withpathOfInterest.4Orsum DOMINO_genesList_signOverlap.4Orsum pathwaysResults.4Orsum \
                --fileAliases Overlap DOMINO multiXrank \
                --outputFolder useCase2Comparison/

The results are display on the :numref:`useCase2_orsum`.

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
.. [8] Curated chemical–gene interactions data were retrieved from the Comparative Toxicogenomics Database (CTD), MDI Biological Laboratory, Salisbury Cove, Maine, and NC State University, Raleigh, North Carolina. World Wide Web (URL: http://ctdbase.org/). [Month, year of data retrieval].

