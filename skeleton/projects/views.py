# -*- coding: utf-8 -*- 
from django.http import HttpResponse#, HttpResponseRedirect
from django.shortcuts import (
    render_to_response, redirect, get_object_or_404, RequestContext
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
#from django.core.urlresolvers import reverse

from models import *
from profiles.models import AcademicProfile

def index(request):
    project = get_object_or_404(Project, id=1) #write custom error that sends user to admin
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
	research_line = get_object_or_404(ResearchLine, id=research_id)
	return render_to_response('research_line.html', ReqeustContext(request, {
		'research_line': research_line,
		}))

def line_collaborators(request, research_id, research_slug):
	research_line = get_object_or_404(ResearchLine, id=research_id)
	collaborators = research_line.collaborators.all()
	return render_to_response('line_collaborators.html', RequestContext(request, {
		'research_line': research_line,
		'collaborators': collaborators
		}))

def research_line_bibliography(request, research_id, research_slug):
	research_line = get_object_or_404(ResearchLine, research_id)
	books = research_line.book_reference.all()
	journals = research_line.journal_reference.all()
	references = books + journals # sort by author
	return render_to_response('bibliography.html', RequestContext(request, {
		'references': references,
		}))

def image_gallery(request):
	images = Image.objects.all()
   	return render_to_response('image_gallery.html', RequestContext(request, {
   		'images': images
   		}))

def image(request, image_id, image_slug):
	image = get_object_or_404(Image, id=image_id)
	return render_to_response('image.html', RequestContext(request, {
		'image': image
		}))

def team(request):
	team = AcademicProfile.objects.all()
	return render_to_response('team.html', RequestContext(request, {
		'team': team
		}))

    pass

def bibliography(request):
	books = BookReference.objects.all()
	journals = JournalReference.objects.all()
	references = books + journals # sort by author
	return render_to_response('bibliography.html', RequestContext(request, {
		'references': references,
		}))

