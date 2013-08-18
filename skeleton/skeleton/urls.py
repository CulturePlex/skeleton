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
    url(r'^register', 'skeleton.views.register_view', name='register'),
    #url(r'^profile/redirect', 'skeleton.views.user_redirect_view', name='user_redirect'),
    url(r'^create_profile/(?P<user_id>\d+)', 'skeleton.views.create_profile_view', name='create_profile'),
    url(r'^user/(?P<user_id>\d+)/(?P<user_slug>\w+)', 'skeleton.views.profile_view', name='profile'),
    url(r'^', include('projects.urls')),
    url(r'^profile', include('profiles.urls')),

)
urlpatterns += staticfiles_urlpatterns()