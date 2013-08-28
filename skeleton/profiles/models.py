from django.db import models
from projects.models import Project, ResearchLine


class AcademicProfile(models.Model):
    name = models.CharField(max_length=60)
    picture = models.ImageField(upload_to='images/profile', blank=True, null=True)
    institution = models.CharField(max_length=250, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    project =  models.ForeignKey(Project, blank=True, null=True, related_name='profiles') # change to profiles
    research = models.ForeignKey(ResearchLine, blank=True, null=True, related_name='collaborators')

    def __unicode__(self):
        return self.name



