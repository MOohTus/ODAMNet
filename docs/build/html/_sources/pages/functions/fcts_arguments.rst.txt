==================================================
Input parameters for each approach
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

    ``--chemicalsFile``, ``--CTD_file`` and ``--targetGenesFile`` parameters are exclusive, only one has to be use. This input is **required**

.. important::

    ``--backgroundFile`` and ``--GMT`` parameters have always to be **given together**.





