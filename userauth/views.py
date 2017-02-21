from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render
from userauth.forms import LoginForm, RegForm, RForm, Drform
from django.http import HttpResponse
from .models import User, Health_status, Doctor, Qualification


def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        user = request.user
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                user.login = True
                #return render(request, 'userauth/l.html')
                if user.status == 'In':
                   return HttpResponseRedirect(reverse('userauth:profile'))
                return HttpResponseRedirect(reverse('scrapedstories:mystory'))

            else:
                return render(request, 'userauth/login.html', {'form': form, 'erro_msg': "wrong username or password"})
        else:
            return render(request, 'userauth/login.html', {'form': form, 'erro_msg': "Error!!"})

    else:
        form = LoginForm()
        return render(request, 'userauth/login.html', {'form': form})


def signup(request,status):
   if request.method == "POST":
    form = RegForm(request.POST)
    if status == 'cuser':
      form1 = RForm(request.POST)
    if status == 'doc':
      form1 = Drform(request.POST)
    if form.is_valid():
        if status != 'ins':
            form1.is_valid()
        if request.POST['password'] != request.POST['cpassword']:
            return render(request, 'userauth/signup.html', {'form': form,'form1':form1, 'pass_match': "password do no match"})
        else:
            uzer = form.save(commit=False)
            password = form.cleaned_data['password']
            uzer.set_password(password)
            if status=='doc':
                uzer.status = 'Dr'
            else:
                if status =='ins':
                 uzer.status = 'In'
                else:
                   if status =='cuser':
                     uzer.status = 'Mr/Ms'
                   else:
                       return HttpResponse("<h1>Bad request</h1>")
            uzer.save()
            if status == 'cuser':
                hs=request.POST['healthstatus']
                a=Health_status()
                a.user=uzer
                a.disease=hs
                a.save()
            if status == 'doc':
                a = Doctor()
                a.reg_no = form1.cleaned_data['reg_no']
                a.user = uzer
                a.save()
                b=Qualification()
                b.doctor=a
                b.qualification= form1.cleaned_data['qualification']
                b.save()
            #return render(request, 'uprof/login.html', {'form': form, 'erro_msg': "email not registered"})
            #return HttpResponse("<h1>Regn successful</h1>")
            #if uzer.status == 'Dr':
                #doctorprof = Doctor.objects.get(user = uzer)
                #qualifications = Qualification.objects.get(doctor = doctorprof)
            forml=LoginForm()
            return render(request, 'userauth/login.html' ,{'form':forml})
    else:
          return HttpResponse("<h1>validation error</h1>")

   else:
        if status == 'cuser':
           form = RegForm()
           form1 = RForm()
           return render(request, 'userauth/signup.html', {'form': form,'form1': form1,'status':status})
        if status == 'ins':
           form = RegForm()
           return render(request, 'userauth/signupinstitution.html', {'form': form,'status':status})
        if status == 'doc':
            form = RegForm()
            form1=Drform()
            return render(request, 'userauth/signupdoctor.html', {'form': form,'form1': form1, 'status': status})


#@transaction.atomic
#@login_required
def signout(request):
    logout(request)
    forml = LoginForm()
    #return render(request, 'userauth/login.html', {'form': forml})
    return HttpResponseRedirect(reverse('userauth:login'))#('/sign/in')

#@login_required
def profile(request):
   uzer=request.user
   if uzer.status == 'Dr':
       doctorprof = Doctor.objects.get(user = uzer)
       qualifications = Qualification.objects.filter(doctor = doctorprof)
       return render(request, 'userauth/indexdoc.html', {'user': uzer,'qualification':qualifications,'doctorprof':doctorprof })
   else:
   #return render(request,'userauth/profile.html',{'user':user})
      return render(request,'userauth/index.html',{'user':uzer,})


def fetchprofile(request,user_id):
   uzer=User.objects.get(id = user_id)
   if uzer.status == 'Dr':
       doctorprof = Doctor.objects.get(user = uzer)
       qualifications = Qualification.objects.filter(doctor = doctorprof)
       return render(request, 'userauth/indexdoc.html', {'user': uzer,'qualification':qualifications,'doctorprof':doctorprof })
   else:
   #return render(request,'userauth/profile.html',{'user':user})
      return render(request,'userauth/index.html',{'user':uzer,})