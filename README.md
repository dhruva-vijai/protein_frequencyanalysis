# Frequency Analysis of Protein Composition in Proteomes
## Problem Statement

Use a Hierarchical Clustering algorithm to analyse the amino acid composition of the various proteins belonging to a given proteome and self-categorise into clusters based on composition.

## Background Information

The amino acid sequence of a given protein is an important factor to consider in bioinformatics, as it provides a rough ouline of the evolutionary history, biological activity and its' 3d structure. Thus, we expect; within a given proteome, there will exist multiple 'clusters' of proteins that share similar amino acid compositions; and thus can be studied together to elucidate certain general trends in the protein properties of the proteome. 


## Specifics

This project is a hard-coded hierarchical clustering algorithm completely written in Python. The point of this project is to conduct a frequency analysis of the amino acid sequence of a given protein trained on a proteome downloaded from UniProt based on a hierarchical clustering-based machine learning algorithm.

Hierarchical clustering is a relatively simple algorithm to execute and does not require much training data, but runs into problems regarding precision; thus the next goal in this project is to develop a neural-network based approach to classifications of the amino acid frequency vectors.

__1) Reading Proteome__

__2) Machine Learning Model__


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

## Improvements

## File Structure

## Assets





This project is a hard-coded hierarchical clustering algorithm completely written in Python. The point of this project is to conduct a frequency analysis of the amino acid sequence of a given protein trained on a proteome downloaded from UniProt based on a hierarchical clustering-based machine learning algorithm.

The frequency distribution of an amino acid sequence has implications that characterise the biological function, evolutionary history, and 3D structure of the acid.

Hierarchical clustering is a relatively simple algorithm to execute and does not require much training data, but runs into problems regarding precision; thus the next goal in this project is to develop a neural-network based approach to classifications of the amino acid frequency vectors.

All credits for the clustering algorithm goes to www.pythonprogramming.net who provided a wonderful course and the source code for the algorithm. Protein sequences are obtained from the UniProt Database.


