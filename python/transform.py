from sklearn.feature_extraction.text import CountVectorizer
import numpy as np


corpus = [
        "What does an LLM do?",
        "An LLM will do what you tell it to do",
        "Students, do not trust everything an LLM will do.",
]

cv = CountVectorizer()
cv.fit(corpus)
