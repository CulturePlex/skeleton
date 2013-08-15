# -*- coding: utf-8 -*- 
from django.shortcuts import render_to_response, redirect, RequestContext
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm

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


def user_view(request, user_id, user_slug):
	pass