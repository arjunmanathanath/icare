from nltk.corpus import stopwords
from nltk_trainer.classification.featx import bag_of_words
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
import collections
import pickle

from nltk.corpus.reader import CategorizedPlaintextCorpusReader
reader = CategorizedPlaintextCorpusReader('/home/arjun/nltk_data/health/diabetes', r'health.*?[0-9]+.txt', cat_pattern=r'health(.*?)[0-9]+.txt')
#print reader.categories()

#takes a corpus .. creates labelled feature sets
def label_feats_from_corpus(corp, feature_detector=bag_of_words):
    label_feats = collections.defaultdict(list)
    for label in corp.categories():
      for fileid in corp.fileids(categories=[label]):
        feats = feature_detector(corp.words(fileids=[fileid]))
        label_feats[label].append(feats)
    return label_feats

#creates test and train features
def split_label_feats(lfeats, split=0.75):
  train_feats = []
  test_feats = []
  for label, feats in lfeats.items():
    cutoff = int(len(feats) * split)
    train_feats.extend([(feat, label) for feat in feats[:cutoff]])
    test_feats.extend([(feat, label) for feat in feats[cutoff:]])
  return train_feats, test_feats

lfeats = label_feats_from_corpus(reader)
train_feats, test_feats = split_label_feats(lfeats, split=0.75)

from nltk.classify import NaiveBayesClassifier
nb_classifier = NaiveBayesClassifier.train(train_feats)
print nb_classifier.labels()

save_classifier = open("health.pickle","wb")
pickle.dump(nb_classifier ,save_classifier)
save_classifier.close()
