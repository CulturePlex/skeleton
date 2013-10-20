# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns(
    'projects.views',
    url(r'^$', 'index_view', name='index'),
    url(r'^bibliography/$', 'bibliography_view', name='bibliography'),
    url(r'^research/(?P<research_slug>.+)/$',
        'research_line_view', name='research_line'),
    url(r'^images/gallery/$', 'image_gallery_view', name='gallery'),
    url(r'^images/gallery/(?P<image_slug>.+)/$', 'image_view', name='image'),
    url(r'^team/$', 'team_view', name='team'),
    url(r'^team/(?P<profile_slug>(\w|-)+)/$', 'profile_view', name='profile'),
    url(r'^search/$', 'search_view', name='search'),
    url(r'^login/$', 'login', name='login'),
)
