==================================================
Installation
==================================================

To use ODAMNet you need ``python>=3.9``.

From PyPi - *It's on going*
-------------------------------

ODAMNet is available as python package. You can easily install it using ``pip``.

.. code-block:: bash

   pip install odamnet

From Conda - *It's on going*
--------------------------------

You can also install it from `bioconda <https://bioconda.github.io/index.html>`_ using ``conda``.

.. code-block:: bash

   conda install odamnet

From Github
-------------

1. Clone the repository from Github

.. code-block:: bash

   git clone https://github.com/MOohTus/ODAMNet.git

2. Then, install it

.. code-block:: bash

   pip install -e ODAMNet/

==================================================
Usage
==================================================

Three different approaches are available to analyse your data:

    #. Overlap analysis
    #. Active Module Identification (using DOMINO)
    #. Random Walk with Restart (using multiXrank)


.. code-block:: bash

   odamnet [overlap|domino|multixrank] [ARGS]


Before running the last method, you could need to create a network from data used:

.. code-block:: bash

   odamnet networkCreation [ARGS]

You can display help:

.. code-block:: bash

   odamnet [-h] [--help]
