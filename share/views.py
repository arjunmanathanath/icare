from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q

from share.forms import ShareForm
from .models import Experience, Templog
from django.utils import timezone
from sentianalyzer import analyzesentiment
# Create your views here.
@login_required
def share(request):
    if request.method=="POST":
      form = ShareForm(request.POST)
      if form.is_valid():
         a=Experience()
         a.text=request.POST['text']
         a.sentiment = analyzesentiment(request.POST['text'])
         a.time = timezone.now()
         a.user=request.user
         a.save()
         b=Templog()
         b.experience=a

         b.doctor = request.POST['doctor']

         b.institution = request.POST['institution']

         b.place = request.POST['place']

         b.regno=form.cleaned_data['regno']
         b.save()

         #code for furthur retrieval of similar
         '''exp=Experience.objects.exclude(user = request.user)
         for ex in exp:
             log=Templog.objects.get(experience = ex).'''
         log = Templog.objects.exclude(experience__user=request.user)
         flog = log.filter(Q(doctor = request.POST['doctor'])|Q(institution = request.POST['institution'])|Q(place = request.POST['place'])|Q(regno = form.cleaned_data['regno']))

         return render(request, 'share/share.html', {'form': form,'logs':flog})

    else:
         form = ShareForm()
         return render(request,'share/share.html',{'form':form})



    '''Poll.objects.get(
    Q(question__startswith='Who'),
    Q(pub_date=date(2005, 5, 2)) | Q(pub_date=date(2005, 5, 6))
)'''
def upvote():
    pass

def downvote():
    pass