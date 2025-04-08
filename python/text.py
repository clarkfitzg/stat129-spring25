from sklearn.feature_extraction.text import CountVectorizer

corpus = [
        "It's going to be raining tomorrow",
        "Rain, rain, go away",
        "It's rainy, so let's go to the library",
]

# Create the object representing the model
cv0 = CountVectorizer()

# Fit it to our data
cv0.fit(corpus)

# What does each column in the matrix (feature) represent?
cv0.get_feature_names_out()

# The actual matrix
m = cv0.transform(corpus)

# DANGER! Convert to dense.
m.todense()




# From 
# https://scikit-learn.org/stable/modules/feature_extraction.html
# Requires several downloads, going to slow things down during lecture.

# from nltk import word_tokenize          
# from nltk.stem import WordNetLemmatizer 
# class LemmaTokenizer:
#     def __init__(self):
#         self.wnl = WordNetLemmatizer()
#     def __call__(self, doc):
#         return [self.wnl.lemmatize(t) for t in word_tokenize(doc)]
# 
# cv1 = CountVectorizer(tokenizer=LemmaTokenizer())  
# cv1.fit(corpus)

# nltk- natural language toolkit
from nltk.stem.snowball import EnglishStemmer

# Following example at
# https://stackoverflow.com/a/36191362
stemmer = EnglishStemmer()
#stemmer = EnglishStemmer(ignore_stopwords = True)

analyzer = CountVectorizer().build_analyzer()

def stemmed_words(doc):
    return [stemmer.stem(w) for w in analyzer(doc)]

stemmed_words(corpus[0])

def stemmed_words1(doc):
	# Better to use builtin:
	# nltk.download('stopwords')
    stopwords = {"it", "to", "the"}
    docwords = [stemmer.stem(w) for w in analyzer(doc)]
    return [x for x in docwords if x not in stopwords]

cv1 = CountVectorizer(analyzer=stemmed_words1)
cv1.fit(corpus)

stemmed_words(corpus[0])
stemmed_words1(corpus[0])


cv1.get_feature_names_out()

# DANGER! Convert to dense.
m = cv1.transform(corpus).todense()

from sklearn.feature_extraction.text import TfidfTransformer

transformer = TfidfTransformer()

counts = cv1.transform(corpus)
tfidf = transformer.fit_transform(counts)
