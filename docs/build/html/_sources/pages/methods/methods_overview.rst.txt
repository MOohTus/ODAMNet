==================================================
Methods overview
==================================================

Analyse the link between environmental factors and Rare Diseases.

Methods
=========

Different approaches are implemented in this tool to analysis link between environmental factor and rare disease pathways :

- :ref:`overlap`
- :ref:`AMI`
- :ref:`RWR`

.. image:: ../../pictures/MethodsOverview.png
   :alt: methods overview


Data source
==============

We want to study the link between target genes and pathways of interest.
Data can be extracted directly from database or given by the user.

Target genes
---------------

Three options :

1. The user may give a list of environmental factors. The script requests CTD database to extract a list of genes that
   are targeted by those environmental factors.
2. The user may give a tsv file with the data from CTD database. This kind of file could be interesting for reproducibility
   or to use a specific data version. The tool extract target genes from this file.
3. The user can directly give a list of genes.

Pathways
---------

Two options :

1. Here, we focus on rare diseases analysis. So, the tool extracts all the pathways that are labeled as rare diseases from
   WikiPathways. The corresponding background file is extracted too, and it is composed of all human pathways.
2. The user may give a GMT file of WikiPathways rare diseases and it's corresponding background file. It could be interesting
   for reproducibility or to use a specific data version. Or, the GMT file might be a custom GMT file with pathways from
   several sources and it has to be given with the corresponding background files.

Examples
-----------

.. tip::

    You can mix input type. For instance, request CTD and give a custom GMT file of pathways of interest.
    Every combination is possible !

We illustrate the documentation with three different examples :

    - :ref:`example1`
    - :ref:`example2`
    - :ref:`example3`
