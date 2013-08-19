from django.db import models
from projects.models import Project


class AcademicProfile(models.Model):
    name = models.CharField(max_length=60)
    project =  models.ForeignKey(Project, blank=True, null=True, related_name='profile')

    def __unicode__(self):
        return self.name



