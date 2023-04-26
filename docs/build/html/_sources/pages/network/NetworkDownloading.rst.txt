.. _netDownloading:

================================
Networks downloading
================================

.. warning::

    - Gene IDs have to be **consistent** between input data *(target genes, GMT and networks)*
    - When data are retrieved by requests, **HGNC** IDs are used.

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

.. code-block:: bash

    odamnet networkDownloading  --netUUID bfac0486-cefe-11ed-a79c-005056ae23aa \
                                --networkFile useCases/InputData/multiplex/1/PPI_HiUnion_LitBM_APID_gene_names_190123.tsv \
                                --simple True

References
============

.. [1] Pratt D, Chen J, Welker D, et al. NDEx, the Network Data Exchange. Cell Syst. 2015;1(4):302-305. doi:10.1016/j.cels.2015.10.001
.. [2] Pillich RT, Chen J, Churas C, et al. NDEx: Accessing Network Models and Streamlining Network Biology Workflows. Curr Protoc. 2021;1(9):e258. doi:10.1002/cpz1.258
.. [3] Baptista, A., Gonzalez, A., & Baudot, A. (2022). Universal multilayer network exploration by random walk with restart. Communications Physics, 5(1), 1-9.
.. [4] Levi, H., Elkon, R., & Shamir, R. (2021). DOMINO: a network‐based active module identification algorithm with reduced rate of false calls. Molecular systems biology, 17(1), e9593.


.. _NDEx: https://www.ndexbio.org/
.. |NDEx| replace:: Network Data Exchange