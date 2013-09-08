# -*- coding: utf-8 -*- 
from django.conf.urls import patterns, include, url

urlpatterns = patterns('projects.views',
    url(r'^$', 'index_view', name='index'),
    url(r'^bibliography/$', 'bibliography_view', name='bibliography'),
    url(r'^research/(?P<research_id>\d+)/(?P<research_slug>.+)/$', 'research_line_view', name='research_line'),
    url(r'images/gallery/$', 'image_gallery_view', name='gallery'),
    url(r'images/(?P<image_id>\d+)/(?P<image_slug>.+)/$', 'image_view', name='image' ),
    url(r'^team/$', 'team_view', name='team'),
    url(r'^search/$', 'search_view', name='search'),
    url(r'^(?P<profile_id>\d+)/(?P<profile_slug>\w+)/$', 'profile_view', name='profile'),
    )