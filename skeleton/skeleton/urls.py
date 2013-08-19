# -*- coding: utf-8 -*- 
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'skeleton.views.home', name='home'),
    # url(r'^skeleton/', include('skeleton.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', 'django.contrib.auth.views.logout_then_login'),
    url(r'^register', 'skeleton.views.register', name='register'),
    url(r'^user/create_profile/(?P<user_id>\d+)', 'skeleton.views.create_profile', name='create_profile'),
    url(r'^user/profile/(?P<user_id>\d+)/(?P<user_slug>\w+)', 'skeleton.views.profile', name='profile'),
    url(r'^', include('projects.urls')),
    url(r'^profile', include('profiles.urls')),

)
urlpatterns += staticfiles_urlpatterns()