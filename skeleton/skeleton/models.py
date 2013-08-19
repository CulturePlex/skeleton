from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.db.models.signals import post_save

class UserProfile(models.Model): 
    affiliation = models.CharField(max_length=250, blank=True, null=True)
    slug = models.SlugField(editable=False)
    user = models.OneToOneField(User, related_name='profile')
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.user.username)
        super(UserProfileModel, self).save(*args, **kwargs)

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfileModel.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)