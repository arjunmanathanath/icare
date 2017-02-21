from nltk.corpus import stopwords
from nltk_trainer.classification.featx import bag_of_words
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
import collections
import pickle
#collects words from (bag_of_non_stopwords) append bigrams
def bag_of_bigrams_words(words, score_fn=BigramAssocMeasures.chi_sq,n=200):
    bigram_finder = BigramCollocationFinder.from_words(words)
    bigrams = bigram_finder.nbest(score_fn, n)
    return bag_of_words(words + bigrams)

#creates 'words': list of non common words in input 'words'
def bag_of_non_stopwords(words, stopfile='english'):
   badwords = stopwords.words(stopfile)
   #non_stopwords = [(set(words) - set(badwords))]
   for word in words:
     if word in badwords:
        words.remove(word)
   return bag_of_bigrams_words(words)

def classif(str):
    classifier_f = open('health.pickle','rb')
    nb_classifier = pickle.load(classifier_f)
    classifier_f.close()
    feature = bag_of_non_stopwords(str.split())
    return nb_classifier.classify(feature)
#/home/arjun/nltk_data
#test me
#print classif("cance is a killer. beware of cancer")


#negfeat = bag_of_non_stopwords(['cancer', 'was', 'was', 'cancer'])
#print nb_classifier.classify(negfeat)
#'neg'
#posfeat = bag_of_non_stopwords(['kate', 'cancer', 'is', 'diabet'])
#print nb_classifier.classify(posfeat)
#'pos'

'''
#from nltk.corpus import movie_reviews
#from featx import label_feats_from_corpus, split_label_feats
print reader.categories()
#['neg', 'pos']
lfeats = label_feats_from_corpus(reader)#corpus here!!!
print lfeats.keys()
#dict_keys(['neg', 'pos'])
train_feats, test_feats = split_label_feats(lfeats, split=0.75)
print len(train_feats)
#1500
print len(test_feats)
#500

#from nltk.classify import NaiveBayesClassifier
#nb_classifier = NaiveBayesClassifier.train(train_feats)
#nb_classifier.labels()
#['neg', 'pos']
'''






