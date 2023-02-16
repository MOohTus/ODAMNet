# README

The goal of this project is to develop computational approaches to analyse the links and overlaps between chemicals
and Rare Diseases.

The [ODAMNet documentation][ODAMNet documentation] is available in ReadTheDocs.

This project was created within the framework of the [EJRP-RD project][EJPRD].

## Installation 

### From PyPi

ODAMNet is available as python package. You can easily install it using `pip`.

```console
$ python3 -m pip install odamnet
```

### From Conda - *It's ongoing*

It is available in [bioconda][bioconda] too.

```console
$ conda install odamnet
```

### From Github

1. Clone the repository from GitHub

```console
$ git clone https://github.com/MOohTus/ODAMNet.git
```

2. Then, install it

```console
$ python3 -m pip install -e ODAMNet/
```

## Usage

Three different approaches are available: 

- Overlap analysis
- Active Modules Identification (AMI, using DOMINO)
- Random Walk with Restart (RWR, using multiXrank)

```console
$ odamnet [overlap|domino|multixrank|networkCreation] [ARGS]
```

## Examples

Three approaches are implemented to study relationships between Rare Diseases (from WikiPathways (WP)) and genes 
targeted by chemicals (extracted from CTD database).

### Overlap analysis

This method computes the overlap between target genes and Rare Disease pathways. It is looking for direct associations, 
i.e., target genes that are part of pathways.

```console
$ odamnet overlap --chemicalsFile FILENAME
```

### Active Module Identification (AMI)

Target genes are defined as "active genes" to search for Active Modules (AM) on a molecular network (e.g.
Protein-Protein Interaction network, PPI). Then, an overlap analysis is performed between AM (containing target genes + linked genes)
and Rare Disease pathways.

```console
$ odamnet domino --chemicalsFile FILENAME --networkFile FILENAME
```

### Random Walk with Restart (RWR)

#### Network and bipartite creation

To perform a Random Walk with Restart through molecular multilayer and diseases network, you need to create a disease network
and link it to the multilayer (i.e. with the bipartite). This network will not have connection between diseases (i.e. disconnected network).
Diseases will be only connected with genes (in the multilayer) that are involved in disease pathways.

```console
$ odamnet networkCreation --networksPath PATH --bipartitePath PATH
```

#### multiXrank

The third approach mesures the proximity of every nodes (g.e. genes, diseases) to the target genes within a multilayer network.
The walk starts from target genes and diffuses through the multilayer composed of different molecular interactions to the disease.

```console
$ odamnet multixrank --chemicalsFile FILENAME --configPath PATH --networksPath PATH --seedsFile FILENAME --sifFileName FILENAME
```

[ODAMNet documentation]: https://odamnet.readthedocs.io/
[bioconda]: https://bioconda.github.io/index.html
[EJPRD]: https://www.ejprarediseases.org/
