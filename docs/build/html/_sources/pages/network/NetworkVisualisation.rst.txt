================================
Networks visualisation
================================

Results of active module identification (AMI) and random walk with restart (RWR) approaches can be visualised using
Cytoscape [1]_.

This page contains a guideline, step by step, to create network visualisation of results such as those presented in
this documentation.

Active module identification results visualisation
====================================================

.. tip::

    .. cssclass:: italic

        To run an Active Module Identification with data requested, see :ref:`Use-case 1 <useCase1_AMI>`
        or with data provided by users, see :ref:`Use-case 2 <useCase2_AMI>`.

The :numref:`cytoscapeAMI` is an example of AMI results visualisation.

.. _cytoscapeAMI:
.. figure:: ../../pictures/UseCase1/UseCase1_AMI.png
    :alt: AMI network visualisation
    :align: center

    : Use-case 1 AMI analysis visualisation (from :numref:`dominoUsage1Fig`). We use Cytoscape [1]_ to create network
    visualisation and Omics Visualizer [2]_ to add overlap results to active modules.

Step by step guidelines
---------------------------

1. Import files
~~~~~~~~~~~~~~~~~~

.. _cytoscapeImportFile_AMI:
.. figure:: ../../pictures/Cytoscape/Cytoscape_import_AMI.png
    :alt: cytoscapeImportFile_AMI
    :width: 400
    :align: center

    : Step 1 - Import files

- **Import Network** from File: ``DOMINO_*_activeModulesNetwork.txt``
- **Import Table** from File: ``DOMINO_*_activeModules.txt`` (*Import Data as Node Table Columns*)

2. Add donuts
~~~~~~~~~~~~~~~~~~

.. _cytoscapeOmicsVisualizer_AMI:
.. figure:: ../../pictures/Cytoscape/Cytoscape_omicsVisualizer.png
    :alt: cytoscapeOmicsVisualizer_AMI
    :width: 600
    :align: center

    : Step 2 - Add donuts using OmicsVisualizer [2]_ app

1. **Omics Visualizer** [2]_ **table** from File: ``DOMINO_*_overlapAMresults4Cytoscape.txt``
2. Manage table **connections**: link network node table with right identifiers

    - Network: *sharedname*
    - Table: *geneSymbol*

3. **Donut Chart Visualisation**: Add overlap results using donuts (Use *termTitle*)

3. Network style
~~~~~~~~~~~~~~~~~~~

.. _cytoscapeStyle_AMI:
.. figure:: ../../pictures/Cytoscape/Cytoscape_styleAMI.png
    :alt: cytoscapeStyle_AMI
    :scale: 50
    :align: left

    : Step 3 - Apply style that you want

- Border Width = ``5.0``
- Fill Color = ``ActiveGenes``
    - True #CCCCCC
    - False #FFFFFF
- Label Font Size = ``20``
- Shape = ``Ellipse``
- Size = ``50``
- ``Lock node width and height``

|
|
|
|
|
|
|
|
|
|
|
|
4. Active module selection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _cytoscapeFilter_AMI:
.. figure:: ../../pictures/Cytoscape/Cytoscape_filterAMI.png
    :alt: cytoscapeFilter_AMI
    :width: 600
    :align: center

    : Step 4 - Select identified active module with a significant overlap

1. **Filter**: Select nodes with ``overlapSignificant = True``
2. **New Network**: From Selected Nodes, All Edges

.. tip::

    You can select modules that you are interested in directly (Ctrl + mouse drag) then create a new network from
    selected nodes (step 2 above).

5. Create legends
~~~~~~~~~~~~~~~~~~~~~

.. _cytoscapeLegend_AMI:
.. figure:: ../../pictures/Cytoscape/Cytoscape_omicsVisualizer_addLegend.png
    :alt: cytoscapeLegend_AMI
    :width: 600
    :align: center

    : Step 5 - Add legend using Omics Visualizer [2]_

Random walk with restart results visualisation
================================================

.. tip::

    .. cssclass:: italic

        To perform a RWR with data extracted from requests, see :ref:`Use-case 1 <useCase1_RWR>` or with data
        provided by users, see :ref:`Use-case 2 <useCase2_RWR>`.

The :numref:`cytoscapeRWR` is an example of RWR results visualisation.

.. _cytoscapeRWR:
.. figure:: ../../pictures/UseCase1/UseCase1_RWR.png
    :alt: cytoscapeRWR
    :align: center

    : Use-case 1 RWR analysis visualisation (from :numref:`useCase1_pathwaysNetworkRWR`). We use Cytoscape [1]_ to
    create network visualisation.

Step by step guidelines
---------------------------

To visualise the RWR results using network representation, use the following steps:


2. Management of nodes table
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


- Create **two new columns** named ``label`` as *string* and ``keep`` as *boolean* in the node table
- **Filter**: Select genes nodes

    - Fill ``label`` column with ``=$name`` and apply to selected nodes
    - Fill ``keep`` column with ``=$seed`` and apply to selected nodes
    - Sort by ``score`` (decrease) and select the 30th first genes that are not a seed (selected nodes from selected rows)
    - Fill ``keep`` column with ``=True`` and apply to selected nodes

7. **Filter**: Select pathways nodes

    - Fill ``label`` column with pathway names (``=$pathway``)
    - Fill ``keep`` column with condition score (``=$score>=0.0002083975629882177``)

8. **Filter**: Select nodes with ``keep = True``
9. **New Network**: From Selected Nodes, All Edges
10. Edit and Remove Duplicate Edges
11. **Style**:

