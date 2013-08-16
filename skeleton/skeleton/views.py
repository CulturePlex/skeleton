# -*- coding: utf-8 -*- 
from django.shortcuts import render_to_response, redirect, RequestContext, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm

from models import User
from forms import ProfileForm #TODO

def new_user_view(request):
    if request.method == 'POST':
        new_user_form = UserCreationForm(request.POST)
        if new_user_form.is_valid():
            new_user = new_user_form.save()
            authenticated_user = authenticate(
                username=request.POST['username'],
                password=request.POST['password1']
                )
            login(request, authenticated_user)
            return redirect('index')
    else:
        new_user_form = UserCreationForm()
    return render_to_response('new_user.html', RequestContext(request,{
        'new_user_form': new_user_form
    }))

def user_redirct(request, user_id): # change in settings
    pass

#@check_request_user
def new_user_profile(request, user_id):
    profile_user = get_object_or_404(User, id=user_id)
    if profile_user != request.user:
        return redirect('index')  #### TODO make decorator to handle this
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect()
    else:
        new_profile_form = ProfileForm()
    return render_to_response('new_profile.html', RequestContext(request, {}))



def user_view(request, user_id, user_slug):
    pass