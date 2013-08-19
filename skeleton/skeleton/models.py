from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.db.models.signals import post_save

class UserProfile(models.Model): 
    affiliation = models.CharField(max_length=250, blank=True, null=True)
    slug = models.SlugField(editable=False)
    user = models.OneToOneField(User, related_name='profile')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.user.username)
        super(UserProfile, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.user.username

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)