from django.contrib import admin
from models import UserProfileModel, User


class ProfileAdmin(admin.ModelAdmin):
	pass

class UserAdmin(admin.ModelAdmin):
	pass

admin.site.register(UserProfileModel, ProfileAdmin)

