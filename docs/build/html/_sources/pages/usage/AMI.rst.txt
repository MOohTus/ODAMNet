Active Module Identification (AMI)
-------------------------------------

Different approaches are implemented in this tool to analysis link between environmental factor and rare disease pathways.

.. click:: main:main
   :prog: main
   :nested: full
   :commands: domino

Up to date analysis - Vitamin A :
===================================

Required options :
^^^^^^^^^^^^^^^^^^^

-f, --factorList FILENAME
    Contains a list of chemicals. Could be chemical names (e.g. vitamin A) or the MeSH identifier (e.g. D014801).
    The user can gives several chemicals in the same line : they will be grouped for the analysis.

-n, --networkFile FILENAME
    Network file name (e.g. PPI network).
    The file contains 3 columns such as SIF format with the source node, the interaction type and the target node.

Optionals options :
^^^^^^^^^^^^^^^^^^^

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

Command line :
^^^^^^^^^^^^^^^^^^^

.. tabs::

    .. group-tab:: short

        .. code-block:: bash

            python3 main.py domino  --factorList examples/InputData/InputFile_factorsList.csv \
                                    --networkFile examples/InputData/PPI_network_2016.sif

    .. group-tab:: detailed

        .. code-block:: bash

            python3 main.py domino  --factorList examples/InputData/InputFile_factorsList.csv \
                                    --directAssociation FALSE \
                                    --nbPub 2 \
                                    --networkFile examples/InputData/PPI_network_2016.sif \
                                    --outputPath examples/OutputResults_example1/

Specific version - Vitamin A :
===============================

Required options :
^^^^^^^^^^^^^^^^^^^

-c, --CTD_file FILENAME
    It's a tab-separated file from CTD request (e.g. created with an up to date analysis). Refers to XXX to have more information about the format.

--WP_GMT FILENAME
    Gene composition of each rare disease pathways of interest from WikiPathways. It's a GMT file-like (e.g. created with an up to date analysis).
    Refers to XXX to have more information about the format.

--backgroundFile FILENAME
    List of all genes present in the WikiPathways database (i.e. human genes).

-n, --networkFile FILENAME
    Network file name (e.g. PPI network).
    The file contains 3 columns such as SIF format with the source node, the interaction type and the target node.

Optionals options :
^^^^^^^^^^^^^^^^^^^^

--nbPub INTEGER
    In CTD, an interaction between a gene and a molecule can have references. The user can set a threshold on the number of publications needed to extract the interaction.
    [default: 2]

-o, --outputPath PATH
    Name of the folder where save the results
    [default: OutputResults]

Command line :
^^^^^^^^^^^^^^^^^^^

.. tabs::

    .. group-tab:: short

        .. code-block:: bash

            python3 main.py domino  --CTD_file examples/InputData/InputFile_CTD_request_D014801_2022_07_01.tsv  \
                                    --WP_GMT examples/InputData/WP_RareDiseases_request_2022_08_01.gmt \
                                    --backgroundFile examples/InputData/InputFile_backgroundsFiles.tsv \
                                    --networkFile examples/InputData/PPI_network_2016.sif

    .. group-tab:: detailed

        .. code-block:: bash

            python3 main.py domino  --CTD_file examples/InputData/InputFile_CTD_request_D014801_2022_07_01.tsv  \
                                    --nbPub 2 \
                                    --WP_GMT examples/InputData/WP_RareDiseases_request_2022_08_01.gmt \
                                    --backgroundFile examples/InputData/InputFile_backgroundsFiles.tsv \
                                    --networkFile examples/InputData/PPI_network_2016.sif \
                                    --outputPath examples/OutputResults_example2/


Global analysis - Data as you want :
======================================

Required options :
^^^^^^^^^^^^^^^^^^^

-g, --geneList FILENAME
    List of gens of interest. One gene per line.

--WP_GMT FILENAME
    GMT file-like of pathways of interest. Pathways can come from several sources.
    Refers to XXX to have more information about the format.

--backgroundFile FILENAME
    Name list of the different background source (each background contain the list of all genes).

-n, --networkFile FILENAME
    Network file name (e.g. PPI network).
    The file contains 3 columns such as SIF format with the source node, the interaction type and the target node.

Optionals options :
^^^^^^^^^^^^^^^^^^^^

-o, --outputPath PATH
    Name of the folder where save the results
    [default: OutputResults]


Vitamin A analysis with data from paper *(Ozisik, 2022)*:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Command line :
^^^^^^^^^^^^^^^^^^^

.. tabs::

    .. group-tab:: short

        .. code-block:: bash

            python3 main.py domino  --geneList examples/InputData/InputFromPaper/VitA-Balmer2002-Genes.txt \
                                    --WP_GMT examples/InputData/InputFromPaper/PathwaysOfInterest.gmt \
                                    --backgroundFile examples/InputData/InputFromPaper/PathwaysOfInterestBackground.txt \
                                    --networkFile examples/InputData/PPI_network_2016.sif

    .. group-tab:: detailed

        .. code-block:: bash

            python3 main.py domino  --geneList examples/InputData/InputFromPaper/VitA-Balmer2002-Genes.txt \
                                    --WP_GMT examples/InputData/InputFromPaper/PathwaysOfInterest.gmt \
                                    --backgroundFile examples/InputData/InputFromPaper/PathwaysOfInterestBackground.txt \
                                    --networkFile examples/InputData/PPI_network_2016.sif \
                                    --outputPath examples/OutputResults_example3/
