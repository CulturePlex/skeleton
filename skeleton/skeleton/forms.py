# -*- coding: utf-8 -*- 
from django import forms
from django.db import models
from models import UserProfileModel

class UserProfileForm(forms.ModelForm):
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)   
    class Meta:
        model = UserProfileModel
        fields = ('affiliation',)