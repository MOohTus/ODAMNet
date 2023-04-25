.. _netUsed:

================================
Networks used
================================

In this section, we present networks used in the use-cases.

We propose to apply the random walk with restart (RWR) approach on two different multilayers.

.. _RWRFig:
.. figure:: ../../pictures/MultilayerComposition.png
    :alt: RWR networks
    :align: center

    : Multilayers composition: On the left, multilayer is composed of genes multilayer network and pathways/processes
      of interest network (disconnected network). On the right, the multilayer is composed of genes multiplayer network
      and disease-disease similarity network.

Multilayers are composed of:

- genes multilayer network + pathways/processes of interest network (:numref:`RWRFig` - left part)

- genes multilayer network + disease-disease similarity network (:numref:`RWRFig` - right part)

Genes multilayer network
===========================

The genes multilayer network is composed of three different networks. Nodes are identical between networks, but the
relationships between them are coming from different sources. Networks are downloaded from the |NDEx|_ (NDEx) [1]_.

.. _PPInet:

Protein-Protein Interaction (PPI) network
-------------------------------------------

The Protein-Protein Interaction (PPI) network is obtained from fusion of three datasets : Hi-Union and Lit-BM [2]_ and
APID [3]_. It's composed of:

- 15,390 3 nodes

- 131,087 edges

- UUID: |netPPI|_

Molecular complexes network
-----------------------------

Molecular complexes network is constructed from the fusion of Hu.map [4]_ and Corum [5]_. It's composed of:

- 8,497 nodes

- 62,073 edges

- UUID: |netComplex|_

Reactome pathways network
---------------------------

The Reactome pathways network was build using data derived from Reactome protein-protein interaction data [6]_.
It's composed of:

- 4,598 nodes

- 19,292 edges

- UUID: |netReactome|_

Use-case command lines
------------------------

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

Pathways/processes of interest network
========================================

In the use-case 1, we are using **data retrieved from databases**. So, we created a rare disease pathways network with
data retrieved from WikiPathways [7]_. The network is composed of 104 nodes and the bipartite contains 4,612 interactions
between genes and rare disease pathways.

In the use-case 2, we are **provided data from a previous study** [8]_. We created a disconnected network with pathways
or processes related to Congenital Anomalies of the Kidney and Urinary Tract (CAKUT) as nodes. The network is composed of
13 nodes and the bipartite network contains 1,655 interactions between genes and pathways and processes related to
CAKUT.

To know how to create these two networks, see the :doc:`../network/NetworkCreation` page.

_DDnet:

Disease-disease similarity network
====================================

Disease-disease similarity network creation
----------------------------------------------

| *Data were downloaded on June 11th, 2022*
| |annot|_ *and* |onto|_ *are coming from HPO*

We constructed a disease-disease network based on the phenotype similarity between diseases. A disease is defined as
a set of phenotypes and each phenotype is associated to the Human Ontology Project IDs (HPO) [9]_.

The similarity score is calculated based on the number of shared phenotypes between two diseases ([10]_, [11]_, [12]_).
Every pairs of diseases will have a similarity score. For each disease we selected the 5 most similar diseases to
create the network.

The **disease-disease** similarity network contains 33,925 edges and 8,264 diseases.

Gene-disease bipartite
-------------------------

| *Data were downloaded on September 27th, 2022*
| |assos|_ *between genes and diseases file is coming from HPO*

The **molecular multilayer network** is connected to the **disease-disease similarity network** with the
**gene-disease bipartite**. The bipartite contains 6,564 associations (4,483 genes and 5,878 diseases).

References
============

