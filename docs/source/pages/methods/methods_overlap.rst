.. _overlap:

==================================================
Overlap analysis
==================================================

Principle
------------

Same method implemented on Ozisik, 2022 paper

- Calculate the overlap between target genes and WikiPathways Rare Diseases (or pathways of interest).
- We are looking for target genes that are part of pathways.
- It's a **direct association**.

How it's working ? Hypergeometric and multitest etc ...

Example 1 : data source from requests
---------------------------------------

Required options
""""""""""""""""""""

-f, --factorList FILENAME
    Contains a list of chemicals. Could be chemical names (e.g. vitamin A) or the MeSH identifier (e.g. D014801).
    The user can gives several chemicals in the same line : they will be grouped for the analysis.

Optionals options
""""""""""""""""""""

--directAssociation BOOLEAN
    If TRUE, only the genes targeted by the chemical are extracted.
    If FALSE, the genes targeted by the chemical and all the descendant molecules are extracted.
    [default: True]

--nbPub INTEGER
    In CTD, an interaction between a gene and a molecule can have references. The user can set a threshold on the number of publications needed to extract the interaction.
    [default: 2]

-o, --outputPath PATH
    Name of the folder where save the results
    [default: OutputResults]

Command lines
""""""""""""""""""""

.. tabs::

    .. group-tab:: short

        .. code-block:: bash

           python3 main.py overlap  --factorList examples/InputData/InputFile_factorsList.csv

    .. group-tab:: detailed

        .. code-block:: bash

           python3 main.py overlap  --factorList examples/InputData/InputFile_factorsList.csv \
                                    --directAssociation FALSE \
                                    --nbPub 2 \
                                    --outputPath examples/OutputResults_example1/



Example 2 : data source from database files
---------------------------------------------

Required options :
""""""""""""""""""""

-c, --CTD_file FILENAME
    It's a tab-separated file from CTD request (e.g. created with an up to date analysis). Refers to XXX to have more information about the format.

--WP_GMT FILENAME
    Gene composition of each rare disease pathways of interest from WikiPathways. It's a GMT file-like (e.g. created with an up to date analysis).
    Refers to XXX to have more information about the format.

--backgroundFile FILENAME
    List of all genes present in the WikiPathways database (i.e. human genes).

Optionals options :
""""""""""""""""""""

--nbPub INTEGER
    In CTD, an interaction between a gene and a molecule can have references. The user can set a threshold on the number of publications needed to extract the interaction.
    [default: 2]

-o, --outputPath PATH
    Name of the folder where save the results
    [default: OutputResults]

Command lines
""""""""""""""""""""

.. tabs::

    .. group-tab:: short

        .. code-block:: bash

           python3 main.py overlap  --CTD_file examples/InputData/InputFile_CTD_request_D014801_2022_07_01.tsv \
                                    --WP_GMT examples/InputData/WP_RareDiseases_request_2022_08_01.gmt \
                                    --backgroundFile examples/InputData/InputFile_backgroundsFiles.tsv

    .. group-tab:: detailed

        .. code-block:: bash

           python3 main.py overlap  --CTD_file examples/InputData/InputFile_CTD_request_D014801_2022_07_01.tsv \
                                    --WP_GMT examples/InputData/WP_RareDiseases_request_2022_08_01.gmt \
                                    --backgroundFile examples/InputData/InputFile_backgroundsFiles.tsv \
                                    --nbPub 2 \
                                    --outputPath examples/OutputResults_example2/



Example 3 : custom data source
---------------------------------------

Required options
""""""""""""""""""""

-g, --geneList FILENAME
    List of gens of interest. One gene per line.

--WP_GMT FILENAME
    GMT file-like of pathways of interest. Pathways can come from several sources.
    Refers to XXX to have more information about the format.

--backgroundFile FILENAME
    Name list of the different background source (each background contain the list of all genes).

Optionals options
""""""""""""""""""""

-o, --outputPath PATH
    Name of the folder where save the results
    [default: OutputResults]

Data from paper *(Ozisik, 2022)*
""""""""""""""""""""""""""""""""""""""""

.. tabs::

    .. group-tab:: short

        .. code-block:: bash

           python3 main.py overlap  --geneList examples/InputData/InputFromPaper/VitA-Balmer2002-Genes.txt \
                                    --WP_GMT examples/InputData/InputFromPaper/PathwaysOfInterest.gmt \
                                    --backgroundFile examples/InputData/InputFromPaper/PathwaysOfInterestBackground.txt

    .. group-tab:: detailed

        .. code-block:: bash

           python3 main.py overlap  --geneList examples/InputData/InputFromPaper/VitA-Balmer2002-Genes.txt \
                                    --WP_GMT examples/InputData/InputFromPaper/PathwaysOfInterest.gmt \
                                    --backgroundFile examples/InputData/InputFromPaper/PathwaysOfInterestBackground.txt \
                                    --outputPath examples/OutputResults_example3/
