---
title: "Digital Twin: Environmental Remediation"
collection: "portfolio"
excerpt: "Can we use AI to emulate Amanzi-ATS simulations to deliver rapid and accurate results to practitioners and enable decision-making on future climate scenarios without a supercomputer?"
---

![clouds]({{ "/images/FDL2022.png" | absolute_url }})

### Project outline
Soil and groundwater contamination is a pervasive problem across all societies worldwide. Contaminated sites often require decades to remediate or to monitor natural attenuation. 
Climate change exacerbates the problem because extreme precipitation and/or shifts in precipitation/evapotranspiration regimes can remobilize contaminants and proliferate affected groundwater.

We leverage a physics-infused machine learning technique, **U-Net enhanced Fourier Neural Operator (U-FNO)**, to create time-dependent surrogate flow and transport models under different climate scenarios at the Department of Energy’s Savannah River Site F-Area as a testbed. We develop a combined loss function that includes both data-driven factors and physical boundary constraints at multiple spatiotemporal scales. Our U-FNOs can reliably predict the spatiotemporal variations of groundwater flow and contaminant transport properties from 1954 to 2100 with realistic climate projections. 
In parallel, we develop **a convolutional autoencoder combined with online clustering** to reduce the dimensionality of the vast historical and projected climate data by quantifying climatic region similarities across the United States. The ML-based unique climate clusters help return reliable future recharge rate projections immediately without querying large climate datasets. 
In all, this Multi-scale Digital Twin work can advance the field of environmental remediation under climate change.

FDL applies AI technologies to science to push the frontiers of research and develop new tools to help solve some of the biggest challenges that humanity faces.
The project is supported by one of FDL 2022 challenges.

### Selected publications
- Physics-informed surrogate modeling for supporting climate resilience at groundwater contamination sites *under submission in AGU 2022 Fall meeting
- Physics-informed surrogate modeling for supporting climate resilience at groundwater contamination sites *under reviewed in NeurIPS 2022

### Contribution
In part of FDL 2022 project, I have contributed to the development of convolutional autoencoder and analysis of climate patterns to provide realistic climate conditions to both groundwater simulation and surrogate model.


### Funding
This project is supported in part by Frontier Development Lab 2022, and funded by Department of Energy and Google Cloud Platform.
