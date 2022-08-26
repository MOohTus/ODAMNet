==================================================
README
==================================================

The goal of this project is to develop computational approaches to analyse the links and overlaps between environmental factors, their molecular targets, and rare diseases pathways.

Installation 
----------------

1. Clone the repository from Github

.. code-block:: bash

   git clone https://github.com/MOohTus/EnvironmentProject.git

2. Then, go inside

.. code-block:: bash

   cd EnvironmentProject/

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

   python3 main.py [overlap|domino|multixrank|networkCreation] [ARGS]

Examples
----------------

Three approaches are implemented to study the relationships between Rare Diseases (from WikiPathways (WP)) and genes targeted by environmental factors (extracted
from CTD database):

Overlap analysis
^^^^^^^^^^^^^^^^^
This method computes the overlap between CTD-associated target genes and WP Rare Disease pathways. It is looking for direct associations, i.e., target genes that are part of pathways.

.. code-block:: bash

   python3 main.py overlap --factorList FILENAME

Active Module Identification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
CTD-associated target genes are defined as "active genes" to search for Active Modules (AM) on a molecular network (e.g.
Protein-Protein Interaction network, PPI). Then, an overlap analysis is performed between AM (containing target genes + associated genes)
and Rare Disease pathways.
The target gene list is extended to others related genes.%A% I'm not sure to get this sentence?

.. code-block:: bash

   python3 main.py domino --factorList FILENAME --networkFile FILENAME

Network and bipartite creation %A% peut etre que ceci devrait etre une sous-section de RWR car c'est utilisé seulement la, non ? Et du coup on parle de 3 méthodes mais il y a 4 sous titres
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
You might need to create a disconnected network of Rare Disease pathways and it's corresponding gene-disease bipartite. %A% je pense que disconnected network aurait besoin d'une definition, un peu plus d'explication sur pourquoi on fait ca
You will use this network to perform a random walk method.

.. code-block:: bash

   python3 main.py networkCreation --networksPath PATH --bipartitePath PATH

Random Walk with Restart
^^^^^^^^^^^^^^^^^^^^^^^^^^
The third approach mesures the proximity of every gene to the target genes within a multilayer network.
It's a diffusion analysis from the factors through different molecular interactions to the disease. %A% c'est un peu compliqué et les deux phrases ne sont pas écrite dans le meme ordre, on ne sait pas trop a quoi correspond "factor" car ce n'a pas été utilisé avant

.. code-block:: bash

   python3 main.py multixrank --factorList FILENAME --configPath PATH --networksPath PATH --seedsFile FILENAME --sifFileName FILENAME


The documentation is in the ``doc/html/index.html`` for now. Will is it hosted by ReadTheDocs after ?
