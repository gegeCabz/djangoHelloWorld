"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.contrib import admin
from django.conf.urls import patterns, url
from HelloWorld.views import hello
from HelloWorld import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^HelloWorld/', hello), 
    url(r'^$', views.HelloWorld_list, name='HelloWorld_list'),
    url(r'^new$', views.HelloWorld_create, name='HelloWorld_new'),
    url(r'^edit/(?P<pk>\d+)$', views.HelloWorld_update, name='HelloWorld_edit'),
    url(r'^delete/(?P<pk>\d+)$', views.HelloWorld_delete, name='HelloWorld_delete'),

]



