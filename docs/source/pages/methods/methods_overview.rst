==================================================
Overview of the approaches
==================================================

In the context of the EJP-RD project, an overlap analysis between a list of genes targeted by vitamins A&D and pathways
related to CAKUT disease was performed (Ozisik *et al.*, 2021 [1]_). For the vitamin A analysis, data was retrieved from
several sources: the `Comparative Toxicogenomics Databse (CTD) <https://ctdbase.org/>`_ [2]_ and the study of Balmer and
Blomhoff [3]_ for the target genes, and WikiPathways (WP) [4]_, Reactome [5]_ and Gene Ontology (GO) [6]_:sup:`,` [7]_
for the disease-associated genes.

Here, our goal is to extract data **directly from databases**, **automatize such analysis**, and implement alternative
approaches to uncover the relationships between environmental factors and Rare Diseases.
Data are extracted automatically from CTD [2]_ for target genes and WP [4]_ for Rare Disease pathways.
We propose different approaches, from simple overlaps using a list of factors, to advances methods based on Active
Subnetwork/Module identification or Random Walk with Restart diffusion. %A% here too need to define or replace factor.

Moreover, the tool is open to **external sources** provided by yourself (g.e. target genes list instead of environmental
factor, Reactome pathways etc ...)

Methods
=========

Three methods are available to study the relationships between environmental factors and rare diseases (:numref:`overviewFig`) :

    - :ref:`overlap`
    - :ref:`AMI`
    - :ref:`RWR`

.. _overviewFig:
.. figure:: ../../pictures/MethodsOverview.png
    :alt: methods overview
    :align: center

    : Overview of the three implemented approaches

Data sources
==============

Throughout this documentation, examples will be presented to illustrate the different sources of information. By default, data are automatically extracted from CTD [2]_ and WikiPathways [4]_.

Target genes %A% il faudra qu'on fasse un point sémantique: target genes, gene data, factor, environmental factor ... Pour être le plus génériques possibles
---------------

Gene data information may come from three different source :

.. tabs::

    .. group-tab:: CTD request

        .. warning::

            The CTD database is updated every month (`updates page <https://ctdbase.org/about/changes/>`_).
            For reproducibility, one might want to produce its own data version.

        Give a list of **environmental factors**. CTD is requested and returns a list of target genes associated with the input list of environmental factors. %A% je suis pas sure du mot "environmental" en fait, je sais pas si on peut dire par exemple qu'un médicament c'est un facteur environmental, ou alors en tous cas je suis pas sure que tout le monde considère ca du même point de vue.

    .. group-tab:: CTD file

        Give a **tsv file** with the data from **CTD** database. The gene list will be extracted from this file.

    .. group-tab:: Genes file

        Give a **list of genes** directly.

For more details about the :ref:`query` format.

Pathways
---------

Pathways can be extracted from two different sources :

.. tabs::

    .. group-tab:: WP request

        .. warning::

            WP is updated regularly (`updates page <https://www.wikipathways.org/index.php/WikiPathways:Updates>`_).
            It could be interesting to provide its own version of data for reproducibility.

        By default, **Rare Disease pathways** are extracted from **WikiPathways** [4]_. The corresponding background genes are
        extracted in the same time (all human genes in WP). The background genes is necessary to calculate statistics.

    .. group-tab:: GMT file

        Give a **GMT file** with pathways. It could be

            - rare diseases pathways from WP for a specific version
            - a custom GMT file with **pathways of interest**. Pathways can come from different sources.
              Corresponding backgrounds genes are needed.

For more details about the :ref:`pathways` format.

Examples %A% Use-cases?
-----------

We performed an analysis to study the relationships between vitamin A and Rare Diseases. We illustrate the different
possibilities of data extraction from different sources through three examples :

    - :ref:`example1`
    - :ref:`example2`
    - :ref:`example3`

.. tip::

    You can mix input types. For instance, you can request CTD and give a custom GMT file of pathways of interest.
    **Every combination is possible!**

References
==============

.. [1] Ozisik, O., Ehrhart, F., Evelo, C. T., Mantovani, A., & Baudot, A. (2021). Overlap of vitamin A and vitamin D target genes with CAKUT-related processes. F1000Research, 10.
.. [2] Davis AP, Grondin CJ, Johnson RJ, Sciaky D, Wiegers J, Wiegers TC, Mattingly CJ The Comparative Toxicogenomics Database: update 2021. Nucleic Acids Res. 2021.
.. [3] Balmer, J. E., & Blomhoff, R. (2002). Gene expression regulation by retinoic acid. Journal of lipid research, 43(11), 1773-1808.
.. [4] Martens, M., Ammar, A., Riutta, A., Waagmeester, A., Slenter, D. N., Hanspers, K., ... & Kutmon, M. (2021). WikiPathways: connecting communities. Nucleic acids research, 49(D1), D613-D621.
.. [5] Jassal, B., Matthews, L., Viteri, G., Gong, C., Lorente, P., Fabregat, A., ... & D’Eustachio, P. (2020). The reactome pathway knowledgebase. Nucleic acids research, 48(D1), D498-D503.
.. [6] Ashburner et al. Gene ontology: tool for the unification of biology. Nat Genet. May 2000;25(1):25-9
.. [7] The Gene Ontology resource: enriching a GOld mine. Nucleic Acids Res. Jan 2021;49(D1):D325-D334
.. [8] Curated chemical–gene interactions data were retrieved from the Comparative Toxicogenomics Database (CTD), MDI Biological Laboratory, Salisbury Cove, Maine, and NC State University, Raleigh, North Carolina. World Wide Web (URL: http://ctdbase.org/). [Month, year of data retrieval].
