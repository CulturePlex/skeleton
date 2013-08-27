# -*- coding: utf-8 -*- 
from django.conf.urls import patterns, include, url

urlpatterns = patterns('projects.views',
    url(r'^$', 'index', name='index'),
    url(r'^research/$', 'research', name='research'),
    url(r'^research/(?P<research_id>\d+)/(?P<research_slug>.+)', 'research_line', name='research_line'),

    )