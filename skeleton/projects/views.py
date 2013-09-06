# -*- coding: utf-8 -*- 
import collections
import operator
from itertools import chain

from django.http import HttpResponse
from django.shortcuts import (
    render_to_response, redirect, get_object_or_404, RequestContext
)
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from models import *
from profiles.models import AcademicProfile
from utils import multi_model_search

def index(request):
    try:
        project = Project.objects.filter(id=1)[0]
    except IndexError:
    	return HttpResponse('Create your project at project_name/admin')
    research_lines = ResearchLine.objects.all()
    images = Image.objects.all()
    if len(images) > 0:
        active_image = images[0]
        if len(images) > 1:
            images = images[1:]
    else:
    	active_image = None
    try:
    	cover_image = project.cover_image
    except:
    	cover_image = None
    team = AcademicProfile.objects.all()
    print team
    return render_to_response('index.html', RequestContext(request, {
    	'project': project,
    	'research_lines': research_lines,
    	'team': team,
    	'cover_image': cover_image,
        'images': images,
        'active_image': active_image
    	}))


def research_line(request, research_id, research_slug):
	research_line = get_object_or_404(ResearchLine, id=research_id)
	sections = research_line.sections.all().order_by('order')
	sections_dict = collections.OrderedDict()
	for section in sections:
		sections_dict.update({section: section.subsections.all().order_by('order')})
	collaborators = research_line.collaborators.all()
	books = research_line.book_reference.all()
	journals = research_line.journal_reference.all()
	references = sorted(chain(books, journals), key=operator.attrgetter('authors'))
	return render_to_response('research_line.html', RequestContext(request, {
		'research_line': research_line,
		'sections': sections_dict,
		'collaborators': collaborators,
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

def bibliography(request):
	books = BookReference.objects.all()
	journals = JournalReference.objects.all()
	references = sorted(chain(books, journals), key=operator.attrgetter('authors'))
	return render_to_response('bibliography.html', RequestContext(request, {
		'references': references,
		}))

def search(request):
	my_models = [
		Project, ResearchLine, Section, Subsection, 
		Image, Reference, BookReference, JournalReference
		]
	query_string = request.GET.get('q', '')
	page = request.GET.get('page', ''None'')
	if query_string and  not page:
		query_results = multi_model_search(my_models, query_string)
        paginator = Paginator(query_results, 25)
        results = paginator.page(1)
    elif query_string and page:
    	query_results = multi_model_search(my_models, query_string)
        paginator = Paginator(query, 25)
    	try:
            results = paginator.page(page)
    	except PageNotAnInteger:
        	# If page is not an integer, deliver first page.
        	results = paginator.page(1)
    	except EmptyPage:
        	# If page is out of range (e.g. 9999), deliver last page of results.
        	results = paginator.page(paginator.num_pages)
    else:
    	results = None
    return render_to_response('search.html', RequestContext(request, {
    	'results': results
    	}))



"""
	model_dict = {
		'project': Project, 
		'research_line': ResearchLine, 
		'section': Section, 
		'subsection': Subsection, 
		'image': Image, 
		'reference': Reference, 
		'book_reference': BookReference, 
		'journal_reference': JournalReference
		}
"""



