from django.contrib import admin
from models import Project, ResearchLine, Image, BookReference, JournalReference
from profiles.models import AcademicProfile

#formfield_overrides = {
    #ImageWithThumbnailField : {'widget' : AdminImageWithThumbnailWidget},
class AcademicProfileInline(admin.TabularInline):
    model = AcademicProfile

class ResearchLineInline(admin.TabularInline):
    model = ResearchLine

class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
    (None, {
        'fields':['name',]
        }),
    ]

    list_display = ['name','research', 'collaborators']

    inlines = [ResearchLineInline, AcademicProfileInline]

    def research(self, instance):
        return u' '.join([line.name for line in instance.research_lines.all()])

    def collaborators(self, instance):
        return u' '.join([collab.name for collab in instance.profile.all()])

    
class ResearchLineAdmin(admin.ModelAdmin):
    #fieldsets = [
    #(None, {'fields':['name']}),
    #('Description', {'fields':['subtitle', 'text']}),
    #('Images', {'fields':['images']}),
    #]
    pass

class ImageAdmin(admin.ModelAdmin):
    list_display = ['image_img']

class BookReferenceAdmin(admin.ModelAdmin):
    pass

class JournalReferenceAdmin(admin.ModelAdmin):
    pass

admin.site.register(Project, ProjectAdmin)
admin.site.register(ResearchLine, ResearchLineAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(BookReference, BookReferenceAdmin)
admin.site.register(JournalReference, JournalReferenceAdmin)