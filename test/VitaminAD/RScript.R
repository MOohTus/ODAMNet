## MT - 20220621

## Functions
## UPSETR : Create matrix from list
## INPUT :
##    - LIST - list2Compare : named list with the genes to compare
## OUTPUT :
##    - matrix : return matrix
createMatrix4Upset <- function(list2Compare){
  tmp <- stack(list2Compare)
  tmp <- cbind(tmp, val = 1)
  matrix <- as.data.frame(reshape2::acast(
    data = tmp, formula = values ~ ind, value.var = "val",
    fill = 0))
  return(matrix)
}

## Libraries
library("UpSetR")

## Global variables
workDirectory <- "/home/morgane/Documents/05_EJPR_RD/WF_Environment/EnvironmentProject/test/VitaminAD/"
overlapFile <- "Overlap_analysis.txt"

## Work directory
setwd(dir = workDirectory)

## Read overlap results (from overlap and domino analysis)
overlapData <- read.table(file = overlapFile, head = TRUE, sep = "\t")
head(overlapData)

## Create list of results
VitaminA_Overlap <- overlapData[c(overlapData$Molecule == "D014801" & overlapData$Analyse == "Overlap"), "WPID"]
VitaminA_DOMINO <- overlapData[c(overlapData$Molecule == "D014801" & overlapData$Analyse == "DOMINO"), "WPID"]
VitaminD_Overlap <- overlapData[c(overlapData$Molecule == "D014807" & overlapData$Analyse == "Overlap"), "WPID"]
VitaminD_DOMINO <- overlapData[c(overlapData$Molecule == "D014807" & overlapData$Analyse == "DOMINO"), "WPID"]

data_list <- list("VitaminA_Overlap" = VitaminA_Overlap, "VitaminA_DOMINO" = VitaminA_DOMINO,
                  "VitaminD_Overlap" = VitaminD_Overlap, "VitaminD_DOMINO" = VitaminD_DOMINO)
data_matrix <- createMatrix4Upset(list2Compare = data_list)

## Create upsetR plot 
upset(data = data_matrix, sets = names(data_matrix))
png(filename = "UpsetR_VitaminA_OverlapDOMINO.png", res = 300, width = 1000, height = 800)
upset(data = data_matrix, intersections = list("VitaminA_Overlap", "VitaminA_DOMINO", c("VitaminA_Overlap", "VitaminA_DOMINO")))
dev.off()
png(filename = "UpsetR_VitaminD_OverlapDOMINO.png", res = 300, width = 1000, height = 800)
upset(data = data_matrix, intersections = list("VitaminD_Overlap", "VitaminD_DOMINO", c("VitaminD_Overlap", "VitaminD_DOMINO")))
dev.off()

upset(data = data_matrix, sets = c("VitaminD_Overlap", "VitaminD_DOMINO"))

## Visualization for active module networks
library("igraph")
networkFile <- "/home/morgane/Documents/06_Data/NETWORKS/01_InitialNetworks/PPI_2016-11-23.gr"

setwd(dir = "/home/morgane/Documents/05_EJPR_RD/WF_Environment/EnvironmentProject/test/VitaminAD/OutputDOMINOResults/")

## VITAMIN A
AMFile <- "/home/morgane/Documents/05_EJPR_RD/WF_Environment/EnvironmentProject/test/VitaminAD/OutputDOMINOResults/DOMINO_D014801_activeModules.txt"
targetsFile <- "/home/morgane/Documents/05_EJPR_RD/WF_Environment/EnvironmentProject/test/VitaminAD/OutputDOMINOResults/DOMINO_inputGeneList_D014801.txt"
networkOutputFileName <- "DOMINO_D014801_activeModules.SIF"
targetsOutputFileName <- "DOMINO_D014801_activeModules.table"
## VITAMIN D
AMFile <- "/home/morgane/Documents/05_EJPR_RD/WF_Environment/EnvironmentProject/test/VitaminAD/OutputDOMINOResults/DOMINO_D014807_activeModules.txt"
targetsFile <- "/home/morgane/Documents/05_EJPR_RD/WF_Environment/EnvironmentProject/test/VitaminAD/OutputDOMINOResults/DOMINO_inputGeneList_D014807.txt"
networkOutputFileName <- "DOMINO_D014807_activeModules.SIF"
targetsOutputFileName <- "DOMINO_D014807_activeModules.table"

## Read network
PPI_file <- "/home/morgane/Documents/06_Data/NETWORKS/01_InitialNetworks/PPI_2016-11-23.gr"
PPI_table <- read.table(file = PPI_file, sep = " ")
PPI_network <- igraph::graph.data.frame(d = PPI_table, directed = FALSE)
PPI_network <- igraph::simplify(graph = PPI_network, remove.multiple = TRUE, remove.loops = TRUE)

## Extract sub network for each active modules
AM <- read.table(file = AMFile, head = FALSE, sep = "\t")
AM_networks <- do.call(rbind, lapply(X = unique(AM$V2), FUN = function(AM_nb, PPI_network){
  AM_selected <- AM[AM$V2 == AM_nb,]$V1
  net_AM_selected <- induced.subgraph(graph = PPI_network, vids = which(names(V(PPI_network)) %in% AM_selected))
  results_dt <- data.frame(get.edgelist(net_AM_selected), 
                           "Cluster" = AM_nb, 
                           "EdgesNumber" = length(E(net_AM_selected)),
                           "NodesNumber" = length(V(net_AM_selected)),
                           "DegreeMax" = max(degree(graph = net_AM_selected)),
                           "DegreeMean" = mean(degree(graph = net_AM_selected)),
                           "diameter" = diameter(graph = net_AM_selected))
  names(results_dt) <- c("Node1", "Node2", "Cluster", "EdgesNumber", "NodesNumber", "DegreeMax", "DegreeMean", "diameter")
  return(results_dt)
}, PPI_network))

## Notice those gnes that come from target
targets <- read.table(file = targetsFile, head = FALSE)
nodesTargets <- data.frame("nodeName" = unique(c(AM_networks$Node1, AM_networks$Node2)))
nodesTargets$Target <- nodesTargets$nodeName %in% targets$V1

## Write results
write.table(x = AM_networks, file = networkOutputFileName, quote = FALSE, sep = ";", row.names = FALSE, col.names = TRUE)
write.table(x = nodesTargets, file = targetsOutputFileName, quote = FALSE, sep = ";", row.names = FALSE, col.names = TRUE)


