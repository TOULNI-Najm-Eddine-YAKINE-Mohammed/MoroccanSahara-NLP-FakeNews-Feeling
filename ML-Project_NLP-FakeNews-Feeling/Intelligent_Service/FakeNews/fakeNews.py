import sys
from joblib import dump, load
from sklearn.svm import SVC
from Scraping import scraping
from NLP import nlp
import pandas as pd
from sklearn import preprocessing
rootPath = sys.path[0]

def dataPreparation():
    scraping.scraping()
    trueData = open(rootPath+"/Scraping/data/trueData.txt", "r", encoding="utf8")
    trueTxt = trueData.read()
    fakeData = open(rootPath+"/Scraping/data/fakeData.txt", "r", encoding="utf8")
    fakeTxt = fakeData.read()
    data = []
    for s in nlp.tokenizationSentence(trueTxt):
        txt = nlp.lemmatization(nlp.cleanText(s))
        if(len(txt)>=20):
            data.append([txt, 'true'])
    for s in nlp.tokenizationSentence(fakeTxt):
        txt = nlp.lemmatization(nlp.cleanText(s))
        if (len(txt) >= 20):
            data.append([txt, 'false'])
    dataCsv = pd.DataFrame(data, columns=['news', 'class'])
    dataCsv.drop_duplicates(subset=None, inplace=True)
    dataCsv = dataCsv.sample(frac=1)
    dataCsv.to_csv(rootPath+'/FakeNews/data.csv', index=False)

def trainingData():
    df = pd.read_csv(rootPath+'/FakeNews/data.csv')
    X = df['news']
    y = df['class']
    le = preprocessing.LabelEncoder()  # creating labelEncoder
    y = le.fit_transform(y)  # Converting string labels into numbers.
    nlp.fit_wordToVector(X)
    nlp.fit_bagOfWords(X)
    X = nlp.bagOfWords(X)
    nlp.fit_tfidf(X)
    X = nlp.tfidf(X)
    return X, y

def testData(text):
    testData = []
    for s in nlp.tokenizationSentence(text):
        txt = nlp.lemmatization(nlp.cleanText(text))
        testData.append(txt)
    testData = nlp.tfidf(nlp.bagOfWords(testData))
    return testData

def trainModel():
    model = SVC(probability=True)
    X,y = trainingData()
    model.fit(X, y) #fit the model
    dump(model, rootPath+'/FakeNews/SVC.model')

def detectFakeNews(text):
    model = load(rootPath+'/FakeNews/SVC.model')
    test = testData(text)
    pProb = model.predict_proba(test) #make a probabilistic prediction
    pClass = model.predict(test) #make a classification prediction
    return pProb,pClass