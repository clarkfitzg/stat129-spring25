#!/opt/anaconda/bin/ipython
import numpy as np
from sklearn.datasets import make_blobs

centers = np.array([[0, 0], [0, 2], [2, 0]])

X, y = make_blobs(n_samples=5000, centers=centers)
