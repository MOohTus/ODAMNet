==================================================
Overview of the approaches
==================================================

Goal
======

Our goal is to uncover **molecular relationships between chemicals** (e.g. vitamins, hormones etc.) and **rare diseases**.
To this end, we implement **three approaches**.

Data are retrieved **automatically** from the **Comparative Toxicogenomics Database** (CTD) [1]_ for target genes of
chemicals and **WikiPathways** [2]_ for rare disease pathways (see :ref:`usecase1`).

We propose three different approaches to uncover molecular relationships between genes which are targeted by chemicals and rare
diseases (:numref:`overviewFig`):

    - :ref:`overlap`: chemical target genes are part of a rare disease pathway
    - :ref:`AMI` (AMI): chemical target genes and/or linked genes that form a module are part of a rare disease pathway
    - :ref:`RWR` (RWR): rare disease pathways prioritization

These three approaches are **complementary** and they perform **network exploration** at different level of interactions.

.. _overviewFig:
.. figure:: ../../pictures/Approaches/Overview_approaches.png
    :alt: overviewFig
    :align: center

    : Overview of the three approaches implemented in ODAMNet

Moreover, the approaches can be used with user-provided input files instead of files fetched with automatic requests.
Take a look at :ref:`usecase2`, if you want to use your own input files.

References
==============

.. [1] Davis AP, Grondin CJ, Johnson RJ *et al.*. The Comparative Toxicogenomics Database: update 2021. Nucleic acids research. 2021.
.. [2] Martens M, Ammar A, Riutta A *et al.*. WikiPathways: connecting communities. Nucleic acids research. 2021.
