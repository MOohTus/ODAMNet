==================================================
Installation
==================================================

1. Clone the repository from Github

.. code-block:: bash

   git clone https://github.com/MOohTus/EnvironmentProject.git

2. Then, go inside

.. code-block:: bash

   cd EnvironmentProject/

3. Run the setup.py file from that directory

.. code-block:: bash

   python3 setup.py install

==================================================
Requirements
==================================================

Python modules required are listed in the requirements.txt file. To install them :

.. code-block:: bash

   python3 install requirements.txt

==================================================
Usage
==================================================

Three different methods are available to analysis your data :

    #. Overlap analysis
    #. Active Module Identification (using DOMINO)
    #. Random Walk with Restart (using multiXrank)


.. code-block:: bash

   python3 main.py [overlap|domino|multixrank] [ARGS]


Before running the last method, you could need to create a network from data used :

.. code-block:: bash

   python3 main.py networkCreation [ARGS]

You can display help :

.. code-block:: bash

   python3 main.py [-h] [--help]