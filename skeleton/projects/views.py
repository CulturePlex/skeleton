# -*- coding: utf-8 -*-
import collections
import operator
from itertools import chain

from django.http import HttpResponse
from django.shortcuts import (
    render_to_response, get_object_or_404, RequestContext
)
#from django.db.models import get_app, get_models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from models import (
    Project, ResearchLine, Section, Subsection, Image, BookReference,
    JournalReference, AcademicProfile
)
from search import multi_model_search


def index_view(request):
    try:
        project = Project.objects.filter(id=1)[0]
    except IndexError:
        return HttpResponse('Create your project at project_name/admin')
    research_lines = ResearchLine.objects.all()
    images = Image.objects.all()
    # Find cover image or active image for carousel.
    if hasattr(project, 'cover_image'):
        cover_image = project.cover_image
        active_image = None
    else:
        cover_image = None
        if len(images) > 0:
            active_image = images[0]
            if len(images) > 1:
                images = images[1:]
        else:
            active_image = None
    team = AcademicProfile.objects.all()
    if team:
        profile = team[0]
    else:
        profile = None
    return render_to_response('index.html', RequestContext(request, {
        'project': project,
        'research_lines': research_lines,
        'profile': profile,
        'cover_image': cover_image,
        'images': images,
        'active_image': active_image
    }))


def research_line_view(request, research_slug):
    research_line = get_object_or_404(ResearchLine, slug=research_slug)
    sections = research_line.sections.all().order_by('order')
    # Group sections with their subsections.
    sections_dict = collections.OrderedDict()
    for section in sections:
        sections_dict.update({
            section: section.subsections.all().order_by('order')
        })
    collaborators = research_line.collaborators.all()
    books = research_line.book_reference.all()
    journals = research_line.journal_reference.all()
    # Combine and sort reference.
    # Template rendering controlled by templatetags/reference instance.
    references = sorted(
        chain(books, journals), key=operator.attrgetter('authors')
    )
    return render_to_response('research_line.html', RequestContext(request, {
        'research_line': research_line,
        'sections': sections_dict,
        'collaborators': collaborators,
        'references': references,
    }))


def image_gallery_view(request):
    images = Image.objects.all()
    return render_to_response('image_gallery.html', RequestContext(request, {
        'images': images
    }))


def image_view(request, image_slug):
    image = get_object_or_404(Image, slug=image_slug)
    return render_to_response('image.html', RequestContext(request, {
        'image': image
    }))


def team_view(request):
    team = AcademicProfile.objects.all()
    return render_to_response('team.html', RequestContext(request, {
        'team': team
    }))


def bibliography_view(request):
    anchor = request.GET.get('ref_id', '')
    books = BookReference.objects.all()
    journals = JournalReference.objects.all()
    # Combine and sort reference, template rendering
    # controlled by templatetages/reference instance.
    references = sorted(
        chain(books, journals), key=operator.attrgetter('authors')
    )
    return render_to_response('bibliography.html', RequestContext(request, {
        'anchor': anchor,
        'references': references,
    }))


# Need to decide on how to handle reference search.
def book_reference_view(request):
    pass


def journal_reference_view(request):
    pass


def search_view(request):
    """
    Call search utils to search entire db.
    Paginate results.
    """
    # Get the models from the app.
    model_list = [
        Project, ResearchLine, Section, Subsection,
        Image, BookReference, JournalReference, AcademicProfile
    ]
    query_string = request.GET.get('q', '')
    page = request.GET.get('page', '')
    if query_string and not page:
        query_results = multi_model_search(model_list, query_string)
        controlled_results = _handle_query_results(query_results)
        paginator = Paginator(controlled_results, 10)
        results = paginator.page(1)
    elif query_string and page:
        query_results = multi_model_search(model_list, query_string)
        controlled_results = _handle_query_results(query_results)
        paginator = Paginator(controlled_results, 10)
        try:
            results = paginator.page(page)
        except PageNotAnInteger:
            results = paginator.page(1)
        except EmptyPage:
            results = paginator.page(paginator.num_pages)
    else:
        results = ''
    return render_to_response('search.html', RequestContext(request, {
        'results': results,
        'query_string': query_string,
    }))


def profile_view(request, profile_slug):
    profile = get_object_or_404(AcademicProfile, slug=profile_slug)
    return render_to_response('profile.html', RequestContext(request, {
        'profile': profile
    }))


def login(request):
    return render_to_response(
        'login.html',
        {},
        context_instance=RequestContext(request)
    )


def _handle_query_results(results):
    output = []
    #import ipdb; ipdb.set_trace()
    for result in results:
        if result.values():
            obj = result.keys()[0]
            obj_name = obj_name = obj.__class__.__name__
            values = result.values()[0]
            if isinstance(obj, BookReference) or \
                    isinstance(obj, JournalReference):
                result_dict = {
                    'result': obj,
                    'name': obj.title,
                    'type': obj_name,
                    'fields': [getattr(obj, value) for value in values]
                }
            else:
                result_dict = {
                    'result': obj,
                    'name': obj.name,
                    'type': obj_name,
                    'fields': [getattr(obj, value) for value in values]
                }
            output.append(result_dict)

    return output
