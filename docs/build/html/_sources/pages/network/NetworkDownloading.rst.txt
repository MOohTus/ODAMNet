================================
Networks downloading
================================

.. warning::

    - Gene IDs have to be **consistent** between input data *(target genes, GMT and networks)*
    - When data are retrieved by queries, **HGNC** IDs are used.

Principle
===========

You can download biological networks from the |NDEx|_ (NDEx) [1]_ using ``networkDownloading`` function available in
ODAMNet. This function downloads biological networks using the NDEx2 Python client [2]_ and the network IDs.

Input parameters for network downloading
============================================

To download biological networks, you needs the network ID ``--netUUID`` and a name to save the network ``--netUUID``.
These two parameters are **required**.

--netUUID TEXT
    NDEx network ID **[required]**

--networkFile FILENAME
    Output file name to save the downloaded network **[required]**

--simple BOOLEAN
    | if TRUE, create a file with two columns and no header
    | if FALSE, create a file with three columns and header

.. tabs::

    .. group-tab:: ``--simple TRUE``

        - **Two** columns: node 1 and node 2
        - **Without header**
        - Network format file used by **multiXrank** [3]_ *(random walk with restart (RWR) approach).*
        - :ref:`GR format <GR>`

        .. code-block:: none

            MMP11	PRPF40A
            ASB16-AS1	SHBG
            KIAA0513	INTS4
            KIAA0513	HAX1
            RAVER2	PTBP1
            CNGB1	PNN
            CLDN3	POM121
            CFD	HDHD2
            DENND10P1	TMEM256

    .. group-tab:: ``--simple FALSE``

        - **Three** columns: node 1, interaction type, node 2
        - **With header**
        - Network format file used by **DOMINO** [4]_ *(active module identification (AMI) approach).*
        - :ref:`SIF format <SIF>`

        .. code-block:: none

            node_1	link	node_2
            MMP11	interacts with	PRPF40A
            ASB16-AS1	interacts with	SHBG
            KIAA0513	interacts with	INTS4
            KIAA0513	interacts with	HAX1
            RAVER2	interacts with	PTBP1
            CNGB1	interacts with	PNN
            CLDN3	interacts with	POM121
            CFD	interacts with	HDHD2
            DENND10P1	interacts with	TMEM256


Use-case command lines
========================

.. warning::

    If ``--simple FALSE``, network file name should has ``.sif`` extension

.. code-block:: bash

    odamnet networkDownloading  --netUUID bfac0486-cefe-11ed-a79c-005056ae23aa \
                                --networkFile useCases/InputData/multiplex/1/PPI_HiUnion_LitBM_APID_gene_names_190123.gr \
                                --simple True

References
============

.. [1] Pratt D, Chen J, Welker *et al.*. NDEx, the Network Data Exchange. Cell Systems. 2015.
.. [2] Pillich RT, Chen J, Churas C, *et al.*. NDEx: Accessing Network Models and Streamlining Network Biology Workflows. Current Protocol. 2021.
.. [3] Baptista A, Gonzalez A & Baudot A. Universal multilayer network exploration by random walk with restart. Communications Physics. 2022.
.. [4] Levi H, Elkon R & Shamir R. DOMINO: a network‐based active module identification algorithm with reduced rate of false calls. Molecular systems biology. 2021.

.. _NDEx: https://www.ndexbio.org/
.. |NDEx| replace:: Network Data Exchange