import numpy as np
import pandas as pd
import nltk
from nltk.corpus import stopwords
import string
from nltk.stem.porter import PorterStemmer

def transfrom_text(text):
    # Lowering
    text = text.lower()
    # Tokenization
    text = nltk.word_tokenize(text)

    # removing special character
    tokens = []
    for i in text:
        if i.isalnum():
            tokens.append(i)

    # removing punctuations and stopwords
    y = []
    for t in tokens:
        if t not in stopwords.words('english') and t not in string.punctuation:
            y.append(t)
    tokens.clear()

    # stemming
    texts = []
    for i in y:
        ps = PorterStemmer()
        texts.append(ps.stem(i))
    y.clear()

    return " ".join(texts)