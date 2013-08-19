# -*- coding: utf-8 -*- 
from django.db import models
from profiles.models import AcademicProfile

class Project(models.Model):
    name = models.CharField(max_length=300)
    contributors =  models.ForeignKey(AcademicProfile, blank=True, null=True)
    research = models.ForeignKey('ResearchLine', blank=True, null=True)
    images = models.ForeignKey('Image', blank=True, null=True)
    references = models.ForeignKey('Reference', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name
    

class ResearchLine(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(editable=False)
    subtitle = models.CharField(max_length=150, blank=True, null=True)
    text = models.TextField()
    images = models.ForeignKey('Image', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(UserProfile, self).save(*args, **kwargs)  

    def __unicode__(self):
        return self.name

class Image(models.Model):
    name = models.CharField(max_length=60)
    caption = models.CharField(max_length=100, blank=True, null=True)
    descritption = models.TextField(blank=True, null=True)
    slug = models.SlugField(editable=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(UserProfile, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name
    

class Reference(models.Model):
    authors = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    date = models.DateField(blank=True, null=True)
    place_of_pub = models.CharField(max_length=100, blank=True, null=True)
    publisher = models.CharField(max_length=50, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    pages = models.CharField(max_length=20, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title
    

class BookReference(Reference):
    book_title = models.CharField(max_length=250)
    editors = models.CharField(max_length=250, blank=True, null=True)
    edition = models.CharField(max_length=25, blank=True, null=True)

class JournalReference(Reference):
    number = models.CharField(max_length=10, blank=True, null=True)






