.. _input:

==================================================
Input files
==================================================

This page is dedicated to input file of ODAMNet.

.. _targetGenes:

Target genes 
=================

.. warning::

    - Gene IDs have to be **consistent** between input data *(target genes, GMT and networks)*
    - When data are retrieved by queries, **HGNC** IDs are used.

Choose one of these input parameters according your input data:

.. tabs::

    .. group-tab:: chemicals file

        -c, --chemicalsFile FILENAME
            Contains a list of chemicals. They have to be in **MeSH** identifiers (e.g. D014801).
            Each line contains one or several chemical IDs, separated by ";".

    .. group-tab:: target genes file

        -t, --targetGenesFile FILENAME
            Contains a list of target genes of interest. One target gene per line.

    .. group-tab:: CTD file

        --CTD_file FILENAME
            It's a tab-separated file and contains results of query sent to CTD.
            This file is created automatically when you give a chemicals file.

.. _chemicalsFile:

1. Chemicals file
---------------------

By default, ODAMNet retrieved chemical target genes list from the |ctd|_ [1]_ (CTD) using queries.
This file contains a list of chemicals IDs (**MeSH**, e.g. D014801). Each line contains one or several chemical IDs,
separated by ";".

.. code-block:: none

    D014801;D014807
    D014212
    C009166

ODAMNet approaches are applied in each line separately. If a line contains multiple chemicals, target genes of each
chemical will be retrieved and merged as unique target genes list.

Chemical target genes are retrieved in **HGCN** format.

.. _targetgenesfile:

2. Target genes file
---------------------

ODAMNet can also used input data provided by the user. This target genes file contains a list of genes. One gene per
line.

.. code-block:: none

    AANAT
    ABCB1
    ABCC2
    ABL1
    ACADM

.. _CTD_file:

3. CTD file
--------------

This third way to retrieved target genes is well appropriate to do **reproducible analysis** or to use a specific
**database version**. The required file contains 9 columns:

- ``Input``: query input (e.g chemical IDs from chemicals file)
- ``ChemicalName``: name of the query input or its descendant chemicals
- ``ChemicalId``: MeSH ID of the query or its descendant chemicals
- ``CasRN``: CasRN ID of the query or its descendant chemicals
- ``GeneSymbol``: names of target genes that are connected to the query or its descendant chemicals
- ``GeneId``: target gene ID (HGCN)
- ``Organism``: organism name
- ``OrganismId``: organism ID
- ``PubMedIds``: PubMed IDs of publications that talk about this connection

.. code-block:: none

    Input	ChemicalName	ChemicalId	CasRN	GeneSymbol	GeneId	Organism	OrganismId	PubMedIds
    d014801	Tretinoin	D014212	302-79-4	ZYG11A	440590	Homo sapiens	9606	23724009|33167477
    d014801	Tretinoin	D014212	302-79-4	ZYX	7791	Homo sapiens	9606	23724009
    d014801	Tretinoin	D014212	302-79-4	ZZZ3	26009	Homo sapiens	9606	33167477
    d014801	Vitamin A	D014801	11103-57-4	ACE2	59272	Homo sapiens	9606	32808185
    d014801	Vitamin A	D014801	11103-57-4	AKR1B10	57016	Homo sapiens	9606	19014918

This kind of files is created as query results with query mode of ODAMNet.

.. _pathways:

Pathways/processes of interest
=================================

By default, ODAMNet retrieved all rare disease pathways and all human pathways from |wp|_ [2]_ using queries. Genes
involved in rare disease pathways are retrieved in **HGCN** format.

Moreover, the user can also provide their own pathways/processes of interest. Two types of files are required by
ODAMNet:

--GMT FILENAME
    It's a tab-delimited file that describes gene sets of pathways/processes of interest. Pathways can come
    from several sources. Each row represents a gene set.

--backgroundFile FILENAME
    This file contains the list of the different background file source. They have to be in the same order that they
    appear on the GMT file. Each file is a GMT file (see above).

.. _GMTFile:

GMT file
--------------

This file contains genes composition of the pathways/processes of interest. There are at least three columns:

- ``pathwayIDs``: first column is pathway IDs
- ``pathways``: second column is pathway names - Optional, you can fill it in a dummy field
- ``HGNC``: all the other columns contain genes inside pathway. The number of columns is different for each pathway and
  varies according the number of genes inside.

The GMT file is organized as follow:

.. code-block:: none

    pathwayIDs 	pathways	HGNC
    WP5195	Disorders in ketolysis	ACAT1	HMGCS1	OXCT1	BDH1	ACAT2
    WP5189	Copper metabolism	ATP7B	ATP7A	SLC11A2	SLC31A1
    WP5190	Creatine pathway	GAMT	SLC6A8	GATM	OAT	CK

For more details, see |gmt|_ webpage.

.. warning::

    :octicon:`alert;2em` GMT file **must doesn't** contain **empty columns**.

.. _bgFile:

Background file
------------------

In addition to the GMT file, ODAMNet needs another GMT file used as background genes for statistical approaches. It can
used different background genes at the same time. So, instead of given directly the background GMT file, ODAMNet takes
as input the list of background file name.

.. code-block:: none

    hsapiens.GO-BP.name.gmt
    hsapiens.REAC.name.gmt
    hsapiens.REAC.name.gmt
    hsapiens.GO-BP.name.gmt
    hsapiens.WP.name.gmt

Background file contains same line number as GMT file and background file names are in the same order that they are in
the GMT file.

Examples
------------------

Background and GMT files need to be in the same folder.

