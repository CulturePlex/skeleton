# -*- coding: utf-8 -*- 
from django.conf.urls import patterns, include, url


urlpatterns = patterns('projects.views',
    url(r'^$', 'index_view', name='index'),
    url(r'^research', 'research_view', name='research'),


    )