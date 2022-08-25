==================================================
README
==================================================

Analyse the link between environmental factors and Rare Diseases. 

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
Python modules required are listed in the requirements.txt file. To install them :

.. code-block:: bash

   python3 install requirements.txt

Usage
----------------

Three different methods are available to analysis your data : 

- Overlap analysis
- Active Module Identification (using DOMINO)
- Random Walk with Restart (using multiXrank)

.. code-block:: bash

   python3 main.py [overlap|domino|multixrank|networkCreation] [ARGS]

Examples
----------------

To study the overlap between Rare Diseases (from WikiPathways (WP)) and genes targeted by environmental factors (extracted
from CTD database), three approaches are implemented :

Overlap analysis
^^^^^^^^^^^^^^^^^
This method calculates the overlap between target genes and Rare Disease pathways. It's looking for direct association :
target genes that take part of pathways.

.. code-block:: bash

   python3 main.py overlap --factorList FILENAME

Active Module Identification
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Target genes are defined as ``active genes`` to search Active Modules (AM), based on a molecular network (e.g.
Protein-Protein Interaction network, PPI). Then, an overlap analysis is performed between AM (target genes + linked genes)
and Rare Disease pathways. The target gene list is extended to others related genes.

.. code-block:: bash

   python3 main.py domino --factorList FILENAME --networkFile FILENAME

Network and bipartite creation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
You might need to create a disconnected network of Rare Disease pathways and it's corresponding gene-disease bipartite.
You will use this network to perform a random walk method.

.. code-block:: bash

   python3 main.py networkCreation --networksPath PATH --bipartitePath PATH

Random Walk with Restart
^^^^^^^^^^^^^^^^^^^^^^^^^^
The third approach mesures the proximity of every gene within a multilayer to the target genes.
It's a diffusion analysis from the factors through different molecular interactions to the disease.

.. code-block:: bash

   python3 main.py multixrank --factorList FILENAME --configPath PATH --networksPath PATH --seedsFile FILENAME --sifFileName FILENAME


.. footnotes::

    The documentation is in the ``doc`` folder for now. Will is it hosted by ReadTheDocs after ?