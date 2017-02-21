from django.conf.urls import url, include
from django.contrib import admin
from .import views
app_name='share'
urlpatterns = [
    url(r'^$', views.share,name='share'),
    url(r'^upvote(?P<soln_id>[0-9]+)/$', views.upvote, name='upvote'),
    url(r'^downvote(?P<soln_id>[0-9]+)/$', views.downvote, name='downvote'),


]
