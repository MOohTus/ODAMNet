==================================================
Output files
==================================================

.. _requestOutput:

Request file results
==================================================

.. _CTDrequestOuput:

CTD request file results
--------------------------

When you request CTD to extract the target genes, two files are created, whatever the approach you choose.

CTD_request_MeSHID_DATE.tsv
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This file contains the results from the request sent to CTD.

CTD_requestFiltered_MeSHID_DATE.tsv
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This file has the same format as the file before but it contains the filtered data. This file can be filtered using the
publication number associated to an interaction between chemical and gene (``--nbPub`` parameter).
These filtered data are used for the analysis.

- ``Input``: chemical query name (from the chemical file)
- ``ChemicalName``: name of the query input or its child chemicals
- ``ChemicalId``: MeSH ID of the query or its child chemicals
- ``CasRN``: CasRN ID of the query or its child chemicals
- ``GeneSymbol``: gene symbol that is connected to the query or its child chemicals
- ``GeneId``: gene ID of this gene (HGCN)
- ``Organism``: organism name where comes from the gene
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

*The file name is composed of the MeSHID that corresponds to the query chemical and of the DATE of the request (aaaa_mm_dd).*

.. _WPrequestOuput:

WP request file results
--------------------------

When you request WikiPathways to extract the Rare Diseases pathways, two files are created whatever the approach chosen.

WP_RareDiseases_request_DATE.gmt
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This file contains the results of the request sent to WikiPathways. All the disease pathways labeled as Rare Diseases are
extracted and save into this GMT file.

GMT file is a tab-separated file:

- ``pathwayIDs``: first column is the WikiPathways ID
- ``pathways``: second column is the name of the WikiPathways
- ``HGNC``: all the other columns contain genes inside the WikiPathways. The number of columns is different for each
  pathways and varies according the number of genes inside.

An example of GMT is displayed below:

.. code-block:: none

    pathwayIDs	pathways	HGNC
    WP5195	Disorders in ketolysis	ACAT1	HMGCS1	OXCT1	BDH1	ACAT2
    WP5189	Copper metabolism	ATP7B	ATP7A	SLC11A2	SLC31A1
    WP5190	Creatine pathway	GAMT	SLC6A8	GATM	OAT	CK

WP_allPathways_request_DATE.gmt
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This GMT file contains all the human disease pathways from WikiPathways. The  format is similar at the previous one.

*The file name is composed of the *DATE* of the request (aaaa_mm_dd).*

.. _overlapOutput:

Overlap analysis
==================================================

Only one file is created with this approach.

Overlap_MeSHID_withRDWP.csv
------------------------------

This file contains the results of the overlap analysis. The number of this file depends of the number of chemicals given as input
(i.e. chemicals file). IN the file name, the *MeSHID* name corresponds on the chemical used.

- ``PathwayIDs``: Pathway ID
- ``PathwayNames``: Pathway name
- ``PathwayBackgroundNames``: Source of the pathway (e.g. Wikipathways)
- ``PathwaySizes``: Number of genes inside the pathway
- ``TargetSize``: Number of genes that interact with chemical and are in the background gene set
- ``IntersectionSize``: Number of target genes that are inside the pathway
- ``BackgroundSizes``: Number of genes in the background gene sets (e.g. genes from all human pathways in WikiPathways)
- ``pValue``: pvalue of the overlap between target genes and pathways of interest (i.e. hypergeometric test)
- ``pAdjusted``: adjusted pvalue (i.e. multitest correction)
- ``Intersection``: list of genes shared between targeted genes and pathway of interest (space-separated)

