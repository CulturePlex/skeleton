# -*- coding: utf-8 -*- 
from django import forms
from django.db import models
from django.shortcuts import get_object_or_404
from models import UserProfile, User

class UserProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta:
        model = UserProfile
        fields = ['affiliation'] 

    def save(self, user, commit=True, *args, **kwargs):
        import ipdb; ipdb.set_trace()
        profile = super(UserProfileForm, self).save(commit=False)
    	data = self.cleaned_data
    	profile.affiliation = data['affiliation']
    	user.first_name = data['first_name']
    	user.last_name = data['last_name']
        if commit:
            profile.save()
            user.save()
    	return profile