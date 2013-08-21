# -*- coding: utf-8 -*- 
from django import forms
from django.db import models
from forms import UserProfileForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm
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


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True, *args, **kwargs):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


