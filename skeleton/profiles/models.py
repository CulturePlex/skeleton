from django.db import models


class AcademicProfile(models.Model):
    name = models.CharField(max_length=60)

    def __unicode__(self):
        return self.name



