# -*- coding: utf-8 -*- 
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import (
    render_to_response, redirect, get_object_or_404, RequestContext
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse

def index_view(request):
	#import ipdb; ipdb.set_trace()
	return render_to_response('index.html', RequestContext(request,{}))

def research_view(request):
	return render_to_response('index.html', RequestContext(request,{}))

def research_line_view(request):
	pass

def image_gallery_view(request):
	pass

def image_view(request):
	pass

def team_view(request):
	pass

def bibliography_view(request):
	pass

