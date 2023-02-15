.. _RWR:

==================================================
Random Walk with Restart
==================================================

Principle
------------

.. note::

    The Random Walk is performed using multiXrank [1]_ --
    :octicon:`mark-github;1em` `GitHub <https://github.com/anthbapt/multixrank>`_ :octicon:`book;1em` `ReadTheDocs <https://multixrank-doc.readthedocs.io/en/latest/>`_

This method measures the **proximity** of every gene within a multilayer to target genes. Every target gene is
defined as a **seed**. The walk starts with a seed selected **randomly**. The proximity is represented by a score that could be use
for multiple analysis. More the score is high, more the node is closed to the seed.

It's a kind of **diffusion analysis** from the genes through different molecular interactions (:numref:`overviewFig` - right part).

*For more details, see the multiXrank's paper* [1]_.

Usage
-------

By default, data are extracted directly by request databases (:numref:`RWRUsageFig`: *data extracted from requests*).
You give the ``--chemicalsFile`` and the **target genes** are extracted from **CTD**.

You can provide your own **target genes file** (:numref:`RWRUsageFig`: *data extracted from users*) with ``--targetGenesFile``.

.. _RWRUsageFig:
.. figure:: ../../pictures/multixrank_graph.png
    :alt: RWR analysis
    :align: center

    : Input and output files/parameters of Random Walk with Restart analysis

    There is two ways to extract target genes : from request (pink boxes) or provided by the user (green boxes).
    Required files/parameters have solid border line and optional files/parameters have dash border line.
    Output files in pink are created only if the input data are extracted from requests.

Input parameters for the RWR analysis
----------------------------------------

| To extract target genes from **CTD**, see parameters on the ``Data extracted from requests`` tab.
| To provide **your own** target genes, see parameters on the ``Data extracted from user`` tab.

.. tabs::

    .. group-tab:: Data extracted from requests

        -c, --chemicalsFile FILENAME
            Contains a list of chemicals. They have to be in **MeSH** identifiers (e.g. D014801).
            You can give several chemicals in the same line : they will be grouped for the analysis.
            [:ref:`FORMAT <chemicalsFile>`] **[required]**

        --directAssociation BOOLEAN
            | ``TRUE``: extract chemicals data, which are in the chemicalsFile, from CTD
            | ``FALSE``: extract chemicals and their child molecules data from CTD
            | ``[default: True]``

        --nbPub INTEGER
            Publications can be associated with chemical interactions.
            You can define a minimum number of publications to keep target genes.
            ``[default: 2]``

    .. group-tab:: Data extracted from user

        -t, --targetGenesFile FILENAME
            Contains a list of target genes. One gene per line. [:ref:`FORMAT <targetGenesFile>`]
            **[required]**

--configPath PATH
    MultiXrank needs a configuration file. It could be short (only file names) or very details (file names + parameters).
    The file contains at least paths of networks, bipartite and seed files. **[required]**

    | For more details : [:ref:`FORMAT <configFile>`] - :octicon:`mark-github;1em` `GitHub <https://github.com/anthbapt/multixrank>`_ :octicon:`book;1em` `ReadTheDocs <https://multixrank-doc.readthedocs.io/en/latest/>`_

--networksPath PATH
    Repository path where networks are saved. **[required]**

--seedsFile FILENAME
    Path name file to store seed list. This file contains the target genes list. They will be used as seed
    on the Random Walk analysis. **[required]**

--sifFileName FILENAME
    Output file name to save the result into a SIF file. **[required]**

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

    .. group-tab:: Data extracted from user

        .. code-block:: bash

            odamnet multixrank  --targetGenesFile useCases/InputData/VitA-Balmer2002-Genes.txt \
                                        --configPath useCases/InputData/config_minimal_useCase2.yml \
                                        --networksPath useCases/InputData/ \
                                        --seedsFile useCases/InputData/seeds.txt \
                                        --sifFileName resultsNetwork_useCase2.sif \
                                        --top 10 --outputPath \
                                        --outputPath useCases/OutputResults_useCase2/

Networks available
--------------------

.. note::

    We use the molecular multilayer network from multiXrank's paper [1]_.

We propose to run two walks through two different network compositions:

- molecular multilayer with three layers + pathways of interest network (:numref:`RWRFig` - left part)
- molecular multilayer with three layers + disease-disease similarity network (:numref:`RWRFig` - right part)

.. _RWRFig:
.. figure:: ../../pictures/NetworkAvailable_RWR.png
    :alt: RWR networks
    :align: center

    : Random Walk with restart into two different network compositions

Molecular multilayer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Protein-Protein Interaction network
"""""""""""""""""""""""""""""""""""""

