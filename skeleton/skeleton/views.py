# -*- coding: utf-8 -*- 
from django.shortcuts import render_to_response, redirect, RequestContext, get_object_or_404
from django.contrib.auth import logout
from models import User, UserProfile
from forms import UserCreateForm, UserProfileForm

def login(request):
    return render_to_response('login.html', RequestContext(request, {}))

def search(request):
    if request.GET == 'q':
        pass
    pass