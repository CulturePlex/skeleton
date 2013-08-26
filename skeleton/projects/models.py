# -*- coding: utf-8 -*- 
from django.db import models
from django.template.defaultfilters import slugify


class Project(models.Model):
    name = models.CharField(max_length=300)
    cover_image = models.ImageField(upload_to='images/project', blank=True, null=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def cover_img(self):
        if self.cover_image:
            return u'<img src={0} height="100" width="100"/>'.format(self.cover_image.url)
        else:
            return 'No Cover Photo'

    cover_img.short_description = 'Cover Image'
    cover_img.allow_tags = True

    def __unicode__(self):
        return self.name

class ResearchLine(models.Model):
    name = models.CharField(max_length=250)
    avatar = models.ImageField(upload_to='images/research', blank=True, null=True)
    subtitle = models.CharField(max_length=150, blank=True, null=True)
    text = models.TextField()
    slug = models.SlugField(editable=False)
    project = models.ForeignKey(Project, blank=True, null=True, related_name='research_lines')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(ResearchLine, self).save(*args, **kwargs)  

    def avatar_img(self):
        if self.avatar:
            return u'<img src={0} height="100" width="100"/>'.format(self.avatar.url)
        else:
            return 'No Avatar'

    avatar_img.short_description = 'Avatar'
    avatar_img.allow_tags = True

    def __unicode__(self):
        return self.name

class Section(models.Model):
    name = models.CharField(max_length=250)
    text = models.TextField()
    order = models.PositiveSmallIntegerField()
    research_lines = models.ForeignKey(ResearchLine, blank=True, null=True, related_name='sections')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Subsection(models.Model):
    name = models.CharField(max_length=250)
    text = models.TextField()
    order = models.PositiveSmallIntegerField()
    section = models.ForeignKey(Section, blank=True, null=True, related_name='subsections')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Image(models.Model):
    image = models.ImageField(upload_to='images/general')
    name = models.CharField(max_length=60)
    caption = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(editable=False)
    project = models.ForeignKey(Project, blank=True, null=True, related_name='images')
    research_line = models.ForeignKey(ResearchLine, blank=True, null=True, related_name='images')
    section = models.ForeignKey(Section, blank=True, null=True, related_name='images')
    subsection = models.ForeignKey(Subsection, blank=True, null=True, related_name='images')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(Image, self).save(*args, **kwargs)

    def image_img(self):
        return u'<img src={0} height="100" width="100"/>'.format(self.image.url)

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

