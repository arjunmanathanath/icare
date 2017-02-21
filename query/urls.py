from django.conf.urls import url
from . import views

app_name = 'query'
urlpatterns = [
    url(r'^$', views.queryhome, name='queryhome'),
    url(r'^post/$', views.postquery, name='postquery'),
    url(r'^solution(?P<question_id>[0-9]+)/$', views.solution, name='solution'),
    url(r'^upvote(?P<soln_id>[0-9]+)/$', views.upvote, name='upvote'),
    url(r'^downvote(?P<soln_id>[0-9]+)/$', views.downvote, name='downvote'),
    #url(r'^post/$', views.query, name='postquery'),
    #url(r'^$', views.query, name='querypage'),
    #url(r'home^$', views.query, name='querypage'),


]
