from django.conf.urls import url, include
from django.contrib import admin

from perfis import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^profiles/(?P<profile_id>\d+)$', views.profile, name='detail'),
    url(r'^profiles/(?P<invited_profile>\d+)/invite$', views.invite, name='invite'),
    url(r'^invitation/(?P<invitation_id>\d+)/accept$', views.accept, name='accept')
]
