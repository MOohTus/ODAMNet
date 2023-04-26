.. _RWR:

==================================================
Random Walk with Restart
==================================================

Principle
------------

.. note::

    The Random Walk with Restart is performed using multiXrank [1]_ --
    :octicon:`mark-github;1em` `GitHub <https://github.com/anthbapt/multixrank>`_ :octicon:`book;1em` `ReadTheDocs <https://multixrank-doc.readthedocs.io/en/latest/>`_

The Random Walk with Restart (RWR) approach measures the **proximity** between target genes and all the nodes (e.g. genes,
diseases ...) that are present in a multilayer network. All target genes are considered as **seeds** to start a walk. The proximity
is represented by a score that can be use for multiple analysis. Higher score corrsponds to smaller distance and better connection between the node and the seeds.

RWR is a **diffusion analysis** from target genes through different molecular interactions (:numref:`overviewFig` - right part).

*For more details, see the multiXrank's paper* [1]_.

Usage
-------

By default, data are extracted directly by querying databases (:numref:`RWRUsageFig`: *data extracted from requests*).
You give the ``--chemicalsFile`` and the **target genes** are extracted from the **Comparative Toxicogenomics Database** (CTD).

You can provide your own **target genes file** (:numref:`RWRUsageFig`: section *data provided by users*) with ``--targetGenesFile``.

.. _RWRUsageFig:
.. figure:: ../../pictures/Overview_RWR.png
    :alt: Random Walk with Restart analysis
    :align: center

    : Input and output of Random Walk with Restart (RWR) analysis

    (Left part) - Target genes and rare disease pathways can be extracted using automatic request. The users can also
    provide their own data. Required input are represented with pink and green solid border line boxes whereas optional
    input are represented with dashed border line boxes.
    (Right part) - Output files that are in pink are created only if the input data are extracted from request.

Input parameters for the RWR analysis
----------------------------------------

.. warning::

    - Gene IDs have to be **consistent** between input data *(target genes, GMT and networks)*
    - When data are retrieved by requests, **HGNC** IDs are used.

| To extract target genes from **CTD**, see parameters on the ``Data extracted from requests`` tab.
| To provide **your own** target genes, see parameters on the ``Data provided by users`` tab.

.. tabs::

    .. group-tab:: Data extracted from requests

        -c, --chemicalsFile FILENAME
            Contains a list of chemicals. They have to be in **MeSH** identifiers (e.g. D014801).
            Each line contains one or several chemical IDs, separated by ";".
            [:ref:`FORMAT <chemicalsFile>`] **[required]**

        --directAssociation BOOLEAN
            | ``TRUE``: extract chemicals data, which are in the chemicalsFile, from CTD
            | ``FALSE``: extract chemicals and their descendant chemicals data from CTD
            | ``[default: True]``

        --nbPub INTEGER
            Each interaction between target gene and chemical can be associated with publications.
            You can filter these interactions according the number of publication associated.
            You can define a minimum number of publications.
            ``[default: 2]``

    .. group-tab:: Data provided by users

        -t, --targetGenesFile FILENAME
            Contains a list of target genes. One target gene per line. [:ref:`FORMAT <targetGenesFile>`]
            **[required]**

--configPath PATH
    MultiXrank needs a configuration file. It can be short (with only file names) or very detailed (with file names + parameters).
    The file contains at least paths of networks, bipartite and seed files. **[required]**

    | For more details : [:ref:`FORMAT <configFile>`] - :octicon:`mark-github;1em` `GitHub <https://github.com/anthbapt/multixrank>`_ :octicon:`book;1em` `ReadTheDocs <https://multixrank-doc.readthedocs.io/en/latest/>`_

--networksPath PATH
    Repository path where networks are saved. **[required]**

--seedsFile FILENAME
    Path name file to store seed list. This file contains the target genes list. They will be used as seed
    on the Random Walk analysis. **[required]**

--sifFileName FILENAME
    Output file name to save the result into a SIF file format. **[required]**

--top INTEGER
    Top nodes that will be saved into the output network (into SIF file).

-o, --outputPath PATH
    Name of the folder to save the results.
    ``[default: OutputResults]``

Use-cases command lines
-------------------------

.. tabs::

    .. group-tab:: Data extracted from requests

        .. code-block:: bash

            odamnet multixrank  --chemicalsFile useCases/InputData/chemicalsFile.csv \
                                        --directAssociation FALSE \
                                        --nbPub 2 \
                                        --configPath useCases/InputData/config_minimal_useCase1.yml \
                                        --networksPath useCases/InputData/ \
                                        --seedsFile useCases/InputData/seeds.txt \
                                        --sifFileName resultsNetwork_useCase1.sif \
                                        --top 10 \
                                        --outputPath useCases/OutputResults_useCase1/

    .. group-tab:: Data provided by users

        .. code-block:: bash

            odamnet multixrank  --targetGenesFile useCases/InputData/VitA-Balmer2002-Genes.txt \
                                        --configPath useCases/InputData/config_minimal_useCase2.yml \
                                        --networksPath useCases/InputData/ \
                                        --seedsFile useCases/InputData/seeds.txt \
                                        --sifFileName resultsNetwork_useCase2.sif \
                                        --top 10 --outputPath \
                                        --outputPath useCases/OutputResults_useCase2/

References
------------

.. [1] Baptista, A., Gonzalez, A., & Baudot, A. (2022). Universal multilayer network exploration by random walk with restart. Communications Physics, 5(1), 1-9.