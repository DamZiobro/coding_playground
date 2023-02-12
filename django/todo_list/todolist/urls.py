#! /usr/bin/env python

from django.urls import path
from django.views.generic import ListView
from . import views

urlpatterns = [
    path(r'create/', views.create, name='create'),
    path(r'list/', views.ListTasks.as_view(), name='list'),
    path(r'hello/', views.HelloView.as_view(), name='crud'),
]
