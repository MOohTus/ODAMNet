==================================================
Installation
==================================================

To use ODAMNet you need ``python>=3.9``.

From PyPi
-------------------------------

ODAMNet is available as python package. You can easily install it using ``pip``.

.. code-block:: bash

   python3 -m pip install odamnet

From Conda - *It's ongoing*
--------------------------------

It is available in `bioconda <https://bioconda.github.io/index.html>`_ using ``conda``.

.. code-block:: bash

   conda install odamnet

From Github
-------------

1. Clone the repository from GitHub

.. code-block:: bash

   git clone https://github.com/MOohTus/ODAMNet.git

2. Then, install it

.. code-block:: bash

   python3 -m pip install -e ODAMNet/

==================================================
Usage
==================================================

Three different approaches are available:

    #. Overlap analysis
    #. Active Modules Identification (AMI, using DOMINO)
    #. Random Walk with Restart (RWR, using multiXrank)


.. code-block:: bash

   odamnet [overlap|domino|multixrank] [ARGS]

The RWR approach requires the bipartite network of gene - rare disease associations. You can create this network using your pathways of interest:

.. code-block:: bash

   odamnet networkCreation [ARGS]

You can display help:

.. code-block:: bash

   odamnet [-h] [--help]
