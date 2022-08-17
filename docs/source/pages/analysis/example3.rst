***************************************************
Example 3 : analysis from custom files
***************************************************

Overlap analysis
------------------

.. code-block:: bash

   python3 main.py overlap  --geneList examples/InputData/InputFromPaper/VitA-Balmer2002-Genes.txt \
                            --GMT examples/InputData/InputFromPaper/PathwaysOfInterest.gmt \
                            --backgroundFile examples/InputData/InputFromPaper/PathwaysOfInterestBackground.txt \
                            --outputPath examples/OutputResults_example3/

Several files are generated :

Active Module Identification : DOMINO
----------------------------------------

.. code-block:: bash

   python3 main.py domino   --geneList examples/InputData/InputFromPaper/VitA-Balmer2002-Genes.txt \
                            --GMT examples/InputData/InputFromPaper/PathwaysOfInterest.gmt \
                            --backgroundFile examples/InputData/InputFromPaper/PathwaysOfInterestBackground.txt \
                            --networkFile examples/InputData/PPI_network_2016.sif \
                            --outputPath examples/OutputResults_example3/

Several files are generated :

Random Walk with Restart : multiXrank
---------------------------------------

.. code-block:: bash

   python3 main.py networkCreation  --networksPath examples/InputData/multiplex/2/ \
                                    --networksName pathwaysOfInterestNetwork_fromPaper.sif \
                                    --bipartitePath examples/InputData/bipartite/ \
                                    --bipartiteName Bipartite_pathOfInterest_geneSymbols_fromPaper.tsv \
                                    --GMT examples/InputData/InputFromPaper/PathwaysOfInterest.gmt \
                                    --outputPath examples/OutputResults_example3/

.. code-block:: bash

   python3 main.py multixrank   --geneList examples/InputData/InputFromPaper/VitA-Balmer2002-Genes.txt \
                                --configPath examples/InputData/config_minimal_example3.yml \
                                --networksPath examples/InputData/ \
                                --seedsFile examples/InputData/seeds.txt \
                                --sifFileName example3_resultsNetwork.sif \
                                --top 10 \
                                --outputPath examples/OutputResults_example3/

Pathway rare diseases identified
----------------------------------------

Using orsum to compare

.. code-block:: bash