.. [1] Pratt D, Chen J, Welker D, et al. NDEx, the Network Data Exchange. Cell Syst. 2015;1(4):302-305. doi:10.1016/j.cels.2015.10.001
.. [2] Luck K, Kim DK, Lambourne L, et al. A reference map of the human binary protein interactome. Nature. 2020;580(7803):402-408. doi:10.1038/s41586-020-2188-x
.. [3] Alonso-López D, Campos-Laborie FJ, Gutiérrez MA, et al. APID database: redefining protein-protein interaction experimental evidences and binary interactomes. Database (Oxford). 2019;2019:baz005. Published 2019 Jan 1. doi:10.1093/database/baz005
.. [4] Drew K, Wallingford JB, Marcotte EM. hu.MAP 2.0: integration of over 15,000 proteomic experiments builds a global compendium of human multiprotein assemblies. Mol Syst Biol. 2021;17(5):e10016. doi:10.15252/msb.202010016
.. [5] Giurgiu M, Reinhard J, Brauner B, et al. CORUM: the comprehensive resource of mammalian protein complexes-2019. Nucleic Acids Res. 2019;47(D1):D559-D563. doi:10.1093/nar/gky973
.. [6] Gillespie M, Jassal B, Stephan R, et al. The reactome pathway knowledgebase 2022. Nucleic Acids Res. 2022;50(D1):D687-D692. doi:10.1093/nar/gkab1028
.. [7] Martens, M., Ammar, A., Riutta, A., Waagmeester, A., Slenter, D. N., Hanspers, K., ... & Kutmon, M. (2021). WikiPathways: connecting communities. Nucleic acids research, 49(D1), D613-D621.
.. [8] Ozisik, O., Ehrhart, F., Evelo, C. T., Mantovani, A., & Baudot, A. (2021). Overlap of vitamin A and vitamin D target genes with CAKUT-related processes. F1000Research, 10.
.. [9] Sebastian Köhler, Michael Gargano, Nicolas Matentzoglu, Leigh C Carmody, David Lewis-Smith, Nicole A Vasilevsky, Daniel Danis, Ganna Balagura, Gareth Baynam, Amy M Brower, Tiffany J Callahan, Christopher G Chute, Johanna L Est, Peter D Galer, Shiva Ganesan, Matthias Griese, Matthias Haimel, Julia Pazmandi, Marc Hanauer, Nomi L Harris, Michael J Hartnett, Maximilian Hastreiter, Fabian Hauck, Yongqun He, Tim Jeske, Hugh Kearney, Gerhard Kindle, Christoph Klein, Katrin Knoflach, Roland Krause, David Lagorce, Julie A McMurry, Jillian A Miller, Monica C Munoz-Torres, Rebecca L Peters, Christina K Rapp, Ana M Rath, Shahmir A Rind, Avi Z Rosenberg, Michael M Segal, Markus G Seidel, Damian Smedley, Tomer Talmy, Yarlalu Thomas, Samuel A Wiafe, Julie Xian, Zafer Yüksel, Ingo Helbig, Christopher J Mungall, Melissa A Haendel, Peter N Robinson, The Human Phenotype Ontology in 2021, Nucleic Acids Research, Volume 49, Issue D1, 8 January 2021, Pages D1207–D1217, https://doi.org/10.1093/nar/gkaa1043
.. [10] Westbury SK, Turro E, Greene D, et al. Human phenotype ontology annotation and cluster analysis to unravel genetic defects in 707 cases with unexplained bleeding and platelet disorders. Genome Med. 2015;7(1):36. Published 2015 Apr 9. doi:10.1186/s13073-015-0151-5
.. [11] Valdeolivas, A., Tichit, L., Navarro, C., Perrin, S., Odelin, G., Levy, N., … & Baudot, A. (2019). Random walk with restart on multiplex and heterogeneous biological networks. Bioinformatics, 35(3), 497-505.
.. [12] Baptista, A., Gonzalez, A., & Baudot, A. (2022). Universal multilayer network exploration by random walk with restart. Communications Physics, 5(1), 1-9.


.. _NDEx: https://www.ndexbio.org/
.. |NDEx| replace:: Network Data Exchange
.. _netPPI: https://www.ndexbio.org/viewer/networks/bfac0486-cefe-11ed-a79c-005056ae23aa
.. |netPPI| replace:: bfac0486-cefe-11ed-a79c-005056ae23aa
.. _netComplex: https://www.ndexbio.org/viewer/networks/419ae651-cf05-11ed-a79c-005056ae23aa
.. |netComplex| replace:: 419ae651-cf05-11ed-a79c-005056ae23aa
.. _netReactome: https://www.ndexbio.org/viewer/networks/b13e9620-cefd-11ed-a79c-005056ae23aa
.. |netReactome| replace:: 	b13e9620-cefd-11ed-a79c-005056ae23aa
.. _annot: https://hpo.jax.org/app/data/annotation
.. |annot| replace:: *Annotations*
.. _onto: https://hpo.jax.org/app/data/ontology
.. |onto| replace:: *ontologies*
.. _assos: https://hpo.jax.org/app/data/annotation
.. |assos| replace:: *Associations*