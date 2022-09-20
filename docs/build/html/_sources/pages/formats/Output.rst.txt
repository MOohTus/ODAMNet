==================================================
Output files
==================================================

.. _requestOutput:

Request file results
==================================================

**CTD_request_MeSHID_DATE.tsv**
This file contains the results from the request sent to CTD.

**CTD_requestFiltered_MeSHID_DATE.tsv**

This file has the same format as the file before but it contains the filtered data. The data could be filtered by the
number of paper for an interaction between gene and molecule. This filtered data is used for the analysis.

- ``Input`` : query input (from the factor input file)
- ``ChemicalName`` : name of the query input or its descendant
- ``ChemicalId`` : MeSH ID of the query or its descendant
- ``CasRN`` : CasRN ID of the query or its descendant
- ``GeneSymbol`` : gene symbol that is connected to the query or its descendant
- ``GeneId`` : gene ID of this gene (HGCN)
- ``Organism`` : organism name that comes from the gene
- ``OrganismId`` : organism ID
- ``PubMedIds`` : PubMed IDs of the paper that talk about this connection

.. code-block:: none

    Input	ChemicalName	ChemicalId	CasRN	GeneSymbol	GeneId	Organism	OrganismId	PubMedIds
    d014801	Tretinoin	D014212	302-79-4	ZXDC	79364	Homo sapiens	9606	33167477
    d014801	Tretinoin	D014212	302-79-4	ZYG11A	440590	Homo sapiens	9606	23724009|33167477
    d014801	Tretinoin	D014212	302-79-4	ZYX	7791	Homo sapiens	9606	23724009
    d014801	Tretinoin	D014212	302-79-4	ZZZ3	26009	Homo sapiens	9606	33167477
    d014801	Vitamin A	D014801	11103-57-4	ACE2	59272	Homo sapiens	9606	32808185
    d014801	Vitamin A	D014801	11103-57-4	AKR1B1	231	Homo sapiens	9606	19014918
    d014801	Vitamin A	D014801	11103-57-4	AKR1B10	57016	Homo sapiens	9606	19014918

**WP_RareDiseases_request_DATE.gmt**
This file contains the results of the request sent to WikiPathways. All the disease pathways labeled as Rare Diseases are
extracted and save into this GMT file.

**WP_allPathways_request_DATE.gmt**
This GMT file contains all the human disease pathways from WikiPathways. Format is similar at the previous one.

GMT file is a tab-separated file :

- ``WPID`` : first column is the WikiPathways ID
- ``pathways`` : second column is the name of the WikiPathways
- ``HGNC`` : all the other columns contain genes inside the WikiPathways. The number of columns is different for each
  pathways and varies according the nuber of genes inside.

.. code-block:: none

    WPID	pathways	HGNC
    WP5195	Disorders in ketolysis	ACAT1	HMGCS1	OXCT1	BDH1	ACAT2
    WP5189	Copper metabolism	ATP7B	ATP7A	SLC11A2	SLC31A1
    WP5190	Creatine pathway	GAMT	SLC6A8	GATM	OAT	CK

.. _overlapOutput:

Overlap output files
==================================================

**Overlap_MeSHID_withRDWP.csv**

This is the result file of the overlap analysis. The number of this file depends of the number of molecule given as input
(i.e. the factor input file).

- ``WPID`` : Pathway ID
- ``WPTitle`` : Pathway name
- ``Source`` : Source of the pathway (g.e. Wikipathways)
- ``WPSize`` : Number of genes inside the pathway
- ``TargetSize`` : Number of genes that interact with the input molecule and are in the background gene set
- ``IntersectionSize`` : Number of targeted genes that are inside the pathway
- ``UniversSize`` : Number of genes in the background gene sets (g.e. genes from all human pathways in WikiPathways)
- ``pValue`` : pvalue of the overlap between targeted genes and pathways of interest (i.e. hypergeometric test)
- ``pAdjusted`` : adjusted pvalue (i.e. multitest correction)
- ``Intersection`` : list of genes sharded between targeted genes and pathway of interest (space-separated)

.. code-block:: none

    WPID;WPTitle;Source;WPSize;TargetSize;IntersectionSize;UniversSize;pValue;pAdjusted;Intersection
    WP4940;15q11.2 copy number variation syndrome;WikiPathway_2022_08_01;10;1721;0;12379;1.0;1.0;
    WP4271;Vitamin B12 disorders;WikiPathway_2022_08_01;13;1721;0;12379;1.0;1.0;
    WP4299;Lamin A-processing pathway;WikiPathway_2022_08_01;3;1721;0;12379;1.0;1.0;
    WP4506;Tyrosine metabolism;WikiPathway_2022_08_01;4;1721;0;12379;1.0;1.0;
    WP5223;2q21.1 copy number variation syndrome;WikiPathway_2022_08_01;42;1721;1;12379;0.9981605117974595;1.0;APC
    WP4686;Leucine, isoleucine and valine metabolism;WikiPathway_2022_08_01;24;1721;2;12379;0.8660465002997586;1.0;BCAT1 BCAT2

.. _AMIOutput:

Active Module Identification
==================================================

**DOMINO_inputGeneList_D014801.txt**

.. code-block:: none

    CCND1
    CDKN1A
    BAD
    ESR1
    KRT18


**Overlap_AM_1_D014801_withRDWP.csv**
Cf. file overlap analysis

**DOMINO_D014801_overlapAMresults4Cytoscape.txt**

- ``geneSymbol`` : gene HCGN ID
- ``AM_number`` : Active module number
- ``termID`` : term ID (g.e. GO, WP, Reactome etc ...)
- ``termTitle`` : term name
- ``overlap_padj`` : overlap adjusted pvalue

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

**DOMINO_D014801_activeModulesNetwork.txt**

- ``source`` : node 1
- ``target`` : node 2
- ``link`` : kind of link
- ``AMI_number`` : active module number

.. code-block:: none

    source	target	link	AMI_number
    CDT1	MCM6	ppi	1
    CDT1	CDK1	ppi	1
    CDT1	ORC1	ppi	1
    CDT1	MCM2	ppi	1
    CDT1	GMNN	ppi	1

**DOMINO_D014801_activeModulesNetworkMetrics.txt**

- ``AMINumber`` : active module number
- ``EdgesNumber`` : Number of edges in the AM
- ``NodesNumber`` : Number of nodes in the AM
- ``activeGenesNumber`` : Number of active genes (target genes)

.. code-block:: none

    AMINumber	EdgesNumber	NodesNumber	activeGenesNumber
    1	357	93	35
    2	246	69	27
    3	135	66	26


**DOMINO_D014801_activeModules.txt**

- ``geneSymbol`` : Gene symbol
- ``ActiveModule`` : active module number
- ``activeGene`` : True if the gene was used as active gene
- ``overlapSignificant`` : True if the AM has significant overlap results

.. code-block:: none

    geneSymbol	ActiveModule	activeGene	overlapSignificant
    NPAT	1	False	False
    CCNA1	1	True	False
    CDC6	1	True	False
    B3GALNT1	1	False	False
    USP26	1	False	False



Random Walk analysis
==================================================

Network creation
==================================================




mettre en note ??
*MeSHID :*
*DATE : aaaa_m_d*