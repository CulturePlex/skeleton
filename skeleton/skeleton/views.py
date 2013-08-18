# -*- coding: utf-8 -*- 
from django.shortcuts import render_to_response, redirect, RequestContext, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm

from models import User, UserProfileModel
from forms import UserProfileForm #TODO

def register_view(request):
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


def create_profile_view(request, user_id):
    #import ipdb; ipdb.set_trace()
    user = get_object_or_404(User, id=user_id)
    profile = user.profile
    if request.user != user:
        return redirect('index')
    if profile.clean_fields():
        return redirect('profile', user_id, user.slug)
    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('index') # or profile?
    else:
        profile_form = UserProfileForm()
    return render_to_response('new_profile.html', RequestContext(request, {
        'profile_form': profile_form,
        }))

def profile_view(request, user_id, user_slug):
    return render_to_response('profile.html', RequestContext(request,{}))


"""def profile_view(request, user_id, user_slug):
    user = get_object_or_404(User, id=user_id)
    profile = get_object_or_404(UserProfileModel)
    if request.user != profile_user:
        return redirect('index')
    if request.method == 'POST':
        edited_user_form = UserCreationForm(request.POST, instance=user)
        edited_profile_from = UserProfileForm(request.POST, instance=profile)
        if edited_user_form.is_valid() and edited_profile_from.is_valid():
            new_user = new_user_form.save(commit=False)
            new_profile = new_profile_form.save(commit=False)
            new_user.first_name = new_profile.first_name
            new_user.last_name = new_profile.last_name
            new_user.email = new_profile.email
            new_user.save()
            new_profile.user = new_user
            new_profile.save()
            authenticated_user = authenticate(
                username=request.POST['username'],
                password=request.POST['password1']
                )
            login(request, authenticated_user)
            return redirect('index')
    else:
        edited_user_form = UserCreationForm(instance=user)
        edited_profile_from = UserProfileForm(instance=profile)
    return render_to_response('new_user.html', RequestContext(request,{
        'new_user_form': new_user_form,
        'new_profile_form': new_profile_form,       
    }))"""