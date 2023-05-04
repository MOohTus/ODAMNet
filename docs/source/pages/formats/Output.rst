==================================================
Output files
==================================================

This page is dedicated to output files created by ODAMNet, grouped by:

- Query result files
- Overlap analysis result files
- Active module identification (AMI) result files
- Random walk with restart (RWR) result files

.. _queryOutput:

Query output files
=====================

By default, ODAMNet retrieved input data from databases using queries. Chemical target genes are retrieved from
|ctd|_ [1]_ (CTD). Rare disease pathways are retrieved from |wp|_ [2]_. And biological networks are also downloaded from
|ndex|_ [3]_.

It implies creation of output files that contain results of these queries.

.. _CTDOutput:

CTD query output files
--------------------------

Chemical target genes are retrieved from CTD. Two files are created:

.. tabs::

    .. group-tab:: ``CTD_request_MeSHID_DATE.tsv``

        This file contains the **raw query results**.

    .. group-tab:: ``CTD_requestFiltered_MeSHID_DATE.tsv``

        This file contains the **filtered query results**. You can filter raw query results according the number of
        publication associated to a chemical - gene association (``--nbPub`` parameter). This file is used for the
        analysis.

These two files have the same format:

- ``Input``: chemical query name (from the chemical file)
- ``ChemicalName``: name of the query input or its descendant chemicals
- ``ChemicalId``: MeSH ID of the query or its descendant chemicals
- ``CasRN``: CasRN ID of the query or its descendant chemicals
- ``GeneSymbol``: target gene name that is connected to the query or its descendant chemicals
- ``GeneId``: target gene ID (HGCN)
- ``Organism``: organism name where comes from the target gene
- ``OrganismId``: organism ID
- ``PubMedIds``: PubMed IDs of the publication associated to this connection

This is an example of this file:

.. code-block:: none

    Input	ChemicalName	ChemicalId	CasRN	GeneSymbol	GeneId	Organism	OrganismId	PubMedIds
    d014801	Tretinoin	D014212	302-79-4	ZXDC	79364	Homo sapiens	9606	33167477
    d014801	Tretinoin	D014212	302-79-4	ZYG11A	440590	Homo sapiens	9606	23724009|33167477
    d014801	Tretinoin	D014212	302-79-4	ZYX	7791	Homo sapiens	9606	23724009
    d014801	Tretinoin	D014212	302-79-4	ZZZ3	26009	Homo sapiens	9606	33167477
    d014801	Vitamin A	D014801	11103-57-4	ACE2	59272	Homo sapiens	9606	32808185
    d014801	Vitamin A	D014801	11103-57-4	AKR1B1	231	Homo sapiens	9606	19014918
    d014801	Vitamin A	D014801	11103-57-4	AKR1B10	57016	Homo sapiens	9606	19014918

*The file name is composed of the MeSHID and DATE that correspond to the query chemical and the query date*
*(aaaa_mm_dd) respectively.*

.. _WPOuput:

WikiPathways query output files
-----------------------------------

Rare disease pathways are retrieved from WikiPathways. Two GMT files are created:

.. tabs::

    .. group-tab:: ``WP_RareDiseases_request_DATE.gmt``

        This file contains the **rare disease pathways** in :ref:`GMT format <GMTFile>`.

    .. group-tab:: ``WP_allPathways_request_DATE.gmt``

        This file contains the **human disease pathways** in :ref:`GMT format <GMTFile>`.

GMT file is a tab-separated file:

- ``pathwayIDs``: first column is the WikiPathways ID
- ``pathways``: second column is the name of the WikiPathways
- ``HGNC``: all the other columns contain genes inside the WikiPathways. The number of columns is different for each
  pathways and varies according the number of genes inside.

This is an example of this file:

.. code-block:: none

    pathwayIDs	pathways	HGNC
    WP5195	Disorders in ketolysis	ACAT1	HMGCS1	OXCT1	BDH1	ACAT2
    WP5189	Copper metabolism	ATP7B	ATP7A	SLC11A2	SLC31A1
    WP5190	Creatine pathway	GAMT	SLC6A8	GATM	OAT	CK

*The file name is composed of the query DATE (aaaa_mm_dd).*