.. list-table:: Network Style
    :header-rows: 1
    :stub-columns: 1

    *   -
        - All Nodes
        - Disease Nodes
    *   - Border Width
        - 5.0
        - 5.0
    *   - Fill Color
        - | Column seed
          | True: CCCCCC
          | False: FFFFFF
        - DD3497
    *   - Label Front Size
        - 20boldlink
        - 50
    *   - Shape
        - Ellipse
        - Triangle
    *   - Lock node width and height
        - True
        - True
    *   - Size
        - 50
        - 100
    *   - Label
        - label
        - label

12. Change network layout (here is yFiles Organic Layout)




1. Import files
~~~~~~~~~~~~~~~~~~

.. _cytoscapeImportFile_RWR:
.. figure:: ../../pictures/Cytoscape/Cytoscape_import_RWR.png
    :alt: cytoscapeImportFile_AMI
    :width: 400
    :align: center

    : Step 1 - Import files

- **Import Network** from File: ``resultsNetwork_useCase1.sif``
- **Import Table** from File: ``multiplex_1.tsv`` and ``multiplex_2.tsv``
- **Import Table** from File: ``seeds.4Cytoscape``

    - Change column names: ``node`` for column 1 and ``seed`` for column 2

.. tip::

   How create the **seeds.4Cytoscape** file ?

   .. code-block:: bash

        awk -F"\t" 'NR==FNR{a[$1]; next} {if($2 in a){print $2"\tTrue"}else{print $2"\tFalse"}}' seeds.txt multiplex_1.tsv > seeds.4Cytoscape

- **Import Table** from File: ``diseasesDescription.txt``

    - Change column names: ``node`` for column 1, ``pathways`` for column 2 and ``score`` for column 3

.. tip::

   How create the **diseasesDescription.txt** file ?

   .. code-block:: bash

        awk -F"\t" 'NR==FNR{a[$1]; next} {if($1 in a){print $1"\t"$2}}' RWR_top20.txt ../../OutputOverlapResults/WP_RareDiseases_request_2022_09_07.gmt > diseasesDescription.txt






2. Add donuts
~~~~~~~~~~~~~~~~~~

.. _cytoscapeOmicsVisualizer_AMI:
.. figure:: ../../pictures/Cytoscape/Cytoscape_omicsVisualizer.png
    :alt: cytoscapeOmicsVisualizer_AMI
    :width: 600
    :align: center

    : Step 2 - Add donuts using OmicsVisualizer [2]_ app

1. **Omics Visualizer** [2]_ **table** from File: ``DOMINO_*_overlapAMresults4Cytoscape.txt``
2. Manage table **connections**: link network node table with right identifiers

    - Network: *sharedname*
    - Table: *geneSymbol*

3. **Donut Chart Visualisation**: Add overlap results using donuts (Use *termTitle*)

3. Network style
~~~~~~~~~~~~~~~~~~~

.. _cytoscapeStyle_AMI:
.. figure:: ../../pictures/Cytoscape/Cytoscape_styleAMI.png
    :alt: cytoscapeStyle_AMI
    :scale: 50
    :align: left

    : Step 3 - Apply style that you want

- Border Width = ``5.0``
- Fill Color = ``ActiveGenes``
    - True #CCCCCC
    - False #FFFFFF
- Label Font Size = ``20``
- Shape = ``Ellipse``
- Size = ``50``
- ``Lock node width and height``

|
|
|
|
|
|
|
|
|
|
|
|
4. Active module selection
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _cytoscapeFilter_AMI:
.. figure:: ../../pictures/Cytoscape/Cytoscape_filterAMI.png
    :alt: cytoscapeFilter_AMI
    :width: 600
    :align: center

    : Step 4 - Select identified active module with a significant overlap

1. **Filter**: Select nodes with ``overlapSignificant = True``
2. **New Network**: From Selected Nodes, All Edges

.. tip::

    You can select modules that you are interested in directly (Ctrl + mouse drag) then create a new network from
    selected nodes (step 2 above).

5. Create legends
~~~~~~~~~~~~~~~~~~~~~

.. _cytoscapeLegend_AMI:
.. figure:: ../../pictures/Cytoscape/Cytoscape_omicsVisualizer_addLegend.png
    :alt: cytoscapeLegend_AMI
    :width: 600
    :align: center

    : Step 5 - Add legend using Omics Visualizer [2]_


References
=============
.. [1] Shannon, P., Markiel, A., Ozier, O., Baliga, N. S., Wang, J. T., Ramage, D., ... & Ideker, T. (2003). Cytoscape: a software environment for integrated models of biomolecular interaction networks. Genome research, 13(11), 2498-2504.
.. [2] Legeay, M., Doncheva, N. T., Morris, J. H., & Jensen, L. J. (2020). Visualize omics data on networks with Omics Visualizer, a Cytoscape App. F1000Research, 9.



.. _networkAMI:
.. _networkRWR:

Random Walk with Restart analysis network visualisation
----------------------------------------------------------------

The Random Walk with Restart (RWR) analysis gives in output a score for each node. Theses score are used to selected
the most relevant connections between nodes. You can visualise theses connections with Cytoscape.

The following :numref:`cytoscapeRWR` is an example of visualisation:

.. figure:: ../../pictures/RWR_pathwaysNet_useCase1.png
    :alt: useCase 1 RWR
    :align: center

    : Visualisation of network using Cytoscape [1]_


.. cssclass:: italic

    To perform a RWR with data extracted from requests, see :ref:`Use-case 1 <useCase1_AMI>`
    or with data provided by users, see :ref:`Use-case 2 <useCase2_AMI>`.

.. [3] https://github.com/cytoscape/legend-creator
.. [4] Baptista, A., Gonzalez, A., & Baudot, A. (2022). Universal multilayer network exploration by random walk with restart. Communications Physics, 5(1), 1-9.
