.. ODAMNet documentation master file, created by
   sphinx-quickstart on Fri Jul 22 11:43:41 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

ODAMNet documentation
==================================

ODAMNet is a set of three different approaches to study the molecular relationship between chemicals and rare diseases.
These three approaches are **Overlap analysis**, **diffusion analysis** using random walk with restart and
**active module identification**.

This project was created within the framework of the `EJRP-RD project <https://www.ejprarediseases.org/>`_.

.. note:: 

   If you use ODAMNet, please cite our publication:

   Térézol M, Baudot A, Ozisik O. ODAMNet: A Python package to identify molecular relationships between chemicals and rare diseases using overlap, active module and random walk approaches. SoftwareX. 2024;26:101701. doi: `10.1016/j.softx.2024.101701 <https://www.softxjournal.com/article/S2352-7110(24)00072-4/fulltext>`.


If you use ODAMNet, please cite our publication:

> Térézol M, Baudot A, Ozisik O. ODAMNet: A Python package to identify molecular relationships between chemicals and rare diseases using overlap, active module and random walk approaches. SoftwareX. 2024;26:101701. doi: `10.1016/j.softx.2024.101701 <https://www.softxjournal.com/article/S2352-7110(24)00072-4/fulltext>`.


.. toctree::
   :caption: Quickstart
   :titlesonly:

   pages/Installation

.. toctree::
   :maxdepth: 2
   :caption: Approaches

   pages/approaches/methods_overview
   pages/approaches/methods_overlap
   pages/approaches/methods_AMI
   pages/approaches/methods_RWR

.. toctree::
   :maxdepth: 2
   :caption: Networks

   pages/network/NetworkDownloading
   pages/network/NetworkCreation
   pages/network/NetworkVisualisation
   pages/network/NetworkUsed

.. toctree::
   :maxdepth: 2
   :caption: Use-cases

   pages/analysis/usecase1
   pages/analysis/usecase2

.. toctree::
   :maxdepth: 2
   :caption: File formats

   pages/formats/Input
   pages/formats/Output

.. toctree::
   :maxdepth: 1
   :caption: Code description

   pages/functions/fcts_arguments
   pages/functions/fcts_description

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
