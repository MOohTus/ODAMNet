==================================================
Overview of the approaches
==================================================

Context
==========

In the context of the EJP-RD project, an overlap analysis between a list of genes targeted by vitamins A&D and pathways
related to CAKUT disease was performed (Ozisik *et al.*, 2021 [1]_).

For the vitamin A analysis, data was retrieved from
several sources: the `Comparative Toxicogenomics Database (CTD) <https://ctdbase.org/>`_ [2]_ and the study of Balmer and
Blomhoff [3]_ for the target genes, and WikiPathways (WP) [4]_, Reactome [5]_ and Gene Ontology (GO) [6]_:sup:`,` [7]_
for the disease-associated genes.

Goal
======

Here, our goal is to extract data **directly from databases**, **automatize such analysis**, and implement alternative
approaches to uncover the **relationships between chemicals** (g.e. vitamins, hormones etc ...) and **Rare Diseases**.

Data are extracted **automatically** from the **Comparative Toxicogenomics Database** (CTD) [2]_ for target genes and
**WikiPathways** (WP) [4]_ for Rare Disease pathways (see :ref:`usecase1`).

We propose three different approaches to study the relationships between genes which are targeted by chemicals and Rare
Diseases (:numref:`overviewFig`):

    - :ref:`overlap`
    - :ref:`AMI`
    - :ref:`RWR`

Theses three approaches are **complementary** and perform **network exploration** at different level of interactions.

.. _overviewFig:
.. figure:: ../../pictures/MethodsOverview.png
    :alt: methods overview
    :align: center

    : Overview of the three implemented approaches

Moreover, the approaches are open to **external input files** provided by yourself (g.e. target genes file instead of
chemicals file, pathways and/or processes etc ...). Look :ref:`usecase2`, if you want to use your own input files.

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
