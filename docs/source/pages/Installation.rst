==================================================
Installation
==================================================

To use ODAMNet you need ``python>=3.9``.

From PyPI
-------------------------------

ODAMNet is available in PyPI_. You can easily install it using ``pip``.

.. code-block:: bash

   python3 -m pip install odamnet

From Conda - *It's ongoing*
--------------------------------

ODAMNet is also available in bioconda_ using ``conda``.

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
    #. Active Modules Identification (AMI, using DOMINO_)
    #. Random Walk with Restart (RWR, using multiXrank_)

To run one of these approaches:

.. code-block:: bash

   odamnet [overlap | domino | multixrank] [ARGS]

To create a disconnected rare disease pathways network and its corresponding gene - rare disease pathways bipartite
network (*these networks may be used for the RWR approach*):

.. code-block:: bash

   odamnet networkCreation [ARGS]

To download biological networks directly from NDEx_:

.. code-block:: bash

   odamnet networkDownloading [ARGS]

To display help:

.. code-block:: bash

   odamnet [-h] [--help]

.. _PyPI: https://pypi.org/project/ODAMNet/
.. _bioconda: https://anaconda.org/bioconda/odamnet
.. _DOMINO: http://domino.cs.tau.ac.il
.. _multiXrank: https://multixrank-doc.readthedocs.io/en/latest/index.html
.. _NDEx: https://www.ndexbio.org/
