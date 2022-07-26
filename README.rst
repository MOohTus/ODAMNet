README
========

Analyse the link between environmental factors and Rare Diseases. 

Installation 
==============

Requierements
---------------

First, the analysis needs these Python modules :

1. requests
2. SPARQLWrapper
3. multixrank
4. pandas
5. scipy
6. statsmodels
7. alive_progress
8. click_option_group
9. click
10. customClick

Installation 
-------------

1. Clone the repository from Github

.. code-block:: bash

   git clone https://github.com/MOohTus/EnvironmentProject.git

2. Then, go inside

.. code-block:: bash

   cd EnvironmentProject/

3. Just run the setup.py file from that directory

.. code-block:: bash

   python3 setup.py install

Usage
======

Help
------

.. code-block:: python3

   python3 main.py -h

Example
========



Overview
==========

Three different methods are available to analysis your data : 

- Overlap analysis
- Active Module Identification (using DOMINO)
- Random Walk with Restart (using multiXrank)

