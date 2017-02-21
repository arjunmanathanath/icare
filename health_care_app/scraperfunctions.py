import urllib
import re
import time
from threading import Thread
import mechanize
import readability
from bs4 import BeautifulSoup
from readability.readability import Document
import urlparse
import scraperfunctions

def Browser():
    browser = mechanize.Browser()
    browser.set_handle_robots(False)
    browser.addheaders = [('User_agent','Chromium')]
    browser.set_handle_refresh(True)
    return browser


def articlescraper(htmlfile):
    #html = br.open(url).read() #if html is a file
    html = htmlfile.read()
    readable_article = Document(html).summary()
    readable_title = Document(html).short_title()

    soup = BeautifulSoup(readable_article)

    final_article = soup.text
    #print final_article
    links = soup.find('img', src=True)

    #print readable_title
    #print final_article 
    article=[]
    links = soup.find('img', src=True)
    article.append(readable_title)
    article.append(final_article)
    if links:
        imageurl = links['src']
        article.append(imageurl)
    return article


def urlfilter(newurl):
    if '#' in newurl:
       list = newurl.split('#')
       newurl = list[0]
    if '?' in newurl:
       list = newurl.split('?')
       newurl = list[0]
    return newurl


'''def Openurl(url,browser):
   try:
      html = browser.open(url)
      return html
   except:
      print 'error'''
   
