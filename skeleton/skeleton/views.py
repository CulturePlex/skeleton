# -*- coding: utf-8 -*- 
from django.shortcuts import render_to_response, redirect, RequestContext, get_object_or_404
from django.contrib.auth import authenticate, login
from models import User, UserProfile
from forms import UserCreateForm, UserProfileForm

def register(request):
    if request.method == 'POST':
        new_user_form = UserCreateForm(request.POST)
        if new_user_form.is_valid():
            new_user = new_user_form.save()
            authenticated_user = authenticate(
                username=request.POST['username'],
                password=request.POST['password1']
                )
            login(request, authenticated_user)
            return redirect('create_profile')
    else:
        new_user_form = UserCreateForm()
    return render_to_response('new_user.html', RequestContext(request,{
        'new_user_form': new_user_form,     
    }))


def create_profile(request):
    user = request.user
    profile = user.profile
    if profile.clean_fields():
        return redirect('profile', user.id, user.slug)
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, instance=profile)
        if profile_form.is_valid():
            profile_form.save(user=user, instance=profile)
            return redirect('index') # or profile?
    else:
        profile_form = UserProfileForm(instance=profile)
    return render_to_response('new_profile.html', RequestContext(request, {
        'profile_form': profile_form,
        }))


def profile(request, user_id, user_slug):
    profile = get_object_or_404(Profile, id=user_id)
    return render_to_response('profile.html', RequestContext(request, {
        'profile': profile
        }))

def edit_profile(request):
    user = request.user
    profile = get_object_or_404(UserProfile, user=user)
    if request.method == 'POST':
        user_form = UserCreateForm(request.POST, instance=user)
        profile_form = UserProfileForm(request.POST, instance=profile)
        if profile_form.is_valid() and user_form.is_valid():
            user_form.save(instance=profile)
            profile_form.save(user=user, instance=profile)
            return redirect('profile', user.id, user.slug)
    else:
        user_form = UserCreateForm(instance=user)
        profile_form = UserProfileForm(instance=profile)
    return render_to_response('edit_profile.html', RequestContext(request, {
        'profile_form': profile_form,
        }))

def search(request):
    pass