NDEx query output files
-------------------------

There are two ways to download biological network from NDEx in ODAMNet.

The first one is when you apply the active module identification (AMI) approach. You can use a biological network
directly downloaded from NDEx. You need to provide the ``--netUUID`` identifier. A :ref:`SIF <SIF>` file will be
created. See :doc:`../approaches/methods_AMI` page for more details.

The second one is using the ``networkDownloading`` function. Providing the ``--netUUID`` identifier, you can download
biological networks in both :ref:`SIF <SIF>` and :ref:`GR <GR>` format. See :doc:`../network/NetworkDownloading` page
for more details.

.. tabs::

    .. group-tab:: GR format

        .. code-block:: none

            MMP11	PRPF40A
            ASB16-AS1	SHBG
            KIAA0513	INTS4
            KIAA0513	HAX1
            RAVER2	PTBP1

    .. group-tab:: SIF format

        .. code-block:: none

            node_1	link	node_2
            MMP11	interacts with	PRPF40A
            ASB16-AS1	interacts with	SHBG
            KIAA0513	interacts with	INTS4
            KIAA0513	interacts with	HAX1
            RAVER2	interacts with	PTBP1

.. _overlapOutput:

Overlap analysis output files
================================

In the Overlap analysis, only one type of file is created: ``Overlap_*.csv``. Number of result files depends of the
chemical number given in the chemicals file.

This file contains ten columns:

- ``PathwayIDs``: Pathway ID
- ``PathwayNames``: Pathway name
- ``PathwayBackgroundNames``: Source of the pathway (e.g. Wikipathways)
- ``PathwaySizes``: Number of genes inside the pathway
- ``TargetSize``: Number of target genes (i.e. that interact with chemical) that are in the background gene set
- ``IntersectionSize``: Number of target genes that are inside the pathway
- ``BackgroundSizes``: Number of genes in the background gene sets (e.g. genes from all human pathways in WikiPathways)
- ``pValue``: pvalue of the overlap between target genes and pathways/processes of interest (i.e. hypergeometric test)
- ``pAdjusted``: adjusted pvalue (i.e. multitest correction)
- ``Intersection``: list of genes shared between targeted genes and pathways/processes of interest (space-separated)

This is an example of this file:

.. code-block:: none

    PathwayIDs;PathwayNames;PathwayBackgroundNames;PathwaySizes;TargetSize;IntersectionSize;BackgroundSizes;pValue;pAdjusted;Intersection
    WP4940;15q11.2 copy number variation syndrome;WikiPathway_2022_08_01;10;1721;0;12379;1.0;1.0;
    WP4271;Vitamin B12 disorders;WikiPathway_2022_08_01;13;1721;0;12379;1.0;1.0;
    WP4299;Lamin A-processing pathway;WikiPathway_2022_08_01;3;1721;0;12379;1.0;1.0;
    WP4506;Tyrosine metabolism;WikiPathway_2022_08_01;4;1721;0;12379;1.0;1.0;
    WP5223;2q21.1 copy number variation syndrome;WikiPathway_2022_08_01;42;1721;1;12379;0.9981605117974595;1.0;APC
    WP4686;Leucine, isoleucine and valine metabolism;WikiPathway_2022_08_01;24;1721;2;12379;0.8660465002997586;1.0;BCAT1 BCAT2

.. cssclass:: italic

    See :doc:`../approaches/methods_overlap` page, :ref:`Use-case 1 overlap analysis <useCase1_overlap>` and
    :ref:`Use-case 2 overlap analysis <useCase2_overlap>` for more details.

.. _AMIOutput:

AMI output files
==================

The ``DOMINO_inputGeneList_*.txt`` file contains the input list of target genes using by DOMINO [4]_.

.. code-block:: none

    CCND1
    CDKN1A
    BAD
    ESR1
    KRT18

The three following files contain results of the **AMI analysis**. They give information about the identified active
modules.

