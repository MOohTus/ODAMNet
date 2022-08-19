==================================================
Methods overview
==================================================

As part of the EJP RD project, an overlap analysis was perform between a list of genes targeted by vitamin A and pathways
related to CAKUT disease. The main goal of this analysis was to show if vitamin A could effect on CAKUT disease (Ozisik *et al.*, 2021 [1]_).

Data information came from several sources : the `Comparative Toxicogenomics Databse (CTD) <https://ctdbase.org/>`_ [2]_
and the study of Balmer and Blomhoff [3]_ for the target genes and WikiPathways (WP) [4]_, Reactome [5]_ and Gene Ontology (GO) [6]_:sup:`,` [7]_.

With this project, we want to automatise the analysis and extract data information directly from databases. Users can
study the link between environmental factors and rare diseases easily juts by giving a factors list. Other methods can
be perform as random walk analyse or active subnetwork identification in addition to overlap. Moreover, the tool is open
to external sources provided by users.

Methods
=========

Three methods are available to study the link between environmental factors and rare diseases (:numref:`overviewFig`) :

    - :ref:`overlap`
    - :ref:`AMI`
    - :ref:`RWR`

.. _overviewFig:
.. figure:: ../../pictures/MethodsOverview.png
    :alt: methods overview
    :align: center

    : Methods implemented overview

Data source
==============

Throughout this documentation, examples will be presented to illustrate these different sources of information. By default,
genes data are automatically extracted from CTD [2]_ and pathways from WikiPathways [4]_.

Target genes
---------------

Gene data information may come from three different source :

.. tabs::

    .. group-tab:: CTD request

        .. warning::

            The CTD database is updated every month (`Updates page <https://ctdbase.org/about/changes/>`_). May provide is own
            version of data is interesting for reproducibility.

        Users give a list of **environmental factors**. CTD is requested an gives a list of target genes.

    .. group-tab:: CTD file

        Users give a **tsv file** with the data from **CTD** database. Genes list is extracted from this file.

    .. group-tab:: Genes file

        Users give a **list of genes** directly

Pathways
---------

Pathways can be extracted from two different sources :

.. tabs::

    .. group-tab:: WP request

        .. warning::

            WP is updated regularly (`Updates page <https://www.wikipathways.org/index.php/WikiPathways:Updates>`_).
            May provide is own version of data is interesting for reproducibility.

        By default, **Rare Disease Pathways** are extracted from **WikiPathways** [4]_. The corresponding background genes are
        extracted in the same time (all human genes in WP).

    .. group-tab:: GMT file

        Users give a **GMT file** with pathways. It could be rare diseases pathways from WP for a specific version,
        or a custom GMT file with **pathways of interest**. Pathways can come from different sources. Corresponding backgrounds
        genes are needed.

Examples
-----------

We performed an analysis to study the link between vitamin A and rare diseases. We illustrated the different source extraction
through three examples.

    - :ref:`example1`
    - :ref:`example2`
    - :ref:`example3`

.. tip::

    You can mix input type. For instance, request CTD and give a custom GMT file of pathways of interest.
    Every combination is possible !

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
