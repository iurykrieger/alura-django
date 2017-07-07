from django.conf.urls import url, include
from django.contrib import admin

from users import views

urlpatterns = [
    url(r'^register/$', views.UserView.as_view(), name='register')
]
