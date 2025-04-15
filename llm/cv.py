# /opt/anaconda/bin/ipython

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer


d = pd.read_csv("/stat129/llm-summary.csv")


# Taking a subset so that we don't 
# do the whole assignment in class
n = 1000
corpus = d["summary"][:n]

cv = CountVectorizer()
X = cv.fit_transform(corpus)

words = cv.get_feature_names_out()

# Predict!
# len means "length", the number of elements
len(words)

# Predict!
X.shape

wordcounts = X.sum(axis = 0)
# drop the 2 dimensional structure
wordcounts = np.ravel(wordcounts)

rank = np.argsort(wordcounts)

# Sorted by number of times they appear
words_popular = words[rank]

