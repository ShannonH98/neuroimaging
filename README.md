# Neuroimaging — Visualization & Stats

## Overview
This repository contains a small Python pipeline for **loading, visualizing, and comparing 3D brain images** (NIfTI format).  
It uses **Nilearn** for neuroimaging utilities and **Matplotlib** for interactive visualization.  

Key features:

- Brain visualization  
- Interactive slice scrolling  
- Voxel-wise brain comparisons  
- Handling brains with different shapes (resampling)

This repo is designed as a learning project for Python-based neuroimaging workflows.

---

## Folder Structure
neuroimaging/
├─ data/ # Optional: place your NIfTI (.nii) files here

├─ src/

│ ├─ visualization.py # Functions for plotting & slice browsing

│ ├─ processing.py # Functions for comparing brains

└─ examples/

└─ pipeline.py # Example script showing full workflow


## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/neuroimaging-repo2.git
cd neuroimaging-repo2

