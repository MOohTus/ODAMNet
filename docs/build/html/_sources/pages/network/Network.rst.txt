.. _netDownloading:

================================
Networks downloading
================================

Principle
~~~~~~~~~~~~

You can download biological networks from NDEx [1]_ using ``networkDownloading`` function available in ODAMNet.

Input parameters for network downloading
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

--netUUID TEXT
    NDEx network ID **[required]**

--networkFile FILENAME
    Output file name to save the downloaded network **[required]**

--simple BOOLEAN
    | if TRUE, create a file with two columns and no header (*for RWR approach*) [:ref:`NETFORMAT`]
    | if FALSE, create a file with three columns and header (*for AMI approach*) [:ref:`NETFORMAT`]

For the use-cases, we downloaded three biological networks.

Use-case command lines
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    odamnet networkDownloading  --netUUID bfac0486-cefe-11ed-a79c-005056ae23aa \
                                --networkFile useCases/InputData/multiplex/1/PPI_HiUnion_LitBM_APID_gene_names_190123.tsv \
                                --simple True


.. _netCreation:

================================
Networks creation
================================

.. _pathwaysOfInterestNet:

Pathways/processes of interest network
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This kind of network can be build using the ``networkCreation`` method.

By default, the network is build using rare disease pathways extracted automatically from WikiPathways.

The created network will be a disconnected network (i.e. no link between nodes). To have a proper SIF format, every nodes
will be link to itself.

--networksPath PATH
    Output repository name where the pathways/processes network will be saved.

--bipartitePath PATH
    Output repository name where the bipartite gene-pathway will be saved.

--networksName FILENAME
    You can give a name to the pathway network. The created file will be in SIF file format.
    ``[default: WP_RareDiseasesNetwork.sif]``

--bipartiteName FILENAME
    You can give a name to the bipartite. It's a tab-separated file.
    ``[default: Bipartite_WP_RareDiseases_geneSymbols.tsv]``

-o, --outputPath PATH
    Name of the folder to save complementary results (i.e. request results)
    ``[default: OutputResults]``

Moreover, you can provide your own pathways/processes of interest file using ``--GMT`` parameter.

.. tabs::

    .. group-tab:: Data extracted from requests

        .. code-block:: bash

            odamnet networkCreation --networksPath useCases/InputData/multiplex/2/ \
                                            --networksName WP_RareDiseasesNetwork_fromRequest.sif \
                                            --bipartitePath useCases/InputData/bipartite/ \
                                            --bipartiteName Bipartite_WP_RareDiseases_geneSymbols_fromRequest.tsv \
                                            --outputPath useCases/OutputResults_useCase1
    .. group-tab:: Data provided by users

        .. code-block:: bash

            odamnet networkCreation --networksPath useCases/InputData/multiplex/2/ \
                                            --networksName pathwaysOfInterestNetwork_fromPaper.sif \
                                            --bipartitePath useCases/InputData/bipartite/ \
                                            --bipartiteName Bipartite_pathOfInterest_geneSymbols_fromPaper.tsv \
                                            --GMT useCases/InputData/PathwaysOfInterest.gmt \
                                            --outputPath useCases/OutputResults_useCase2

Principle
~~~~~~~~~~~~

Input parameters for network downloading
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use-case command lines
~~~~~~~~~~~~~~~~~~~~~~~~

.. _netUsed:

================================
Networks used
================================

Genes multilayer network
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Protein-Protein Interaction (PPI) network
""""""""""""""""""""""""""""""""""""""""""""

The Protein-Protein Interaction (PPI) network is obtained from fusion of three datasets : APID, Hi-Union [2]_
and Lit-BM [3]_. It's composed of:

- 15,390 3 nodes

- 131,087 edges

- UUID: |netPPI|

Molecular complexes network
"""""""""""""""""""""""""""""""

Molecular complexes network is constructed from the fusion of Hu.map [4]_ and Corum [5]_. It's composed of:

- 8,497 nodes

- 62,073 edges

- UUID: |netComplex|

Reactome pathways network
""""""""""""""""""""""""""""

The Reactome pathways network was build using data derived from Reactome protein-protein interaction data [6]_.
It's composed of:

- 4,598 nodes

- 19,292 edges

- UUID: |netReactome|

Use-case command lines
~~~~~~~~~~~~~~~~~~~~~~~~

.. tabs::

    .. group-tab:: PPI network

        .. code-block:: bash

            odamnet networkDownloading  --netUUID bfac0486-cefe-11ed-a79c-005056ae23aa \
                                        --networkFile useCases/InputData/multiplex/1/PPI_HiUnion_LitBM_APID_gene_names_190123.tsv \
                                        --simple True

    .. group-tab:: Molecular complexes network

        .. code-block:: bash

            odamnet networkDownloading  --netUUID 419ae651-cf05-11ed-a79c-005056ae23aa \
                                        --networkFile useCases/InputData/multiplex/1/Complexes_gene_names_190123.tsv \
                                        --simple True

    .. group-tab:: Reactome pathways network

        .. code-block:: bash

            odamnet networkDownloading  --netUUID b13e9620-cefd-11ed-a79c-005056ae23aa \
                                        --networkFile useCases/InputData/multiplex/1/Pathways_reactome_gene_names_190123.tsv \
                                        --simple True


.. _DDnet:

Disease-disease similarity network
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Disease-disease similarity network creation
""""""""""""""""""""""""""""""""""""""""""""""

| *Data was download on the 2022/06/11.*
| |annot|_ *and* |onto|_ *are coming from HPO.*

.. _annot: https://hpo.jax.org/app/data/annotation
.. |annot| replace:: *Annotations*
.. _onto: https://hpo.jax.org/app/data/ontology
.. |onto| replace:: *ontologies*

We constructed a disease-disease network based on the phenotype similarity between diseases. A disease is defined as
a set of phenotypes and each phenotype is associated to the Human Ontology Project IDs (HPO).

The similarity score is calculated based on the number of shared phenotypes between two diseases ([3]_, [2]_, [1]_).
Every pairs of diseases will have a similarity score. For each disease we selected the 5 most similar diseases to
create the network.

The **disease-disease** network contains 33,925 edges and 8,264 diseases.

.. tip::

    | You can use any network and multilayer network as input.
    | :octicon:`alert;1em` Be careful with the configuration file and the gene IDs used.

Gene-disease bipartite
""""""""""""""""""""""""

| *Data was download on the 2022/09/27.*
| |assos|_ *between genes and diseases file is coming from HPO*

.. _assos: https://hpo.jax.org/app/data/annotation
.. |assos| replace:: *Associations*


The **molecular multilayer network** is connected to the **disease-disease similarity network** with the **gene-disease bipartite**.
The bipartite contains 6,564 associations (4,483 genes and 5,878 diseases).


References
============

.. [1] NDEx
.. [2] PPI Network
.. [3] PPI Network
.. [4] Molecular complexes Network
.. [5] Molecular complexes Network
.. [6] Reactome Network

.. _netPPI: https://www.ndexbio.org/viewer/networks/bfac0486-cefe-11ed-a79c-005056ae23aa
.. |netPPI| replace:: bfac0486-cefe-11ed-a79c-005056ae23aa
.. _netComplex: https://www.ndexbio.org/viewer/networks/419ae651-cf05-11ed-a79c-005056ae23aa
.. |netComplex| replace:: 419ae651-cf05-11ed-a79c-005056ae23aa
.. _netReactome: https://www.ndexbio.org/viewer/networks/b13e9620-cefd-11ed-a79c-005056ae23aa
.. |netReactome| replace:: 	b13e9620-cefd-11ed-a79c-005056ae23aa