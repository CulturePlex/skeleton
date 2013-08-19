# -*- coding: utf-8 -*- 
from django.shortcuts import render_to_response, redirect, RequestContext, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm

from models import User, UserProfile
from forms import UserProfileForm #TODO

def register(request):
    if request.method == 'POST':
        new_user_form = UserCreationForm(request.POST)
        if new_user_form.is_valid():
            new_user = new_user_form.save()
            authenticated_user = authenticate(
                username=request.POST['username'],
                password=request.POST['password1']
                )
            login(request, authenticated_user)
            return redirect('create_profile', new_user.id)
    else:
        new_user_form = UserCreationForm()
    return render_to_response('new_user.html', RequestContext(request,{
        'new_user_form': new_user_form,     
    }))


def create_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    profile = user.profile
    if request.user != user:
        return redirect('index') # decorator
    if profile.clean_fields():
        return redirect('profile', user_id, user.slug)
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST)
        if profile_form.is_valid():
            profile_form.save(user=user, profile=profile)
            return redirect('index') # or profile?
    else:
        profile_form = UserProfileForm()
    return render_to_response('new_profile.html', RequestContext(request, {
        'profile_form': profile_form,
        }))

def profile(request, user_id, user_slug):
    return render_to_response('profile.html', RequestContext(request,{}))


def edit_profile(request, user_id, user_slug):
    user = get_object_or_404(User, id=user_id)
    profile = get_object_or_404(UserProfileModel)
    if request.user != profile_user: #decorator
        return redirect('index')
    pass