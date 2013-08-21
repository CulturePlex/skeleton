# -*- coding: utf-8 -*- 
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import (
    render_to_response, redirect, get_object_or_404, RequestContext
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse

from models import *

def index(request):
	project = get_object_or_404(Projects, id=1)
	research_lines = ResearchLine.objects.all()
	images = Image.objects.all()
	image = None
	if len(images) < 1:
		image = None
		images = None
	elif len(images) == 1:
		image = images[0]
		images = None
    return render_to_response('index.html', RequestContext(request, {
    	'project': project,
    	'research_lines': research_lines,
    	'image': image,
    	'images': images,
    	}))

def research(request):
	research_lines = ResearchLine.objects.all()
    return render_to_response('research.html', RequestContext(request,{
    	'research_lines': research_lines
    	}))

def research_line(request, research_id, research_slug):
    pass

def research_line_bibliography(request, research_id, research_slug):
	pass

def image_gallery(request):
    pass

def image(request, image_id, image_slug):
    pass

def team(request):
    pass

def bibliography(request):
    pass

