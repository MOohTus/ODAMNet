.. _input:

==================================================
Input files
==================================================

.. _query:

Target genes input files
==================================================

mettre un truc sur les formats des genes que ctd ça donne les genes symbole etc et que pour tous les examples on utilise des genes symboles



.. line-block::

    You have to choose from where data source come from :

        :ref:`factorList` : give chemical ID as input and request CTD
        :ref:`CTDFile` : specific version of data
        :ref:`genesList`

.. _factorList:

1. Environmental factors file
----------------------------------

-f, --factorList FILENAME
    Contains a list of chemicals : MeSH identifier (e.g. D014801).
    The user can gives several chemicals in the same line : they will be grouped for the analysis.

Factor file format : InputFile_factorsList.csv
CSV file where each line contains one or several molecules names.
Molecule name format : name of the molecule or MeSH ID.

The user can give several molecules. One analysis by molecule : each molecule is considering seperately.
The users an give several molecule for the same analysis. On the same line, separated by a ";".

.. code-block:: none

            D014801;D014807
            D014212
            C009166

.. _CTDFile:

2. CTD file
--------------

-c, --CTD_file FILENAME
    It's a tab-separated file from CTD request (e.g. created with an up to date analysis). Refers to XXX to have more information about the format.

This file contains the results from the request sent to CTD.

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

.. _genesList:

3. Genes list file
---------------------

-g, --geneList FILENAME
    List of gens of interest. One gene per line.

.. code-block:: none

    AANAT
    ABCB1
    ABCC2
    ABL1
    ACADM
    ACAN
    ACSL1
    ACTA1
    ACTA2

.. _pathways:

Pathways input files
==================================================

--GMT FILENAME
    It's a tab-delimited file that describes gene sets of pathways of interest. Pathways can come from several sources.
    Each row represents a gene set and there is at least three columns :

        - ``pathwayIDs`` : first column is pathway IDs
        - ``pathways`` : second column is pathway names - Optional, you can fill in a dummy field
        - ``HGNC`` : all the other columns contain genes inside pathway. The number of columns is different for each
          pathway and varies according the number of genes inside.

The GMT file is organized as follow:

.. code-block:: none

    pathwayIDs 	pathways	HGNC
    WP5195	Disorders in ketolysis	ACAT1	HMGCS1	OXCT1	BDH1	ACAT2
    WP5189	Copper metabolism	ATP7B	ATP7A	SLC11A2	SLC31A1
    WP5190	Creatine pathway	GAMT	SLC6A8	GATM	OAT	CK

More details for `GMT file format <https://software.broadinstitute.org/cancer/software/gsea/wiki/index.php/Data_formats#GMT:_Gene_Matrix_Transposed_file_format_.28.2A.gmt.29>`_

--backgroundFile FILENAME
    Name list of the different background source (each background contain the list of all genes). Each file is a GMT
    file (see the previous parameter)
    Same order than the pathways of interest file.

.. code-block:: none

    hsapiens.GO-BP.name.gmt
    hsapiens.REAC.name.gmt
    hsapiens.REAC.name.gmt
    hsapiens.REAC.name.gmt
    hsapiens.GO-BP.name.gmt
    hsapiens.WP.name.gmt


.. _net:

Network input files
==================================================

SIF format : Simple Interaction Format
One interaction by row
Three columns : source node, relationship type and target node
Tab-delimited file

http://wiki.biouml.org/index.php/SIF_(file_format)


For AMI analysis
Give the recommendations from DOMINO and the link to them

-n, --networkFile FILENAME
    Network file name (e.g. PPI network).
    The file contains 3 columns such as SIF format with the source node, the interaction type and the target node.

.. code-block:: none

    node_1	link	node_2
    AAMP	ppi	VPS52
    AAMP	ppi	BHLHE40
    AAMP	ppi	AEN
    AAMP	ppi	C8orf33
    AAMP	ppi	TK1

Random walk input files
==================================================

.. _configFile:

--configPath PATH
    Configuration file required by multiXrank tool. It could be short or very details (g.e. with tuned parameters).
    The short one contains the network and bipartite trees and the path of the seed file.
    If the user want more details go the the multiXrank's documentation :
    `github <https://github.com/anthbapt/multixrank>`__ /
    `doc <https://multixrank-doc.readthedocs.io/en/latest/>`__

**configPath format**

.. code-block:: none

    multiplex:
        1:
            layers:
                - examples/InputData/multiplex/1/Complexes_Nov2020.gr
                - examples/InputData/multiplex/1/PPI_Jan2021.gr
                - examples/InputData/multiplex/1/Reactome_Nov2020.gr
        2:
            layers:
                - examples/InputData/multiplex/2/WP_RareDiseasesNetwork_fromVitaminPaper.sif
    bipartite:
        examples/InputData/bipartite/Bipartite_WP_RareDiseases_geneSymbols_fromVitaminPaper.tsv:
            source: 2
            target: 1
    seed:
        examples/InputData/seeds.txt


**layers and bipartites format**

.. code-block:: none

    NFYA	NFYB
    NFYA	NFYC
    NFYB	NFYC
    BTRC	CUL1
    BTRC	SKP1


**seed format**

.. code-block:: none

    AANAT
    ABCB1
    ABCC2
    ABL1
    ACADM


.. _simpleFile:

list of genes file format