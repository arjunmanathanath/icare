from django.contrib import admin
from . models import ScrapeData, SeedUrlDefiner
# Register your models here.
admin.site.register(ScrapeData)
admin.site.register(SeedUrlDefiner)
