# -*- coding: utf-8 -*- 
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import (
    render_to_response, redirect, get_object_or_404, RequestContext
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse

def profile_view(request, profile_id, profile_slug):
    pass