.. tabs::

    .. group-tab:: ``*_activeModulesNetwork.txt``

        This file contains **details** about each identified active module found. It contains four columns:

        - ``source``: node 1
        - ``target``: node 2
        - ``link``: kind of link
        - ``AMI_number``: active module number

        This is an example of the file:

        .. code-block:: none

            source	target	link	AMI_number
            CDT1	MCM6	ppi	1
            CDT1	CDK1	ppi	1
            CDT1	ORC1	ppi	1
            CDT1	MCM2	ppi	1
            CDT1	GMNN	ppi	1

    .. group-tab:: ``*_activeModulesMetrics.txt``

        Some **metrics** are calculated for each identified active module.

        - ``AMINumber``: active module number
        - ``EdgesNumber``: number of edges in the active module
        - ``NodesNumber`` : number of nodes in the active module
        - ``ActiveGenesNumber``: number of target genes

        This is an example of the file:

        .. code-block:: none

            AMINumber	EdgesNumber	NodesNumber	ActiveGenesNumber
            1	357	93	35
            2	246	69	27
            3	135	66	26

    .. group-tab:: ``*_activeModules.txt``

        This file is created to import in **Cytoscape** [5]_ for the visualisation. It contains four columns :

            - ``GeneSymbol`` : Gene name
            - ``ActiveModule`` : active module number
            - ``ActiveGene`` : True if it's target gene
            - ``overlapSignificant`` : True if the active module has significant overlap results

        This is an example of the file:

        .. code-block:: none

            geneSymbol	ActiveModule	activeGene	overlapSignificant
            NPAT	1	False	False
            CCNA1	1	True	False
            CDC6	1	True	False
            B3GALNT1	1	False	False
            USP26	1	False	False

The three following files contain results of the **Overlap analysis** between identified active modules and
pathways/processes of interest.

.. tabs::

    .. group-tab:: ``Overlap_AM_*.csv``

        There are as many overlap files as identified active modules. This file contains the **Overlap analysis results**.
        See :ref:`overlapOutput` for more details.

    .. group-tab:: ``*_signOverlap.txt``

        This file contains the **significant overlap results** between identified active modules and pathways/processes of
        interest. If two overlap are significant in several active modules, the best pvalue is conserved.

        It contains 2 columns: pathways/processes of interest and best adjusted pvalue.

        This is an example of this file:

        .. code-block:: none

            WP5087	2.778369668213874e-25
            WP4541	4.368084017694385e-07
            WP4577	2.839118197421641e-06
            WP5053	1.2298630252448874e-05

    .. group-tab:: ``*_overlapAMresults4Cytoscape.txt``

        This file is created for the visualisation using **Cytoscape** [5]_. It contains five columns:

        - ``geneSymbol``: gene HCGN ID
        - ``AM_number``: Active module number
        - ``termID``: pathway/process ID (e.g. GO, WP, Reactome etc ...)
        - ``termTitle``: pathway/process name
        - ``overlap_padj``: overlap adjusted pvalue

        This is an example of this file:

        .. code-block:: none

            geneSymbol	AM_number	termID	termTitle	overlap_padj
            CEBPA	2	WP4879	Overlap between signal transduction pathways contributing to LMNA laminopathies	0.010978293424676187
            CEBPB	2	WP4879	Overlap between signal transduction pathways contributing to LMNA laminopathies	0.010978293424676187
            JUNB	2	WP4879	Overlap between signal transduction pathways contributing to LMNA laminopathies	0.010978293424676187
            RUNX2	2	WP4879	Overlap between signal transduction pathways contributing to LMNA laminopathies	0.010978293424676187
            CEBPA	2	WP4844	Influence of laminopathies on Wnt signaling	0.027997181221540435
            CEBPB	2	WP4844	Influence of laminopathies on Wnt signaling	0.027997181221540435
            RUNX2	2	WP4844	Influence of laminopathies on Wnt signaling	0.027997181221540435
            CXCL5	6	WP5087	Malignant pleural mesothelioma	4.823470963219471e-11
            FN1	6	WP5087	Malignant pleural mesothelioma	4.823470963219471e-11


.. cssclass:: italic

    See :doc:`../approaches/methods_AMI` page, :ref:`Use-case 1 AMI analysis <useCase1_AMI>` and
    :ref:`Use-case 2 AMI analysis <useCase2_AMI>` for more details.

.. _RWROutput:

RWR output files
==================

