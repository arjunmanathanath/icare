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
import threading
import time

from scrapedstories.classifytext import classif
from scrapedstories.numberofwords import Numberofwords
from .models import ScrapeData

lock=threading.Lock()

def scraper(seedurl,steps):
    urls = seedurl #collect seed from db
    visited = seedurl #collect visited from db 
    counter = 0
    result_urls =[]
    
    while counter<steps:
        scrapeStep(urls,result_urls)
        
        urls= []
        for u in result_urls:
        	if u not in visited:
                        
        		urls.append(u)
        		visited.append(u)
        
        counter+=1
    #print visited


def scrapeStep(seed,result_urls):
    #br = scraperfunctions.Browser()
    del result_urls[:] 
    threadlist=[]
    for url in seed:
         t= Thread(target=openparse, args=(url,result_urls))
         t.setDaemon(True)
         threadlist.append(t)
    try:
        for g in threadlist:
            g.start()
    except:
        print 'oops!!thread_out'
    time.sleep(240)

    

def openparse(url,result_urls):
     br = scraperfunctions.Browser()
     try:
          htmlfile = br.open(url)
          article = scraperfunctions.articlescraper(htmlfile)

          #d[url] = article#replace with db population
          if Numberofwords(article[1]) >320:
              with lock:
                  data = ScrapeData()
                  data.slink = url
                  data.title = article[0]
                  data.snippet =article[1]
                  if len(article)==3:
                      data.simage = article[2]
                  data.category = classif(article[0])
                  data.save()
          for link in br.links():
              newurl = urlparse.urljoin(link.base_url,link.url)
              newurl = scraperfunctions.urlfilter(newurl)
              if newurl:
                 with lock:
                   result_urls.append(newurl)
     except:
          print 'Cannot open..'
          
    
#scraper(["https://www.parsehub.com/"],2)
