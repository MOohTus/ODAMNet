.. _overlap:

==================================================
Overlap analysis
==================================================

Principle
------------

.. note::

    This method is exactly the same that Ozisik implemented on his paper [1]_ .

This method calculates the overlap between genes and pathways of interest. We are looking for genes that are part of pathways.
It's a **direct association** (:numref:`overviewFig` - left part).

First, the method calculates the **overlap** between genes and each pathways. Then, a **statistical significance** is calculated
using an **hypergeometric test**. Finally, a **Benjamini-Hochberg** (BH adjusted) method is apply to correct values and
decrease the false discovery rate.

Required options
--------------------

.. tip::

    You can mix input type. For instance, request CTD and give a custom GMT file of pathways of interest.
    Every combination is possible !

.. tabs::

    .. group-tab:: Request

        -f, --factorList FILENAME
            Contains a list of chemicals. Could be chemical names (e.g. vitamin A) or the MeSH identifier (e.g. D014801).
            The user can gives several chemicals in the same line : they will be grouped for the analysis.

    .. group-tab:: Request Files

        -c, --CTD_file FILENAME
            It's a tab-separated file from CTD request (e.g. created with an up to date analysis). Refers to XXX to have more information about the format.

        --GMT FILENAME
            Gene composition of each rare disease pathways of interest from WikiPathways. It's a GMT file-like (e.g. created with an up to date analysis).
            Refers to XXX to have more information about the format.

        --backgroundFile FILENAME
            List of all genes present in the WikiPathways database (i.e. human genes).

    .. group-tab:: Custom Files

        -g, --geneList FILENAME
            List of gens of interest. One gene per line.

        --GMT FILENAME
            GMT file-like of pathways of interest. Pathways can come from several sources.
            Refers to XXX to have more information about the format.

        --backgroundFile FILENAME
            Name list of the different background source (each background contain the list of all genes).

Optionals options
--------------------

--directAssociation BOOLEAN
    If TRUE, only the genes targeted by the chemical are extracted.
    If FALSE, the genes targeted by the chemical and all the descendant molecules are extracted.
    [default: True]

--nbPub INTEGER
    In CTD, an interaction between a gene and a molecule can have references.
    The user can set a threshold on the number of publications needed to extract the interaction.
    [default: 2]

-o, --outputPath PATH
    Name of the folder where save the results
    [default: OutputResults]

Command line examples
------------------------

.. tabs::

    .. group-tab:: Request

        .. code-block:: bash

            python3 main.py overlap --factorList examples/InputData/InputFile_factorsList.csv \
                                    --directAssociation FALSE \
                                    --nbPub 2 \
                                    --outputPath examples/OutputResults_example1/

    .. group-tab:: Request Files

        .. code-block:: bash

            python3 main.py overlap --CTD_file examples/InputData/InputFile_CTD_request_D014801_2022_07_01.tsv \
                                    --WP_GMT examples/InputData/WP_RareDiseases_request_2022_08_01.gmt \
                                    --backgroundFile examples/InputData/InputFile_backgroundsFiles.tsv \
                                    --nbPub 2 \
                                    --outputPath examples/OutputResults_example2/

    .. group-tab:: Custom Files

        .. code-block:: bash

            python3 main.py overlap --geneList examples/InputData/InputFromPaper/VitA-Balmer2002-Genes.txt \
                                    --WP_GMT examples/InputData/InputFromPaper/PathwaysOfInterest.gmt \
                                    --backgroundFile examples/InputData/InputFromPaper/PathwaysOfInterestBackground.txt \
                                    --outputPath examples/OutputResults_example3/

References
------------

.. [1] Ozisik, O., Ehrhart, F., Evelo, C. T., Mantovani, A., & Baudot, A. (2021). Overlap of vitamin A and vitamin D target genes with CAKUT-related processes. F1000Research, 10.
