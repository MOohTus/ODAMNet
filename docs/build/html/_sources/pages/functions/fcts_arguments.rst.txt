==================================================
Input parameters for each approach
==================================================

ODAMNet script
=================

.. click:: odamnet.odamnet:main
   :prog: odamnet

Overlap
=============

.. click:: odamnet.odamnet:overlap
   :prog: odamnet overlap
   :nested: full
   :commands: overlap

DOMINO
=============

.. click:: odamnet.odamnet:DOMINO
   :prog: odamnet domino
   :nested: full
   :commands: domino

RWR
=============

.. click:: odamnet.odamnet:multiXrank
   :prog: odamnet multixrank
   :nested: full
   :commands: multixrank

Network creation
=====================

.. click:: odamnet.odamnet:createNetworkFiles
   :prog: odamnet networkCreation
   :nested: full
   :commands: networkCreation

Network downloading
======================

.. click:: odamnet.odamnet:networkDownloading
   :prog: odamnet networkDownloading
   :nested: full
   :commands: networkDownloading

.. important::

    ``--chemicalsFile``, ``--CTD_file`` and ``--targetGenesFile`` parameters are exclusive, only one has to be use. This input is **required**.

.. important::

    ``--backgroundFile`` and ``--GMT`` parameters have always to be **given together**.