.. code-block:: none

    PathwayIDs;PathwayNames;PathwayBackgroundNames;PathwaySizes;TargetSize;IntersectionSize;BackgroundSizes;pValue;pAdjusted;Intersection
    WP4940;15q11.2 copy number variation syndrome;WikiPathway_2022_08_01;10;1721;0;12379;1.0;1.0;
    WP4271;Vitamin B12 disorders;WikiPathway_2022_08_01;13;1721;0;12379;1.0;1.0;
    WP4299;Lamin A-processing pathway;WikiPathway_2022_08_01;3;1721;0;12379;1.0;1.0;
    WP4506;Tyrosine metabolism;WikiPathway_2022_08_01;4;1721;0;12379;1.0;1.0;
    WP5223;2q21.1 copy number variation syndrome;WikiPathway_2022_08_01;42;1721;1;12379;0.9981605117974595;1.0;APC
    WP4686;Leucine, isoleucine and valine metabolism;WikiPathway_2022_08_01;24;1721;2;12379;0.8660465002997586;1.0;BCAT1 BCAT2

.. _AMIOutput:

Active Module Identification
==================================================

When you run the Active Module Identification analysis, at least six results files are created. The number depends of the number of Active Modules found.

DOMINO_inputGeneList_MeSHID.txt
----------------------------------

This file contains the list of target genes. There are used as Active Genes for the analysis.

.. code-block:: none

    CCND1
    CDKN1A
    BAD
    ESR1
    KRT18

Overlap_AM_X_MeSHID_withRDWP.csv
-----------------------------------

This is the result file of the overlap analysis. The number of this file depends of the number of Active Modules found.
In the file name, the *X* represents the AM number. See the :ref:`Overlap output <overlapOutput>` part for more details.

DOMINO_MeSHID_overlapAMresults4Cytoscape.txt
----------------------------------------------

This file is created to be given to Cytoscape for the visualisation. It contains five columns:

- ``geneSymbol``: gene HCGN ID
- ``AM_number``: Active module number
- ``termID``: pathway/process ID (e.g. GO, WP, Reactome etc ...)
- ``termTitle``: pathway/process name
- ``overlap_padj``: overlap adjusted pvalue

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

DOMINO_MeSHID_activeModulesNetwork.txt
----------------------------------------

This file contains details of each AM found. It contains four columns:

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

DOMINO_MeSHID_activeModulesNetworkMetrics.txt
-----------------------------------------------

Some metrics are calculated such as number of edges and nodes for each AM identified.

- ``AMINumber``: active module number
- ``EdgesNumber``: number of edges in the AM
- ``NodesNumber`` : number of nodes in the AM
- ``ActiveGenesNumber``: number of active genes (target genes)

.. code-block:: none

    AMINumber	EdgesNumber	NodesNumber	ActiveGenesNumber
    1	357	93	35
    2	246	69	27
    3	135	66	26

DOMINO_MeSHID_activeModules.txt
----------------------------------

This file is created to be given to Cytoscape for the visualisation. It contains four columns :

- ``GeneSymbol`` : Gene symbol
- ``ActiveModule`` : active module number
- ``ActiveGene`` : True if the gene was used as active gene
- ``overlapSignificant`` : True if the AM has significant overlap results

.. code-block:: none

    geneSymbol	ActiveModule	activeGene	overlapSignificant
    NPAT	1	False	False
    CCNA1	1	True	False
    CDC6	1	True	False
    B3GALNT1	1	False	False
    USP26	1	False	False

*The file name is composed of the MeSHID that corresponds to the query chemical*

Random Walk with Restart analysis
=======================================

config_minimal.yml and seeds.txt
------------------------------------

These two files are copies of configuration and seed files used in input. For more details of the config file format see
the [:ref:`FORMAT <configFile>`] part. Seeds file contains target genes used as seeds for the walk.

multiplex_X.tsv
------------------

The number of this file depends on the number of multiplex you give in input. IN the name, the *X* corresponds to the folder name of the
multiplex. It contains three columns:

- ``multiplex``: multiplex folder name
- ``node``: name of node inside the multiplex (e.g. target genes, pathways ...)
- ``score``: score calculated by the walk

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

resultsNetwork_useCase1.sif
---------------------------------

The name of this network file depends on what you give in input (``--sifFileName``). See :ref:`RWR` for more details.
It's a SIF file format [:ref:`FORMAT <SIF>`] and contains three columns:

- ``source node``: node names
- ``link source``: source of the link (which multiplex or bipartite)
- ``target node``: node names

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