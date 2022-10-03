================================
Network visualisation
================================

You can visualise network results using Cytoscape [1]_. Here, we describe steps that we used to create network visualisations.

.. _networkAMI:

Active Modules Identification (AMI) network visualisation
------------------------------------------------------------

On the Active Modules (AM) Identification analysis, several AM are generated. You can visualise them using
network representation with Cytoscape.

The following :numref:`cytoscapeAMI` is an example of display :

.. _cytoscapeAMI:
.. figure:: ../../pictures/example1_DOMINO_AMnetwork.png
    :alt: example1 AMI
    :align: center

    : Visualisation of AM using Cytoscape [1]_ and Omics Visualizer [2]_

To create the same display of AM, use the following steps :

1. **Import Network** from File : ``DOMINO_*_activeModulesNetwork.txt``
2. **Import Table** from File : ``DOMINO_*_activeModules.txt``
3. **Omics Visualizer** [2]_ **table** from File : ``DOMINO_*_overlapAMresults4Cytoscape.txt``
4. Manage table **connections** : link network and the previous table

    - Network : *sharedname*
    - Table : *geneSymbol*

5. **Donut Chart Visualization** : Add overlap results using donuts (Use *TermID*)
6. **Style** :

    - Border Width = ``5.0``
    - Fill Color = ``ActiveGenes`` True #CCCCCC False #FFFFFF
    - Label Font = ``20``
    - Shape = ``Circle``
    - ``Lock node width and height``
    - Size = ``50``

7. **Filter** : Select nodes with ``overlapSignificant = True``
8. **New Network** : From Selected Nodes, All Edges
9. Add **legends** using Omics Visualizer [2]_ and Legend Creator [3]_

*To run AM identification with data requested, see* :ref:`Use-case 1 <useCase1_AMI>` *or with your data see* :ref:`Use-case 2 <useCase2_AMI>`.

.. _networkRWR:

Random Walk with Restart analysis (RWR) network visualisation
----------------------------------------------------------------

To explore a network, we use a Random Walk with Restart [4]_ approach. As results, each node has a score. You can
visualise these scores using a network representation with Cytoscape.

The following :numref:`cytoscapeRWR` is an example of display :

.. _cytoscapeRWR:
.. figure:: ../../pictures/RWR_pathwaysNet_useCase1.png
    :alt: useCase 1 RWR
    :align: center

    : Visualisation of network using Cytoscape [1]_

To visualise the RWR results using network representation, use the following steps :

1. **Import Network** from File : ``resultsNetwork_useCase1.sif``
2. **Import Table** from File : ``multiplex_1.tsv`` and ``multiplex_2.tsv``
3. **Import Table** from File : ``seeds.4Cytoscape``

    - Change column names to ``node`` and ``seed``

.. tip::

   How create the **seeds.4Cytoscape** file ?

   .. code-block:: bash

        awk -F"\t" 'NR==FNR{a[$1]; next} {if($2 in a){print $2"\tTrue"}else{print $2"\tFalse"}}' seeds.txt multiplex_1.tsv > seeds.4Cytoscape

4. **Import Table** from File : ``diseasesResults.txt``

    - Change column names to ``node``, ``pathways`` and ``score``

.. tip::

   How create the **diseasesResults.txt** file ?

   The ``higherScore`` is the highest score in ``multiplex_1.tsv`` file and the ``gmtFile`` is the gmt file of
   pathways of interest.

   .. code-block:: bash

        awk -F"\t" 'NR==FNR{a[$1]=$2;next} {if($3>=higherScore){$3=sprintf("%.6f", $3); print $2"\t"a[$2]"\t"$3}}' gmtFile multiplex_2.tsv > diseasesResults.txt

5. Create **two new columns** named ``label`` as string and ``keep`` as boolean
6. **Filter** : Select genes nodes

    - To ``label`` column, fill with ``=$name`` and apply to selected nodes
    - To ``keep`` column, fill with ``=$seed`` and apply to selected nodes
    - Sort by ``score`` (decrease) and select the 30th first genes that are not a seed (selected nodes from selected rows)
    - To ``keep`` column, fill with ``=True`` and apply to selected nodes

7. **Filter** : Select pathways nodes

    - Add pathway names into ``label`` column (``=$pathway``)
    - Add a condition score into ``keep`` column (``=$score>=0.0002083975629882177``)

8. **Filter** : Select nodes with ``keep = True``
9. **New Network** : From Selected Nodes, All Edges
10. Edit and Remove Duplicate Edges
11. **Style** :

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
          | True : CCCCCC
          | False : FFFFFF
        - DD3497
    *   - Label Front Size
        - 20
        - 50
    *   - Shape
        - Circle
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

12. Layout = yFiles Organic Layout

*To perform a RWR with data requested, see* :ref:`Use-case 1 <useCase1_RWR>` *or with your data see* :ref:`Use-case 2 <useCase2_RWR>`.

References
--------------------------------------------------

.. [1] Shannon, P., Markiel, A., Ozier, O., Baliga, N. S., Wang, J. T., Ramage, D., ... & Ideker, T. (2003). Cytoscape: a software environment for integrated models of biomolecular interaction networks. Genome research, 13(11), 2498-2504.
.. [2] Legeay, M., Doncheva, N. T., Morris, J. H., & Jensen, L. J. (2020). Visualize omics data on networks with Omics Visualizer, a Cytoscape App. F1000Research, 9.
.. [3] https://github.com/cytoscape/legend-creator
.. [4] Baptista, A., Gonzalez, A., & Baudot, A. (2022). Universal multilayer network exploration by random walk with restart. Communications Physics, 5(1), 1-9.