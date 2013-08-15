from django.conf.urls import patterns, include, url


urlpatterns = patterns('profiles.views',
	url(r'^(?P<profile_id>\d+)/(?P<profile_slug>\w+)', 'profile_view', name='profile'),




		)