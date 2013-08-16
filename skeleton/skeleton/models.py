from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class UserProfile(models.Model):    
    email = models.EmailField()
    affiliation = models.CharField(max_length=250, blank=True, null=True)
    slug = models.SlugField(max_length=100)
    user = models.ForeignKey(User, related_name='profile')

    class Meta:
        unique_together = (('user', 'email'),)
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.user.username)
        super(UserProfile, self).save(*args, **kwargs)

