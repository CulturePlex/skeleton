from django.contrib import admin
from models import UserProfileModel


class ProfileAdmin(admin.ModelAdmin):
	pass

admin.site.register(UserProfileModel, ProfileAdmin)

