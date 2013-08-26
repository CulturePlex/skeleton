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
    project = Project.objects.filter(id=1)[0]
    if not project:
    	return HttpResponse('Create your project at project_name/admin')
    research_lines = ResearchLine.objects.all()
    images = Image.objects.all()
    cover_image = project.cover_image
    return render_to_response('index.html', RequestContext(request, {
    	'project': project,
    	'research_lines': research_lines,
    	'images': images,
    	'cover_image': cover_image
    	}))

def research(request):
    research_lines = ResearchLine.objects.all()
    return render_to_response('research.html', RequestContext(request,{
    	'research_lines': research_lines
    	}))

def research_line(request, research_id, research_slug):
	research_line = get_object_or_404(ResearchLine, id=research_id)
	sections = research_line.sections.all().order_by('order')
	collaborators = research_line.collaborators.all()
	books = research_line.book_reference.all()
	journals = research_line.journal_reference.all()
	return render_to_response('research_line.html', RequestContext(request, {
		'research_line': research_line,
		'collaborators': collaborators,
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

def bibliography(request):
	books = BookReference.objects.all()
	journals = JournalReference.objects.all()
	references = books + journals # sort by author
	return render_to_response('bibliography.html', RequestContext(request, {
		'references': references,
		}))

