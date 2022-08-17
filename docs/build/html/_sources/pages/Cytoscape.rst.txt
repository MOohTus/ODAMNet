***************************************************
Visualization using Cytoscape
***************************************************

DOMINO visualisation using Cytoscape :

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