.. EnvironmentProject documentation master file, created by
   sphinx-quickstart on Fri Jul 22 11:43:41 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

EnvironmentProject's documentation
==================================

.. important::
   This project was created within the EJRP RD project.

.. toctree::
   :caption: Quickstart
   :titlesonly:

   pages/Installation

.. toctree::
   :maxdepth: 3
   :caption: Methods
   :titlesonly:

   pages/methods/methods_overview
   pages/methods/methods_overlap
   pages/methods/methods_AMI
   pages/methods/methods_RWR
   pages/methods/methods_newNetwork
   pages/methods/Cytoscape

.. toctree::
   :maxdepth: 2
   :caption: Analysis

   pages/analysis/example1
   pages/analysis/example2
   pages/analysis/example3

.. toctree::
   :maxdepth: 1
   :caption: File formats

   pages/formats/Input
   pages/formats/Output

.. toctree::
   :maxdepth: 1
   :caption: Functions description

   pages/functions/fcts_main
   pages/functions/fcts_overlap
   pages/functions/fcts_AMI
   pages/functions/fcts_RWR
   pages/functions/fcts_newNetwork


.. seealso::

    Module :py:mod:`overlap`
      Documentation of the :py:mod:`zipfile` standard module.

.. code-block:: bash
   :emphasize-lines: 3,5

   def some_function():
       interesting = False
       print 'This line is highlighted.'
       print 'This one is not...'
       print '...but this one is.'


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
