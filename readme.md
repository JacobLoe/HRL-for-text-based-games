# HRL for text based games
How to create a conda environment for hierarchical reinforcement learning.

(Tested with Anaconda ver 4.9.2)


Creae and activate conda environement:
```
conda create -n hrltb pytorch=1.7.1 matplotlib==2.2.3 networkx==2.2
conda activate hrltb
```

Inside conda install requirements with:
```
pip install -r requirements.txt
```

For running jupyter notebooks:
```
conda install -c anaconda ipykernel

python -m ipykernel install --user --name=hrltb
```
