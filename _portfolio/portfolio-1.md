
---
title:  "Clouds"
collection: portfolio
---


### Project outline
Clouds represent the single largest uncertainty in projections of future climate change.
Their multi-scale nature means that even state-of-the-art numerical climate simulations cannot reliably project how their distribution, frequency, and properties will alter under high-CO~2~ conditions.
Observational data may therefore be key to understanding cloud behavior, but the information contained in decades and petabytes of multispectral cloud imagery from satellite instruments has received only limited use.
Recent advances in artificial intelligence (AI) now allow tapping this underutilized resource to improve understanding of cloud dynamics and feedbacks.
A core requirement for analysis of cloud images is *dimension reduction*: dividing a complex high-resolution spatial field into a more limited set of categories. 
Most attempts at automated cloud classification to date have involved supervised learning of a limited number of human-defined cloud categories, but spatial patterns of cloud textures vary widely, and our goal is to produce novel classifications that provide new insight.

Clouds project therefore proposes, **Rotation-Invariant Cloud Clustering (RICC)**,instead to leverage modern unsupervised deep learning methods to identify robust and meaningful clusters of cloud patterns, and to apply the resulting clustering method to 21 years of data from the Moderate Resolution Imaging Spectroradiometer (MODIS) instruments on NASA's Aqua and Terra satellites. The resulting dataset of cloud classifications will deliver in a compact form (10s of GB of class labels, with high spatial and temporal resolution) information currently accessible only as 100s of TB of multi-spectral images. 

RICC will enable the data-driven diagnosis of patterns of cloud organization, provide insight into their evolution on timescales of hours to decades, and contribute to a democratization of climate research by facilitating access to core data.

### Selected publications
- [Data-Driven Cloud Clustering via a Rotationally Invariant Autoencoder](https://ieeexplore.ieee.org/document/9497325)
- [Cloud Classification with Unsupervised Deep Learning](https://par.nsf.gov/servlets/purl/10195161)


### Contributor
[Takuya Kurihana](https://takglobus.github.io/takuyakurihana.github.io/)  
Email: `tkurihana at uchicago.edu`   


This project is supported in part by the AI for Science Program of the Center for Data and Computing at the University of Chicago, in part by the Center for Robust Decision-making on Climate and Energy Policy (RDCEP) through NSF under Grant SES-1463644, and in part by the U.S. Department of Energy, Office of Science, Advanced Scientific Computing Research under Contract DE-AC02-06CH11357. 