Protein-Protein interaction (PPI) network is fusion of three datasets : APID, Hi-Union and Lit-BM. It's composed of:

- 14,703 nodes (proteins)

- 143,653 edges

Complexes network
""""""""""""""""""""

Complexes network is constructed from the fusion of Hu.map and Corum using OmniPathR. It's composed of:

- 8,537 nodes

- 63,561 edges

Reactome network
""""""""""""""""""""

This network is extracted from NDEs and corresponding to the Human Reactome data. It's composed of:

- 7,926 nodes

- 194,500 edges

.. _pathwaysOfInterestNet:

Pathways of interest network
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This kind of network can be build using the ``networkCreation`` method.

By default, the network is build using Rare Diseases pathways extracted automatically from WP.

--networksPath PATH
    Output repository name where the pathways network will be saved.

--bipartitePath PATH
    Output repository name where the bipartite gene-pathway will be saved.

--networksName FILENAME
    You can give a name to the pathway network. It's a SIF file but each pathway of interest is link to itself.
    ``[default: WP_RareDiseasesNetwork.sif]``

--bipartiteName FILENAME
    You can give a name to the bipartite. It's a tab-separated file.
    ``[default: Bipartite_WP_RareDiseases_geneSymbols.tsv]``

-o, --outputPath PATH
    Name of the folder to save complementary results (i.e. request results)
    ``[default: OutputResults]``

Moreover, you can provide your own pathways/processes of interest file using ``--GMT`` parameter.

This kind of network can be build from Rare Diseases pathways (WP) or from your own pathways/processes of interest
with ``networkCreation`` method.

.. tabs::

    .. group-tab:: Data extracted from requests

        .. code-block:: bash

            odamnet networkCreation --networksPath useCases/InputData/multiplex/2/ \
                                            --networksName WP_RareDiseasesNetwork_fromRequest.sif \
                                            --bipartitePath useCases/InputData/bipartite/ \
                                            --bipartiteName Bipartite_WP_RareDiseases_geneSymbols_fromRequest.tsv \
                                            --outputPath useCases/OutputResults_useCase1
    .. group-tab:: Data extracted from user

        .. code-block:: bash

            odamnet networkCreation --networksPath useCases/InputData/multiplex/2/ \
                                            --networksName pathwaysOfInterestNetwork_fromPaper.sif \
                                            --bipartitePath useCases/InputData/bipartite/ \
                                            --bipartiteName Bipartite_pathOfInterest_geneSymbols_fromPaper.tsv \
                                            --GMT useCases/InputData/PathwaysOfInterest.gmt \
                                            --outputPath useCases/OutputResults_useCase2

.. _DDnet:

Disease-disease similarity network
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Disease-disease similarity network creation
""""""""""""""""""""""""""""""""""""""""""""""

*Data was download on the 2022/06/11.*
*Annotation (`website <https://hpo.jax.org/app/data/annotation>`_) and ontologies (`website <https://hpo.jax.org/app/data/ontology>`_) are coming from HPO.*

We constructed a disease-disease network based on the phenotype similarity between diseases. A disease is defined as
a set of phenotypes and each phenotype is associated to the Human Ontology Project IDs (HPO).

The similarity score is calculated based on the number of shared phenotypes between two diseases ([3]_, [2]_, [1]_).
Every pairs of diseases will have a score, so for each disease we selected the top 5 of the most similar disease.

The **disease-disease** network contains 33,925 edges and 8,264 diseases.

.. tip::

    | You can use any multilayer and networks that you want.
    | :octicon:`alert;1em` Be careful with the configuration file and the gene IDs used.

Gene-disease bipartite
""""""""""""""""""""""""

*Data was download on the 2022/09/27.*
*Association file is coming from HPO* (`website <https://hpo.jax.org/app/data/annotation>`_).

The **molecular multiplex network** is connected to the **disease-disease similarity network** with the **gene-disease bipartite**.
The bipartite contains 6,564 associations (4,483 genes and 5,878 diseases).

References
------------

.. [1] Baptista, A., Gonzalez, A., & Baudot, A. (2022). Universal multilayer network exploration by random walk with restart. Communications Physics, 5(1), 1-9.
.. [2] Valdeolivas, A., Tichit, L., Navarro, C., Perrin, S., Odelin, G., Levy, N., ... & Baudot, A. (2019). Random walk with restart on multiplex and heterogeneous biological networks. Bioinformatics, 35(3), 497-505.
.. [3] Westbury SK, Turro E, Greene D, et al. Human phenotype ontology annotation and cluster analysis to unravel genetic defects in 707 cases with unexplained bleeding and platelet disorders. Genome Med. 2015;7(1):36. Published 2015 Apr 9. doi:10.1186/s13073-015-0151-5