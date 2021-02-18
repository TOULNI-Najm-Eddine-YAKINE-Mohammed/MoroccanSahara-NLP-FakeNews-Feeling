import warnings
warnings.filterwarnings(action='ignore')
import sys
import nltk
import gensim
import stopwords as stopwords
from nltk import sent_tokenize, word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from gensim.models import Word2Vec
from joblib import dump, load
rootPath = sys.path[0]

# Tokenization
def tokenizationSentence(text):
    return sent_tokenize(text)
def tokenizationWord(text):
    return word_tokenize(text)

# Words Frequency
def wordsFrequency(text, nbr):
    words = tokenizationWord(text)
    fdist = FreqDist(words)
    return fdist.most_common(nbr)

# Remove Punctuation
def removePunctuation(text):
    words_no_punc = []
    words = tokenizationWord(text)
    for w in words:
        if w.isalpha():
            words_no_punc.append(w.lower())
    txt = ''
    for w in words_no_punc:
        txt += w+' '
    return txt

# Remove Stop Words
def cleanText(text):
    stopWords = stopwords.words("english")
    clean_words = []
    words_no_punc = tokenizationWord(removePunctuation(text))
    for w in words_no_punc:
        if w not in stopWords:
            clean_words.append(w.lower())
    txt = ''
    for w in clean_words:
        txt += w + ' '
    return txt

# Stemming
def stemming(text):
    stem = []
    porter = PorterStemmer()
    for w in tokenizationWord(text):
        stem.append(porter.stem(w))
    txt = ''
    for w in stem:
        txt += w + ' '
    return txt

# Lemmatizing
def lemmatization(text):
    lem = []
    lemmatizer = WordNetLemmatizer()
    for w in tokenizationWord(text):
        lem.append(lemmatizer.lemmatize(w))
    txt = ''
    for w in lem:
        txt += w + ' '
    return txt

# PoS Tagging
def posTagging(text):
    words = tokenizationWord(text)
    tag = nltk.pos_tag(words)
    return tag

# Bag Of Words
def fit_bagOfWords(sentences):
    cv = CountVectorizer()
    cv.fit_transform(sentences)
    dump(cv, rootPath+'/NLP/models/bagOfWords.model')
def bagOfWords(sentences):
    model = load(rootPath+'/NLP/models/bagOfWords.model')
    return model.transform(sentences)

# TF-IDF
def fit_tfidf(freq_term_matrix):
    tfidf = TfidfTransformer(norm="l2")
    tfidf.fit(freq_term_matrix)
    tfidf.fit_transform(freq_term_matrix)
    dump(tfidf, rootPath+'/NLP/models/tfidf.model')
def tfidf(sentences):
    model = load(rootPath+'/NLP/models/tfidf.model')
    return model.transform(sentences)

# Word2Vector
def fit_wordToVector(sentences):
    data = []
    for s in sentences:
        temp = []
        for w in tokenizationWord(s):
            temp.append(w)
        data.append(temp)
    model = gensim.models.Word2Vec(data)
    model.train(data, total_examples=model.corpus_count, epochs=30)
    dump(model, rootPath + '/NLP/models/word2vec.model')
def w2vSimilarity(word1, word2):
    model = load(rootPath+'/NLP/models/word2vec.model')
    return model.similarity(word1, word2)