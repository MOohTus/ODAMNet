.. _overlap:

==================================================
Overlap analysis
==================================================

Principle
------------

.. note::

    This method is exactly the same that Ozisik *et al.,* implemented on his paper [1]_ .

This method calculates the overlap between genes and pathways of interest. We are looking for genes that are part of pathways.
It's a **direct association** (:numref:`overviewFig` - left part).

First, the method calculates the **overlap** between genes and each pathways. Then, a **statistical significance** is calculated
using an **hypergeometric test**. Finally, a **Benjamini-Hochberg** (BH adjusted) method is apply to correct values and
decrease the false discovery rate.

Required arguments
--------------------

.. tip::

    You can mix input type. For instance, you can request CTD and give a custom GMT file of pathways of interest.
    **Every combination is possible !**

.. tabs::

    .. group-tab:: Request

        -f, --factorList FILENAME
            Contains a list of chemicals. They have to be in **MeSH** identifiers (e.g. D014801).
            You can give several chemicals in the same line : they will be grouped for the analysis.
            [:ref:`FORMAT <factorList>`]

    .. group-tab:: Request Files

        -c, --CTD_file FILENAME
            Tab-separated file from CTD request. [:ref:`FORMAT <CTDFile>`]

        --GMT FILENAME
            Tab-delimited file that describes gene sets of Rare Disease pathways (from WP).
            [:ref:`FORMAT <pathways>`]

        --backgroundFile FILENAME
            List of the different background source file name. Each background genes source is a GMT file.
            It should be in the same order than the GMT file. Here, the background GMT file contains
            all Rare Disease pathways.
            [:ref:`FORMAT <pathways>`]

    .. group-tab:: Custom Files

        -g, --geneList FILENAME
            List of genes of interest. One gene per line. [:ref:`FORMAT <genesList>`]

        --GMT FILENAME
            Tab-delimited file that describes gene sets of pathways of interest.
            Pathways can come from several sources (e.g. WP and GO\:BP).
            [:ref:`FORMAT <pathways>`]

        --backgroundFile FILENAME
            List of the different background source file name. Each background genes source is a GMT file.
            It should be in the same order than the GMT file.
            [:ref:`FORMAT <pathways>`]

Optionals arguments
--------------------

--directAssociation BOOLEAN
    | If ``TRUE``, only the genes targeted by the factors are extracted.
    | If ``FALSE``, the genes targeted by the factors and all the descendant molecules are extracted.
    | ``[default: True]``

--nbPub INTEGER
    In CTD, an interaction between a gene and a molecule can have references.
    You can set a threshold on the number of publications needed to extract the interaction.
    ``[default: 2]``

-o, --outputPath PATH
    Name of the folder where to save the results.
    ``[default: OutputResults]``

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

            python3 main.py overlap --CTD_file examples/InputData/CTD_request_D014801_2022_08_24.tsv \
                                    --WP_GMT examples/InputData/WP_RareDiseases_request_2022_08_24.gmt \
                                    --backgroundFile examples/InputData/backgroundsFiles.tsv \
                                    --nbPub 2 \
                                    --outputPath examples/OutputResults_example2/

    .. group-tab:: Custom Files

        .. code-block:: bash

            python3 main.py overlap --geneList examples/InputData/InputFromPaper/VitA-CTD-Genes.txt \
                                    --WP_GMT examples/InputData/InputFromPaper/PathwaysOfInterest.gmt \
                                    --backgroundFile examples/InputData/InputFromPaper/PathwaysOfInterestBackground.txt \
                                    --outputPath examples/OutputResults_example3/

References
------------

.. [1] Ozisik, O., Ehrhart, F., Evelo, C. T., Mantovani, A., & Baudot, A. (2021). Overlap of vitamin A and vitamin D target genes with CAKUT-related processes. F1000Research, 10.
