.. _input:

==================================================
Input files
==================================================

.. _targetGenes:

Target genes 
=================

.. line-block::

        Two ways exist to extract the list of target genes:

        :ref:`chemicalsFile`: give chemical IDs file as input and request the Comparative Toxicogenomics Database (CTD)
        :ref:`targetGenesFile`: give your own target genes file

.. tip::

   For reproducibility, you can give your own version of CTD file using ``--CTD_file`` [:ref:`FORMAT <CTD_file>`] 

.. _chemicalsFile:

1. Chemicals file 
---------------------

.. tip::

   Target genes are extracted from CTD in HGCN format.


-c, --chemicalsFile FILENAME
    Contains a list of chemicals. They have to be in **MeSH** identifiers (e.g. D014801).
    Each line contains one or several chemical IDs, separated by ";".

.. code-block:: none

            D014801;D014807
            D014212
            C009166

Target genes will be extracted from CTD for each line and the three approaches will be performed on each line separatly.
If they are multiple chemicals into one line, target genes of each chemical will be extracted and used as only one list
of target genes as input of the three approaches.

.. _targetGenesFile:

2. Target genes file
---------------------

-t, --targetGenesFile FILENAME
    Contains a list of target genes of interest. One target gene per line.

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

It's composed of 9 columns:

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


.. _pathways:

Pathways/processes of interest
=================================

By default, WikiPathays is automatically requested to extract rare disease pathways. Moreover, you can give your own
pathways/processes of interest (``--GMT``). You need to provided the ontology source of them too (``backgroundFile``).

--GMT FILENAME
    It's a tab-delimited file that describes gene sets of pathways/processes of interest. Pathways can come from several sources.
    Each row represents a gene set.

There are at least, three columns:

- ``pathwayIDs``: first column is pathway IDs
- ``pathways``: second column is pathway names - Optional, you can fill it in a dummy field
- ``HGNC``: all the other columns contain genes inside pathway. The number of columns is different for each pathway and varies according the number of genes inside.

The GMT file is organized as follow:

.. code-block:: none

    pathwayIDs 	pathways	HGNC
    WP5195	Disorders in ketolysis	ACAT1	HMGCS1	OXCT1	BDH1	ACAT2
    WP5189	Copper metabolism	ATP7B	ATP7A	SLC11A2	SLC31A1
    WP5190	Creatine pathway	GAMT	SLC6A8	GATM	OAT	CK

More details for `GMT file format <https://software.broadinstitute.org/cancer/software/gsea/wiki/index.php/Data_formats#GMT:_Gene_Matrix_Transposed_file_format_.28.2A.gmt.29>`_.

.. warning::

    :octicon:`alert;2em` GMT file **must doesn't** contain **empty columns**.

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

   Theses parameters, ``--GMT`` and ``--backgroundFile`` can be used for reproducibility.

.. _network:

Networks
===========================

.. _SIF:

Active Module Identification input network
---------------------------------------------

-n, --networkFile FILENAME
    Network file name. The file is in SIF (Simple Interaction File) format.
    It's a tab-delimited file.

There are three columns: source node, interaction type, target node.

.. code-block:: none

    node_1      link    node_2
    AAMP        ppi     VPS52
    AAMP        ppi     BHLHE40
    AAMP        ppi     AEN
    AAMP        ppi     C8orf33
    AAMP        ppi     TK1

More details for `SIF file format <http://wiki.biouml.org/index.php/SIF_(file_format)>`_.

.. warning::

   :octicon:`alert;2em` By default, the analysis is running using the **HGCN** gene ids. Pay attention of the gene IDs inside the network file.

.. _GR:

Random Walk with Restart input network
------------------------------------------

MultiXrank [1]_ accepts networks and bipartites in **.gr format**. It's a tab-delimited graph format with two columns.

.. code-block:: none

    NFYA	NFYB
    NFYA	NFYC
    NFYB	NFYC
    BTRC	CUL1
    BTRC	SKP1


.. _configFile:

Configuration file
=====================

--configPath PATH
    Configuration file required by multiXrank tool [1]_. It could be short or very detailed (g.e. with tuned parameters).
    The short one contains the network and bipartite trees and the path of the seed file.
    If users want more details, see the multiXrank's documentation:
    :octicon:`mark-github;1em` `Github <https://github.com/anthbapt/multixrank>`_ /
    :octicon:`book;1em` `Documentation <https://multixrank-doc.readthedocs.io/en/latest/>`_

This is an example of minimal configuration file:

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

References
------------

.. [1] Baptista, A., Gonzalez, A., & Baudot, A. (2022). Universal multilayer network exploration by random walk with restart. Communications Physics, 5(1), 1-9.