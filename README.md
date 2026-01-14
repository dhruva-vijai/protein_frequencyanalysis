# Frequency Analysis of Protein Composition in Proteomes
## Problem Statement

Use a Hierarchical Clustering algorithm to analyse the amino acid composition of the various proteins belonging to a given proteome and self-categorise into clusters based on composition.

## Background Information

The amino acid sequence of a given protein is an important factor to consider in bioinformatics, as it provides a rough ouline of the evolutionary history, biological activity and its' 3d structure. Thus, we expect; within a given proteome, there will exist multiple 'clusters' of proteins that share similar amino acid compositions; and thus can be studied together to elucidate certain general trends in the protein properties of the proteome. 


## Specifics

This project is a hard-coded hierarchical clustering algorithm completely written in Python. The point of this project is to conduct a frequency analysis of the amino acid sequence of a given protein trained on a proteome downloaded from UniProt based on a hierarchical clustering-based machine learning algorithm.

Hierarchical clustering is a relatively simple algorithm to execute and does not require much training data, but runs into problems regarding precision; thus the next goal in this project is to develop a neural-network based approach to classifications of the amino acid frequency vectors.

__1) Reading Proteome__

The amino acid sequence of proteins in a given protein was extracted by parsing through **Fasta** files downloaded from the  UniProt database using BioPython in readfasta.py

__2) Machine Learning Model__

We use a hierarchical clustering model implementing a mean-shift algorithm to analyse the given data. Hierarchical clustering is a relatively old machine learning algorithm that takes a given set of points in an arbitrary space and classifies the points into clusters of points based on their similarity to one another. This algorithm is a form of unsupervised machine learning as the computer itself decides the number and location of clusters. 

The "points" in this vector space that we train the model on is a 20-dimensional vector where each component of the vector is the percentage composition of a given amino acid in the protein sequence. 

All credits for the clustering algorithm goes to www.pythonprogramming.net who provided a wonderful course and the source code for the algorithm. Protein sequences are obtained from the UniProt Database.


## Necessary Libraries

1) BioPython

2) NumPy

3) MatPlotLib

## Basic Setup

cd projects

git clone

conda activate venv

conda install -c forge biopython matplotlib numpy -y

## Problems Faced

1) Relatively simple algorithm lacks learning capacities and the ability to learn more complex, non-linear relationships.

2) The proteomes used were relatively small/simple proteomes which don't have diversity  in available proteins.


## Improvements

1) Improve training features instead of simply using composition vectors.

2) Improve code efficiency by writing the code in C++.

3) Use proteomes that have a larger, more diverse range of proteins that show more clusters to better understand the model efficiency.


## File Structure

1) clustering.py - This file executes the clustering algorithm and completes the classification algorithm.

2) readfasta.py - This code parses the FASTA file and obtains a dictionary containing sequence values and composition vectors.

3) FASTA file - A fasta file contains records that describe the protein structure of different proteins that belong to a given proteome. We parse this file to obtain the records of different structures.






