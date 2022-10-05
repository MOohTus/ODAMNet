.. _input:

==================================================
Input files
==================================================

.. _query:

Target genes 
=================

.. line-block::

        Two ways exist to extract the list of target genes :

        :ref:`chemicalsFile` : give chemical ID as input and request CTD
        :ref:`targetGenesFile` : gie your own target genes list

.. tip::

   For reproducibility, you can give your own version of CTD file using ``--CTD_file`` [:ref:`FORMAT <CTD_file>`] 

.. _chemicalsFile:

1. Chemicals file 
---------------------

.. tip::

   Target genes are extracted from CTD and WP in HGCN format


-c, --chemicalsFile FILENAME
    Contains a list of chemicals. They have to be in MeSH identifiers (e.g. D014801).
    Each line contains one or several chemical IDs, seperated by ";".  

.. code-block:: none

            D014801;D014807
            D014212
            C009166

.. _targetGenesFile:

2. Genes list file
---------------------

-t, --targetGenesFile FILENAME
    List of target genes of interest. One gene per line.

.. code-block:: none

    AANAT
    ABCB1
    ABCC2
    ABL1
    ACADM


.. _CTD_file:

3. CTD file
--------------

--CTD_file FILENAME
    It's a tab-separated file and contains results of request sent to CTD.
    This file is created automatically when you give a chemicals file. 

There are 9 columns : 

- ``Input`` : query input (e.g chemical IDs from chemicals file)
- ``ChemicalName`` : name of the query input or its child molecule
- ``ChemicalId`` : MeSH ID of the query or its child molecule
- ``CasRN`` : CasRN ID of the query or its child molecule
- ``GeneSymbol`` : symbol of genes connected to the query or its child molecule
- ``GeneId`` : gene ID (HGCN)
- ``Organism`` : organism name 
- ``OrganismId`` : organism ID
- ``PubMedIds`` : PubMed IDs of the paper that talk about this connection

.. code-block:: none

    Input	ChemicalName	ChemicalId	CasRN	GeneSymbol	GeneId	Organism	OrganismId	PubMedIds
    d014801	Tretinoin	D014212	302-79-4	ZYG11A	440590	Homo sapiens	9606	23724009|33167477
    d014801	Tretinoin	D014212	302-79-4	ZYX	7791	Homo sapiens	9606	23724009
    d014801	Tretinoin	D014212	302-79-4	ZZZ3	26009	Homo sapiens	9606	33167477
    d014801	Vitamin A	D014801	11103-57-4	ACE2	59272	Homo sapiens	9606	32808185
    d014801	Vitamin A	D014801	11103-57-4	AKR1B10	57016	Homo sapiens	9606	19014918


.. _pathways:

Pathways of interest input files
==================================================

By default, WP is automatically requested to extract Rare Diseases pathways. Moreover, you can give your own 
pathways/processes of interest (``--GMT``). You need to provided the source of them too (``backgroundFile``). 

--GMT FILENAME
    It's a tab-delimited file that describes gene sets of pathways of interest. Pathways can come from several sources.
    Each row represents a gene set.

There is at least, three columns : 

- ``pathwayIDs`` : first column is pathway IDs
- ``pathways`` : second column is pathway names - Optional, you can fill in a dummy field
- ``HGNC`` : all the other columns contain genes inside pathway. The number of columns is different for each pathway and varies according the number of genes inside.

The GMT file is organized as follow:

.. code-block:: none

    pathwayIDs 	pathways	HGNC
    WP5195	Disorders in ketolysis	ACAT1	HMGCS1	OXCT1	BDH1	ACAT2
    WP5189	Copper metabolism	ATP7B	ATP7A	SLC11A2	SLC31A1
    WP5190	Creatine pathway	GAMT	SLC6A8	GATM	OAT	CK

More details for `GMT file format <https://software.broadinstitute.org/cancer/software/gsea/wiki/index.php/Data_formats#GMT:_Gene_Matrix_Transposed_file_format_.28.2A.gmt.29>`_

--backgroundFile FILENAME
    This file contains the list of the different background file source. They have to be in the same order that they 
    appear on the GMT file. Each file is a GMT file (see above). 

.. code-block:: none

    hsapiens.GO-BP.name.gmt
    hsapiens.REAC.name.gmt
    hsapiens.REAC.name.gmt
    hsapiens.GO-BP.name.gmt
    hsapiens.WP.name.gmt


.. tip::

   Theses parameters, ``--GMT`` and ``--backgroundFile`` can use for reproducibility. You can give a GMT file from WP request results.

.. _AMIinput:

Active Module Identification
=================================


.. _SIF:

-n, --networkFile FILENAME
    Network file name in SIF (Simple Interaction File) format. 
    It's a tab-delimited file.

There are three columns : source node, interaction type, target node. 

.. code-block:: none

    node_1      link    node_2
    AAMP        ppi     VPS52
    AAMP        ppi     BHLHE40
    AAMP        ppi     AEN
    AAMP        ppi     C8orf33
    AAMP        ppi     TK1

More details for `SIF file format <http://wiki.biouml.org/index.php/SIF_(file_format)>`_


--netUUID TEXT
    You can use a network extracted automatically from `NDEx <https://www.ndexbio.org/#/>`_ [3]_. You have to provide
    the UUID of the network (e.g. ``079f4c66-3b77-11ec-b3be-0ac135e8bacf``).

.. warning::

   :octicon:`alert;2em` By default, analysis is run using **gene symbols HGCN**. Pay attention of the gene IDs given in the network.

.. _RWRinput:

Random walk input files
============================

.. tip::

   See :octicon:`mark-github;1em` `Github <https://github.com/anthbapt/multixrank>`_ / and  :octicon:`book;1em` `Documentation <https://multixrank-doc.readthedocs.io/en/latest/>`_ to have more details



.. _configFile:

--configPath PATH
    Configuration file required by multiXrank tool. It could be short or very details (g.e. with tuned parameters).
    The short one contains the network and bipartite trees and the path of the seed file.
    If the user want more details go the the multiXrank's documentation :
    :octicon:`mark-github;1em` `Github <https://github.com/anthbapt/multixrank>`_ /
    :octicon:`book;1em` `Documentation <https://multixrank-doc.readthedocs.io/en/latest/>`_

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

.. [3]
