from django.contrib import admin
from models import UserProfile


class ProfileAdmin(admin.ModelAdmin):
	pass

admin.site.register(UserProfile, ProfileAdmin)

