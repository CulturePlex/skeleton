# -*- coding: utf-8 -*- 
from django.conf.urls import patterns, include, url

urlpatterns = patterns('projects.views',
    url(r'^$', 'index', name='index'),
    url(r'^bibliography/$', 'bibliography', name='bibliography'),
    url(r'^research/(?P<research_id>\d+)/(?P<research_slug>.+)/$', 'research_line', name='research_line'),
    url(r'images/gallery/$', 'image_gallery', name='gallery'),
    url(r'images/(?P<image_id>\d+)/(?P<image_slug>.+)/$', 'image', name='image' ),
    url(r'^team/$', 'team', name='team'),
    url(r'^search/$', 'search', name='search'),
    )