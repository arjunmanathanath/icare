from __future__ import unicode_literals

from django.db import models

# Create your models here.
from scrapedstories.classifytext import classif


class ScrapeData(models.Model):
    title = models.CharField(max_length=320,blank=True,null=True)
    snippet = models.TextField(blank=True,null=True)
    slink = models.URLField(max_length=500,blank=True,null=True)
    simage = models.URLField(max_length=500,blank=True,null=True)
    category = models.CharField(max_length=40,blank=True,null=True)
    #date= models.DateTimeField('date published',blank=True,null=True)

    def __str__(self):
        return self.title

    #def save(self, *args, **kwargs):
        #super(ScrapeData, self).save(*args, **kwargs)  # Call the "real" save() method.
        #self.category = classif(self.snippet)
        #super(ScrapeData, self).save(*args, **kwargs)


class SeedUrlDefiner(models.Model):
    seed_url = models.URLField(max_length=20,blank=True,null=True)

