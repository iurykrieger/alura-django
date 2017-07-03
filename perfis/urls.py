from django.conf.urls import url, include
from django.contrib import admin

from perfis.views import index, profile

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^profiles/(?P<profile_id>\d+)$', profile, name='profile')
]
