# -*- coding: utf-8 -*- 
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import (
    render_to_response, redirect, get_object_or_404, RequestContext
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse

def index(request):
    #import ipdb; ipdb.set_trace()
    return render_to_response('index.html', RequestContext(request,{}))

def research(request):
    return render_to_response('index.html', RequestContext(request,{}))

def research_line(request):
    pass

def image_gallery(request):
    pass

def image(request):
    pass

def team(request):
    pass

def bibliography(request):
    pass

