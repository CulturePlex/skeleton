# -*- coding: utf-8 -*- 
from django import forms
from django.db import models
from django.shortcuts import get_object_or_404
from models import UserProfile, User

class UserProfileForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)   
    affiliation = forms.CharField(max_length=250)

    def save(self, user):
    	profile = get_object_or_404(UserProfile, user=user)
    	data = self.cleaned_data
    	profile.affiliation = data['affiliation']
    	profile.save()
    	user.first_name = data['first_name']
    	user.last_name = data['last_name']
    	user.save()
    	return profile