==================================================
Input arguments for each method
==================================================

Main script
=============

.. click:: main:main
   :prog: main

Overlap
=============

.. click:: main:overlap
   :prog: main overlap
   :nested: full
   :commands: overlap

DOMINO
=============

.. click:: main:DOMINO
   :prog: main domino
   :nested: full
   :commands: domino

RWR
=============

.. click:: main:multiXrank
   :prog: main multixrank
   :nested: full
   :commands: multixrank

Network creation
=====================

.. click:: main:createNetworkFiles
   :prog: main networkCreation
   :nested: full
   :commands: networkCreation

.. important::

    ``--factorList``, ``--CTD_file`` and ``--geneList`` options are exclusive, only one has to be use. This three input are **required**

.. important::

    ``--backgroundFile`` and ``--GMT`` options have always to be **given together**.

-----------------------------------------------------------------




