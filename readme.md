# HRL for text based games
How to create a conda environment for hierarchical reinforcement learning.

(Tested with Anaconda ver 4.9.2)

Create and activate conda environment:
```
conda create -f environment.yml
conda activate hrl-tb
```

For using jupyter notebooks run this in the conda environment:
```
python -m ipykernel install --user --name=hrl-tb
```