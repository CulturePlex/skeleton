from django.contrib import admin
from models import Project, ResearchLine, Image, BookReference, JournalReference
from profiles.models import AcademicProfile

class AcademicProfileInline(admin.TabularInline):
	model = AcademicProfile
	extra = 2

class ProjectAdmin(admin.ModelAdmin):
	fieldsets = [
	(None,		 {'fields':['name']}),

	]
	
class ResearchLineAdmin(admin.ModelAdmin):
	#fieldsets = [
	#(None, {'fields':['name']}),
	#('Description', {'fields':['subtitle', 'text']}),
	#('Images', {'fields':['images']}),
	#]
	pass

class ImageAdmin(admin.ModelAdmin):
	pass

class BookReferenceAdmin(admin.ModelAdmin):
	pass

class JournalReferenceAdmin(admin.ModelAdmin):
	pass

admin.site.register(Project, ProjectAdmin)
admin.site.register(ResearchLine, ResearchLineAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(BookReference, BookReferenceAdmin)
admin.site.register(JournalReference, JournalReferenceAdmin)