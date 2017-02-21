from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from scrapedstories.models import ScrapeData
from scrapedstories.myscrapercrawler import scraper
from userauth.models import Health_status

def scraperpopulate(request):
    scraper(["https://pypi.python.org/pypi/newspaper"], 2)
    return HttpResponse("<p>time to checkout the db!!!!</p>")


def mystory(request):

    disease= Health_status.objects.get(user=request.user).disease
    if disease == 'cancer':
       data = ScrapeData.objects.filter(category='cancer').order_by('?')[:3]
       context = {'stories': data,}
       return render(request,'scrapedstories/stories.html',context)
    else:
        data = ScrapeData.objects.filter(category='diabetes').order_by('?')[:3]
        context = {'stories': data, }
        return render(request, 'scrapedstories/stories.html', context)

    #return HttpResponse("<p>arjun hai!</p>")

