from nltk.tokenize import sent_tokenize
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyzesentiment(str):
    analyzer = SentimentIntensityAnalyzer()
    vs = analyzer.polarity_scores(str)
    if vs['neu']>vs['neg'] and vs['neu']>vs['pos']:
      return 'negative'
    else:
      if vs['neg']<vs['pos']:
        return 'positive'
      else:
        return 'negative'