from django.contrib import admin
from models import UserProfile


class ProfileAdmin(admin.ModelAdmin):

	fieldsets = [
	(None, {
		'fields': ['affiliation']
		}) 
	]

	list_display = ['username', 'email', 'first', 'last', 'affiliation']

	def username(self, instance):
		return instance.user.username

	def email(self, instance):
		return instance.user.email

	def first(self, instance):
		return instance.user.first_name

	def last(self, instance):
		return instance.user.last_name

admin.site.register(UserProfile, ProfileAdmin)

