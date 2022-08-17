***************************************************
Visualisation using Cytoscape
***************************************************

Active modules network visualisation (DOMINO)
-----------------------------------------------

1. Import Network from File : ``DOMINO_D014801_activeModulesNetwork.txt``
2. Import Table from File : ``DOMINO_D014801_activeModules.txt``
3. Omics Visualizer table from File : ``DOMINO_D014801_overlapAMresults4Cytoscape.txt``
4. Manage table connections : link network and the previous table

    - Network : sharedname
    - Table : geneSymbol

5. Donut Chart Visualization : Add overlap results using donuts (Use TermID)
6. Style :

    - Border Width = 5.0
    - Fill Color = ActiveGenes True #CCCCCC False #FFFFFF
    - Label Font = 20
    - Shape = Circle
    - Lock node width and height
    - Size = 50

7. Filter : Select nodes with overlapSignificant = True
8. New Network : From Selected Nodes, All Edges
9. Add legends using Omics Visualizer and Legend Creator


Network visualisation (multiXrank)
-----------------------------------------

1. Import Network from File : ``example1_resultsNetwork.sif``
2. Import Table from File : ``multiplex_1.tsv`` and ``multiplex_2.tsv``
3. Import Table from File : ``seeds.4Cytoscape``

    - Change column names to ``node`` and ``seed``

.. tip::

   How create the **seeds.4Cytoscape** file ?

   .. code-block:: bash

        awk -F"\t" 'NR==FNR{a[$1]; next} {if($2 in a){print $2"\tTrue"}else{print $2"\tFalse"}}' seeds.txt multiplex_1.tsv > seeds.4Cytoscape

4. Import Table from File : ``diseasesResults.txt``

    - Change column names to ``node``, ``pathways`` and ``score``

.. tip::

   How create the **diseasesResults.txt** file ?

   The ``higherScore`` is the highest score in ``multiplex_1.tsv`` file and the ``gmtFile`` is the gmt file of
   pathways of interest.

   .. code-block:: bash

        awk -F"\t" 'NR==FNR{a[$1]=$2;next} {if($3>=higherScore){$3=sprintf("%.6f", $3); print $2"\t"a[$2]"\t"$3}}' gmtFile multiplex_2.tsv > diseasesResults.txt

5. Create two new columns named ``label`` and ``keep``
6. Filter : Select genes nodes

    - To ``label`` column, fill with ``=$name`` and apply to selected nodes
    - To ``keep`` column, fill with ``=$seed`` and apply to selected nodes
    - Sort by ``score`` (decrease) and select the 30th first genes that are not a seed (selected nodes from selected rows)
    - To ``keep`` column, fill with ``=True`` and apply to selected nodes

7. Filter : Select pathways nodes

    - Add pathway names into ``label`` column (``=$pathway``)
    - Add a condition score into ``keep`` column (``=$score>=0.00020841510533737325``)

8. Filter : Select nodes with ``keep = True``
9. New Network : From Selected Nodes, All Edges
10. Edit and Remove Duplicate Edges
11. Style for all nodes :

    - Border Width = 5.0
    - Fill Color = seed True #CCCCCC False #FFFFFF
    - Label Font Size = 20
    - Shape = Circle
    - Lock node width and height
    - Size = 50
    - Label = label

12. Style for pathway nodes:

    - Shape = Triangle
    - Size = 100
    - Label Font Size = 50
    - Color = #DD3497

13. Layout = yFiles Organic Layout