In the RWR approach, the ``config_minimal.yml`` and ``seeds.txt`` input files are copy/paste into the output directory
results. See :ref:`configFile` for more details.

The other created files contain RWR results.

.. tabs::

    .. group-tab:: ``multiplex_*.tsv``

        There are as many multiplex output files as multiplexes used in the RWR analysis. It contains **RWR scores** for
        each node and three columns:

        - ``multiplex``: multiplex folder name
        - ``node``: name of node inside the multiplex (e.g. target genes, pathways ...)
        - ``score``: score calculated by the walk

        This is an example of this file:

        .. code-block:: none

            multiplex	node	score
            1	VCAM1	0.0002083975629882177
            1	FN1	0.00020345404504599346
            1	EGFR	0.00020244600248388192
            1	HSP90AB1	0.00020195660880228006
            1	CTNNB1	0.0002014264852242386
            1	TP53	0.00019080205293178928
            1	MED1	0.0001875608976608657
            1	EP300	0.00018540571477254143
            1	SMAD3	0.0001852022345355004

    .. group-tab:: ``UseCase1_RWR_network.sif``

        The name of this network file depends on what you give in input (``--sifFileName``). See :ref:`RWR` for more
        details. This file is created for the visualisation using **Cytoscape** [5]_. This network file is a
        [:ref:`SIF format <SIF>`] and contains three columns:

        - ``source node``: node names
        - ``link source``: source of the link (which multiplex or bipartite)
        - ``target node``: node names

        This is an example of this file:

        .. code-block:: none

            A8K1F4_HUMAN	multiplex/1/PPI_Jan2021.gr	TP53
            A8K251_HUMAN	multiplex/1/PPI_Jan2021.gr	HSP90AB1
            AAK1	multiplex/1/Reactome_Nov2020.gr	EGFR
            AARS	multiplex/1/PPI_Jan2021.gr	FN1
            AARS	multiplex/1/PPI_Jan2021.gr	VCAM1
            AATF	multiplex/1/PPI_Jan2021.gr	SMAD3
            ABCE1	multiplex/1/PPI_Jan2021.gr	VCAM1
            ABCF1	multiplex/1/PPI_Jan2021.gr	FN1
            ABI1	multiplex/1/Reactome_Nov2020.gr	MAPK1
            ABL1	multiplex/1/PPI_Jan2021.gr	EGFR

    .. group-tab:: ``RWR_top20.txt``

        This file contains the list of the **top X of pathways/processes of interests**, according their RWR score.
        You can choose the top number using the ``--top`` parameter.

        This is an example of this file:

        .. code-block:: none

            node	score
            WP5087	0.002847885875091137
            WP4673	0.0009022865859048019
            WP2059	0.0007759015708361376
            WP5124	0.0007759015708361376
            WP4298	0.0007690455140750499

.. cssclass:: italic

    See :doc:`../approaches/methods_RWR` page, :ref:`Use-case 1 RWR analysis <useCase1_RWR>` and
    :ref:`Use-case 2 RWR analysis <useCase2_RWR>` for more details.

References
==============

.. [1] Davis AP, Grondin CJ, Johnson RJ *et al.*. The Comparative Toxicogenomics Database: update 2021. Nucleic acids research. 2021.
.. [2] Martens M, Ammar A, Riutta A *et al.*. WikiPathways: connecting communities. Nucleic acids research. 2021.
.. [3] Pratt D, Chen J, Welker *et al.*. NDEx, the Network Data Exchange. Cell Systems. 2015.
.. [4] Levi H, Elkon R & Shamir R. DOMINO: a network‐based active module identification algorithm with reduced rate of false calls. Molecular systems biology. 2021.
.. [5] Shannon P, Markiel A, Ozier O *et al.*. Cytoscape: a software environment for integrated models of biomolecular interaction networks. Genome research. 2003.

.. _ctd: http://ctdbase.org/
.. |ctd| replace:: **the Comparative Toxicogenomics Database**
.. _wp: https://www.wikipathways.org/
.. |wp| replace:: **WikiPathways**
.. _ndex: https://www.ndexbio.org/
.. |ndex| replace:: **the Network Data Exchange**