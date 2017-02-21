from django.conf.urls import include, url
from django.contrib import admin
from . import views


app_name='userauth'
urlpatterns = [
    url(r'^in$', views.signin, name='login'),
    url(r'^up(?P<status>[A-z]*?)/$', views.signup, name='signup'),
    url(r'^out$', views.signout, name='logout'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile(?P<user_id>[0-9]+)/$', views.fetchprofile, name='profile'),

]

