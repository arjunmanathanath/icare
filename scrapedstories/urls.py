from django.conf.urls import url, include
from django.contrib import admin
from . import views

app_name='scrapedstories'
urlpatterns = [

    url(r'^$', views.scraperpopulate, name='scraperpopulate'),
    url(r'^mystory/$', views.mystory, name='mystory'),

]