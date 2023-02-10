==================================================
README
==================================================

The goal of this project is to develop computational approaches to analyse the links and overlaps between environmental factors, their molecular targets, and rare diseases pathways.

Installation 
----------------

1. Clone the repository from Github

.. code-block:: bash

   git clone https://github.com/MOohTus/ODAMNet.git

2. Then, go inside

.. code-block:: bash

   cd ODAMNet/

3. Run the setup.py file from that directory

.. code-block:: bash

   python3 setup.py install

Requirements
----------------

The required Python modules are listed in the requirements.txt file. To install them:

.. code-block:: bash

   python3 install requirements.txt

Usage
----------------

Three different approaches are available to analyse your data: 

- Overlap analysis
- Active Module Identification (using DOMINO)
- Random Walk with Restart (using multiXrank)

.. code-block:: bash

   odamnet [overlap|domino|multixrank|networkCreation] [ARGS]

Examples
----------------

Three approaches are implemented to study the relationships between Rare Diseases (from WikiPathways (WP)) and genes targeted by environmental factors (extracted
from CTD database):

Overlap analysis
"""""""""""""""""""""

This method computes the overlap between CTD-associated target genes and WP Rare Disease pathways. It is looking for direct associations, i.e., target genes that are part of pathways.

.. code-block:: bash

   odamnet overlap --factorList FILENAME

Active Module Identification
"""""""""""""""""""""""""""""""""

CTD-associated target genes are defined as "active genes" to search for Active Modules (AM) on a molecular network (e.g.
Protein-Protein Interaction network, PPI). Then, an overlap analysis is performed between AM (containing target genes + associated genes)
and Rare Disease pathways.
The target gene list is extended to others related genes.%A% I'm not sure to get this sentence?

.. code-block:: bash

   odamnet domino --factorList FILENAME --networkFile FILENAME

Random Walk with Restart
""""""""""""""""""""""""""""

Network and bipartite creation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To perform a Random Walk with Restart through molecular multilayer and diseases network, you need to create a disease network
and link it to the multilayer (i.e. with the bipartite). This network will not have connection between diseases (i.e. disconnected network).
Diseases will be only connected with genes (in the multilayer) that are involved in disease pathways.

.. code-block:: bash

   odamnet networkCreation --networksPath PATH --bipartitePath PATH

multiXrank
^^^^^^^^^^^^^^^^^^

The third approach mesures the proximity of every nodes (g.e. genes, diseases) to the target genes within a multilayer network.
The walk starts from target genes and diffuses through the multilayer composed of different molecular interactions to the disease.

.. code-block:: bash

   odamnet multixrank --factorList FILENAME --configPath PATH --networksPath PATH --seedsFile FILENAME --sifFileName FILENAME


The documentation is in the ``doc/html/index.html`` for now. Will is it hosted by ReadTheDocs after ?
