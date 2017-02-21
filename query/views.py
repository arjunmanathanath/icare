from django.core.urlresolvers import reverse

from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from query.forms import PostQuery, PostSolutions
from .models import Query, Solutions, Upvote,Downvote
from userauth.models import User
from userauth.models import Health_status
from django.utils import timezone
from django.http import HttpResponse
from scrapedstories import classifytext
# Create your views here.

@login_required
def postquery(request):
    if request.method == 'POST':
        form = PostQuery(request.POST)
        if form.is_valid():
            qi=Query()
            qi.query_text = form.cleaned_data['query_text']
            qi.user_posted = request.user
            qi.written = timezone.now()
            qi.disease = classifytext.classif(form.cleaned_data['query_text'])
            qi.save()
            queries = Query.objects.exclude(user_posted = request.user).filter(disease=qi.disease).order_by('?')[:5]
            myqueries = Query.objects.filter(user_posted=request.user)
            return render(request, 'query/qaa.html', {'queries': queries,'myqueries':myqueries})
        else:
            return HttpResponse("<p>Validation Error</p>")
    else:
        form = PostQuery()
        return render(request,'query/formm.html',{'form':form})

def queryhome(request):
    choice = Health_status.objects.get(user=request.user)
    queries = Query.objects.filter(disease= choice.disease).order_by('?')[:5]
    myqueries = Query.objects.filter(user_posted=request.user)
    return render(request,'query/qaa.html',{'queries':queries,'myqueries':myqueries})

def solution(request,question_id):
    if request.method == 'POST':
        form = PostSolutions(request.POST)
        if form.is_valid():
            qi=Solutions()
            qi.soln_text = form.cleaned_data['soln_text']
            qi.user_posted = request.user
            qi.written = timezone.now()
            qi.query = Query.objects.get(id=question_id)
            qi.save()
            return HttpResponseRedirect(reverse('query:queryhome'))
            #return render(request, 'query/ans.html', {'queries': queries})
        else:
            return HttpResponse("<p>Validation Error</p>")
    else:
        form = PostSolutions()
        squery = Query.objects.get(id=question_id)
        solutions = Solutions.objects.filter(query = squery).order_by('?')[:3]
        return render(request, 'query/ans.html', {'soln': solutions,'form':form,'q_id':question_id})

def upvote(request,soln_id):
  if request.method == 'POST':
    soln = Solutions.objects.get(id=soln_id)
    try:
        user=Upvote.objects.filter(solution=soln).get(voted_user = request.user)
        if user:
            return HttpResponse("<p>sorry you voted once!!!!..................</p>")
        else:
            x=User.objects.get(username = 'asd')
    except:

        soln.vote = soln.vote+1
        soln.save()
        s=Upvote()
        s.solution = soln
        s.voted_user=request.user
        s.save()

        return render(request, 'query/ansclick.html',{'solution': soln})

def downvote(request,soln_id):
  if request.method == 'POST':
    soln = Solutions.objects.get(id=soln_id)
    try:
        user = Downvote.objects.filter(solution=soln).get(voted_user=request.user)
        if user:
            return HttpResponse("<p>sorry you voted once!!!!..................</p>")
        else:
            x = User.objects.get(username='asd')
    except:

        soln.vote = soln.vote-1
        soln.save()
        s=Downvote()
        s.solution = soln
        s.voted_user=request.user
        s.save()
        return render(request,'query/ansclick.html' ,{'solution': soln})





