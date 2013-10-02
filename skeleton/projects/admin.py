from django.contrib import admin
from models import (
    Project, ResearchLine, Section, Subsection, Image, BookReference,
    JournalReference, AcademicProfile
)


class AcademicProfileInline(admin.TabularInline):
    model = AcademicProfile


class ResearchLineInline(admin.TabularInline):
    model = ResearchLine


class ImageInline(admin.TabularInline):
    model = Image
    fields = ['image', 'name', 'caption', 'description']


class BookReferenceInline(admin.TabularInline):
    model = BookReference


class JournalReferenceInline(admin.TabularInline):
    model = JournalReference


class SectionInline(admin.TabularInline):
    model = Section


class SubsectionInline(admin.TabularInline):
    model = Subsection


class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': ['name']
            }),
        ('Description', {
            'fields': ['description']
            }),
    ]

    list_display = ['name', 'research', 'collaborators', 'cover_img']
    inlines = [
        ImageInline,
        ResearchLineInline,
        AcademicProfileInline,
        BookReferenceInline,
        JournalReferenceInline
    ]

    def research(self, instance):
        return u' ,'.join([
            line.name for line in instance.research_lines.all()
        ])

    def collaborators(self, instance):
        return u' ,'.join([
            profile.name for profile in instance.profiles.all()
        ])


class ResearchLineAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': ['name']
            }),
        ('Description', {
            'fields': ['subtitle', 'text']
            })
    ]
    list_display = ['avatar_img', 'name', 'subtitle', 'collaborators']
    inlines = [
        ImageInline,
        SectionInline,
        BookReferenceInline,
        JournalReferenceInline,
        AcademicProfileInline
    ]

    def collaborators(self, instance):
        return u' ,'.join([
            collab.name for collab in instance.collaborators.all()
        ])


class SectionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': ['name', 'order', 'research_lines']
            }),
        ('Description', {
            'fields': ['text']
            })
    ]
    list_display = ['order', 'name', 'avatar_img']
    inlines = [ImageInline, SubsectionInline]


class SubsectionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': ['name', 'order', 'section']
            }),
        ('Description', {
            'fields': ['text']
            })
    ]
    list_display = ['order', 'name', 'avatar_img']
    inlines = [ImageInline]


class ImageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': ['name', 'image']
            }),
        ('Description', {
            'fields': ['caption', 'description']
            }),
        ('Associated With', {
            'fields': ['research_line', 'section', 'subsection']
            })
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
        ('Publication', {
            'fields': ['place_of_pub', 'publisher', 'date', 'edition']
            }),
        ('Reference', {
            'fields': ['pages', 'url']
            }),
        ('Associated With', {
            'fields': ['project', 'research_line']
            })
    ]
    list_display = [
        'title', 'authors', 'book_title', 'publisher', 'place_of_pub', 'date'
    ]


class JournalReferenceAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': ['title', 'journal_title']
            }),
        ('Authors/Editors', {
            'fields': ['authors']
            }),
        ('Publication', {
            'fields': ['place_of_pub', 'publisher', 'date', 'number']
            }),
        ('Reference', {
            'fields': ['pages', 'url']
            }),
        ('Associated With', {
            'fields': ['project', 'research_line']
            })
    ]
    list_display = [
        'title',
        'authors',
        'journal_title',
        'publisher',
        'place_of_pub',
        'date'
    ]


class AcademicProfileAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': ['name', 'institution', 'website']
            }),
        ('About', {
            'fields': ['bio']
            })
    ]
    list_display = ['name', 'institution', 'profile_img']

    inlines = [ImageInline]

admin.site.register(Project, ProjectAdmin)
admin.site.register(ResearchLine, ResearchLineAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Subsection, SubsectionAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(BookReference, BookReferenceAdmin)
admin.site.register(JournalReference, JournalReferenceAdmin)
admin.site.register(AcademicProfile, AcademicProfileAdmin)
