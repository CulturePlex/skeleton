# -*- coding: utf-8 -*- 
from django.db import models
from django.template.defaultfilters import slugify


class Project(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

class ResearchLine(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(editable=False)
    subtitle = models.CharField(max_length=150, blank=True, null=True)
    text = models.TextField()
    project = models.ForeignKey(Project, blank=True, null=True, related_name='research_lines')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(ResearchLine, self).save(*args, **kwargs)  

    def __unicode__(self):
        return self.name

class Image(models.Model):
    image = models.ImageField(upload_to='images')
    name = models.CharField(max_length=60)
    caption = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(editable=False)
    project = models.ForeignKey(Project, blank=True, null=True, related_name='images')
    research_line = models.ForeignKey(ResearchLine, blank=True, null=True, related_name='images')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Image, self).save(*args, **kwargs)

    def image_img(self):
        if self.image:
            return u'<img src={0} height="100" width="100"/>'.format(self.image.url)
        else:
            return 'No Image'
    image_img.short_description = 'Image'
    image_img.allow_tags = True

    def __unicode__(self):
        return self.name
    
class Reference(models.Model):
    title = models.CharField(max_length=250)
    authors = models.CharField(max_length=250)
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
    project = models.ForeignKey(Project, blank=True, null=True, related_name='book_reference')
    research_line = models.ForeignKey(ResearchLine, blank=True, null=True, related_name='book_reference')

class JournalReference(Reference):
    journal_title = models.CharField(max_length=250)
    number = models.CharField(max_length=10, blank=True, null=True)
    project = models.ForeignKey(Project, blank=True, null=True, related_name='journal_reference')
    research_line = models.ForeignKey(ResearchLine, blank=True, null=True, related_name='journal_reference')




