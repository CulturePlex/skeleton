from django.contrib import admin
from models import Project, ResearchLine, Image, BookReference, JournalReference
from profiles.models import AcademicProfile

#formfield_overrides = {
    #ImageWithThumbnailField : {'widget' : AdminImageWithThumbnailWidget},
class AcademicProfileInline(admin.TabularInline):
    model = AcademicProfile

class ResearchLineInline(admin.TabularInline):
    model = ResearchLine

class ImageInline(admin.TabularInline):
    model = Image

class BookReferenceInline(admin.TabularInline):
    model = BookReference

class JournalReferenceInline(admin.TabularInline):
    model = JournalReference

class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
    (None, {
        'fields':['name']
        }),
    ('Description', {
        'fields': ['description']
        })
    ]
    list_display = ['name','research', 'collaborators']
    inlines = [ResearchLineInline, ImageInline, AcademicProfileInline]

    def research(self, instance):
        return u' ,'.join([line.name for line in instance.research_lines.all()])

    def collaborators(self, instance):
        return u' ,'.join([profile.name for profile in instance.profiles.all()])

    
class ResearchLineAdmin(admin.ModelAdmin):
    fieldsets = [
    (None, {
        'fields':['name']
        }),
    ('Description', {
        'fields':['subtitle', 'text']
        }),
    ]
    list_display = ['name', 'subtitle', 'collaborators']
    inlines = [ImageInline, AcademicProfileInline, BookReferenceInline, JournalReferenceInline]

    def collaborators(self, instance):
        return u' ,'.join([collab.name for collab in instance.collaborators.all()])


class ImageAdmin(admin.ModelAdmin):
    fieldsets = [
    (None, {
        'fields': ['name']
        }),
    ('Description', {
        'fields': ['caption', 'description']
        }),
    ]
    list_display = ['name', 'caption', 'image_img']

class BookReferenceAdmin(admin.ModelAdmin):
    fieldsets = [
    (None, {
        'fields': ['title', 'book_title']
        }),
    ('Authors/Editors', {
        'fields': ['authors', 'editors']
        }),
    ('Publication',{
        'fields': ['place_of_pub', 'publisher', 'date', 'edition']
        }),
    ('Reference', {
        'fields': ['pages', 'url']
        })
    ]
    list_display = ['title', 'authors', 'book_title', 'publisher', 'place_of_pub', 'date']
    

class JournalReferenceAdmin(admin.ModelAdmin):
    fieldsets = [
    (None, {
        'fields': ['title', 'journal_title']
        }),
    ('Authors/Editors', {
        'fields': ['authors']
        }),
    ('Publication',{
        'fields': ['place_of_pub', 'publisher', 'date', 'number']
        }),
    ('Reference', {
        'fields': ['pages', 'url']
        })
    ]
    list_display = ['title', 'authors', 'journal_title', 'publisher', 'place_of_pub', 'date']

admin.site.register(Project, ProjectAdmin)
admin.site.register(ResearchLine, ResearchLineAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(BookReference, BookReferenceAdmin)
admin.site.register(JournalReference, JournalReferenceAdmin)