.. tabs::

    .. group-tab:: One background genes

        Three lines of WP background file

        .. code-block:: none

            hsapiens.WP.name.gmt
            hsapiens.WP.name.gmt
            hsapiens.WP.name.gmt


    .. group-tab:: Several background genes

        Five lines of background files. Same order than in the corresponding GMT file.

        .. code-block:: none

            hsapiens.GO-BP.name.gmt
            hsapiens.REAC.name.gmt
            hsapiens.REAC.name.gmt
            hsapiens.GO-BP.name.gmt
            hsapiens.WP.name.gmt


.. tabs::

    .. group-tab:: One background genes

        Three lines of WP pathways

        .. code-block:: none

            pathwayIDs 	pathways	HGNC
            WP5195	Disorders in ketolysis	ACAT1	HMGCS1	OXCT1	BDH1	ACAT2
            WP5189	Copper metabolism	ATP7B	ATP7A	SLC11A2	SLC31A1
            WP5190	Creatine pathway	GAMT	SLC6A8	GATM	OAT	CK

    .. group-tab:: Several background genes

        Five pathways of interest. Same order than in the background file.

        .. code-block:: none

            pathwayIDs 	pathways	HGNC
            GO:0072001	renal system development	CYP26B1	CFLAR	PLXND1	HOXA11	SOX8
            REAC:R-HSA-8853659	RET signaling	GAB2	PIK3CB	PRKACA	RAP1GAP	DOK5
            REAC:R-HSA-157118	Signaling by NOTCH	PLXND1	CREBBP	PSMB1	PSMC4	MAMLD1
            GO:0060993	kidney morphogenesis	HOXA11	SOX8	PKD1	WWTR1	FGF10
            WP:WP4830	GDNF/RET signalling axis	IFT27	FOXC2	GFRA1	AGTR2	EYA1

Networks
===========================

In ODAMNet, two mains network format file are used:

- Simple interaction file (SIF)
- Graph file (GR)

.. _SIF:

SIF file
----------

This network format is used in the :doc:`../approaches/methods_AMI` (AMI) approach. The SIF file contains three
columns: source node, interaction type and target node with header. It's a tab-separated file.

.. code-block:: none

    node_1      link    node_2
    AAMP        ppi     VPS52
    AAMP        ppi     BHLHE40
    AAMP        ppi     AEN
    AAMP        ppi     C8orf33
    AAMP        ppi     TK1

For more details, see |sifNet|_ webpage.

.. _GR:

GR file
----------

This network format is used in the :doc:`../approaches/methods_RWR` (RWR) approach. The GR format contains two columns:
source node and target node, without header. It's a tab-separated file.

.. code-block:: none

    NFYA	NFYB
    NFYA	NFYC
    NFYB	NFYC
    BTRC	CUL1
    BTRC	SKP1

.. _configFile:

Configuration file
=====================

.. warning::

    :octicon:`alert;2em` Follow the same **folder tree** used in multiXrank

To perform a RWR, multiXrank [3]_ needs a configuration file as input. This file contains path of networks used. It
could be short (see bellow) or very detailed with parameters.

For more details about this file, see the multiXrank's documentation:
:octicon:`mark-github;1em` `Github <https://github.com/anthbapt/multixrank>`_ /
:octicon:`book;1em` `Documentation <https://multixrank-doc.readthedocs.io/en/latest/>`_.

This is an example of short configuration file:

.. tabs::

    .. group-tab:: Pathways/processes of interest network

        .. code-block:: bash
            :emphasize-lines: 9,11

             multiplex:
                 1:
                     layers:
                         - multiplex/1/Complexes_gene_names_190123.gr
                         - multiplex/1/Pathways_reactome_gene_names_190123.gr
                         - multiplex/1/PPI_HiUnion_LitBM_APID_gene_names_190123.gr
                 2:
                     layers:
                         - multiplex/2/RareDiseasePathways_network_useCase1.gr
             bipartite:
                 bipartite/Bipartite_RareDiseasePathways_geneSymbols_useCase1.gr:
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
                        - multiplex/1/Complexes_gene_names_190123.gr
                        - multiplex/1/Pathways_reactome_gene_names_190123.gr
                        - multiplex/1/PPI_HiUnion_LitBM_APID_gene_names_190123.gr
                2:
                    layers:
                        - multiplex/2/DiseaseSimilarity_network_2022_06_11.gr
            bipartite:
                bipartite/Bipartite_genes_to_OMIM_2022_09_27.gr:
                    source: 2
                    target: 1
            seed:
                seeds.txt

.. tip::

    Whatever the networks used, the **command line is the same**. You have to **change** the network name inside the
    **configuration file**.

References
=============

.. [1] Davis AP, Grondin CJ, Johnson RJ *et al.*. The Comparative Toxicogenomics Database: update 2021. Nucleic acids research. 2021.
.. [2] Martens M, Ammar A, Riutta A *et al.*. WikiPathways: connecting communities. Nucleic acids research. 2021.
.. [3] Baptista A, Gonzalez A & Baudot A. Universal multilayer network exploration by random walk with restart. Communications Physics. 2022.

.. _ctd: http://ctdbase.org/
.. |ctd| replace:: **the Comparative Toxicogenomics Database**
.. _wp: https://www.wikipathways.org/
.. |wp| replace:: **WikiPathways**
.. _gmt: https://software.broadinstitute.org/cancer/software/gsea/wiki/index.php/Data_formats#GMT:_Gene_Matrix_Transposed_file_format_.28.2A.gmt.29
.. |gmt| replace:: GMT file format
.. _sifNet: http://wiki.biouml.org/index.php/SIF_(file_format)
.. |sifNet| replace:: SIF file format