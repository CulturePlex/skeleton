# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Project'
        db.create_table(u'projects_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'projects', ['Project'])

        # Adding model 'ResearchLine'
        db.create_table(u'projects_researchline', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('subtitle', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='research_lines', null=True, to=orm['projects.Project'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'projects', ['ResearchLine'])

        # Adding model 'Section'
        db.create_table(u'projects_section', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('text', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('order', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('research_lines', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sections', to=orm['projects.ResearchLine'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'projects', ['Section'])

        # Adding model 'Subsection'
        db.create_table(u'projects_subsection', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('text', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('order', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('section', self.gf('django.db.models.fields.related.ForeignKey')(related_name='subsections', to=orm['projects.Section'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'projects', ['Subsection'])

        # Adding model 'Image'
        db.create_table(u'projects_image', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('project', self.gf('django.db.models.fields.related.OneToOneField')(blank=True, related_name='cover_image', unique=True, null=True, to=orm['projects.Project'])),
            ('research_line', self.gf('django.db.models.fields.related.OneToOneField')(blank=True, related_name='avatar', unique=True, null=True, to=orm['projects.ResearchLine'])),
            ('section', self.gf('django.db.models.fields.related.OneToOneField')(blank=True, related_name='avatar', unique=True, null=True, to=orm['projects.Section'])),
            ('subsection', self.gf('django.db.models.fields.related.OneToOneField')(blank=True, related_name='avatar', unique=True, null=True, to=orm['projects.Subsection'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'projects', ['Image'])

        # Adding model 'Reference'
        db.create_table(u'projects_reference', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('authors', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('place_of_pub', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('publisher', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('pages', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'projects', ['Reference'])

        # Adding model 'BookReference'
        db.create_table(u'projects_bookreference', (
            (u'reference_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['projects.Reference'], unique=True, primary_key=True)),
            ('book_title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('editors', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('edition', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='book_reference', null=True, to=orm['projects.Project'])),
            ('research_line', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='book_reference', null=True, to=orm['projects.ResearchLine'])),
        ))
        db.send_create_signal(u'projects', ['BookReference'])

        # Adding model 'JournalReference'
        db.create_table(u'projects_journalreference', (
            (u'reference_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['projects.Reference'], unique=True, primary_key=True)),
            ('journal_title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='journal_reference', null=True, to=orm['projects.Project'])),
            ('research_line', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='journal_reference', null=True, to=orm['projects.ResearchLine'])),
        ))
        db.send_create_signal(u'projects', ['JournalReference'])

        # Adding model 'AcademicProfile'
        db.create_table(u'projects_academicprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('institution', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('bio', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='profiles', null=True, to=orm['projects.Project'])),
            ('research', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='collaborators', null=True, to=orm['projects.ResearchLine'])),
        ))
        db.send_create_signal(u'projects', ['AcademicProfile'])


    def backwards(self, orm):
        # Deleting model 'Project'
        db.delete_table(u'projects_project')

        # Deleting model 'ResearchLine'
        db.delete_table(u'projects_researchline')

        # Deleting model 'Section'
        db.delete_table(u'projects_section')

        # Deleting model 'Subsection'
        db.delete_table(u'projects_subsection')

        # Deleting model 'Image'
        db.delete_table(u'projects_image')

        # Deleting model 'Reference'
        db.delete_table(u'projects_reference')

        # Deleting model 'BookReference'
        db.delete_table(u'projects_bookreference')

        # Deleting model 'JournalReference'
        db.delete_table(u'projects_journalreference')

        # Deleting model 'AcademicProfile'
        db.delete_table(u'projects_academicprofile')


    models = {
        u'projects.academicprofile': {
            'Meta': {'object_name': 'AcademicProfile'},
            'bio': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'institution': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'profiles'", 'null': 'True', 'to': u"orm['projects.Project']"}),
            'research': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'collaborators'", 'null': 'True', 'to': u"orm['projects.ResearchLine']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        u'projects.bookreference': {
            'Meta': {'object_name': 'BookReference', '_ormbases': [u'projects.Reference']},
            'book_title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'edition': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'editors': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'book_reference'", 'null': 'True', 'to': u"orm['projects.Project']"}),
            u'reference_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['projects.Reference']", 'unique': 'True', 'primary_key': 'True'}),
            'research_line': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'book_reference'", 'null': 'True', 'to': u"orm['projects.ResearchLine']"})
        },
        u'projects.image': {
            'Meta': {'object_name': 'Image'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'project': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'cover_image'", 'unique': 'True', 'null': 'True', 'to': u"orm['projects.Project']"}),
            'research_line': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'avatar'", 'unique': 'True', 'null': 'True', 'to': u"orm['projects.ResearchLine']"}),
            'section': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'avatar'", 'unique': 'True', 'null': 'True', 'to': u"orm['projects.Section']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'subsection': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'avatar'", 'unique': 'True', 'null': 'True', 'to': u"orm['projects.Subsection']"}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'projects.journalreference': {
            'Meta': {'object_name': 'JournalReference', '_ormbases': [u'projects.Reference']},
            'journal_title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'journal_reference'", 'null': 'True', 'to': u"orm['projects.Project']"}),
            u'reference_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['projects.Reference']", 'unique': 'True', 'primary_key': 'True'}),
            'research_line': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'journal_reference'", 'null': 'True', 'to': u"orm['projects.ResearchLine']"})
        },
        u'projects.project': {
            'Meta': {'object_name': 'Project'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'projects.reference': {
            'Meta': {'object_name': 'Reference'},
            'authors': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pages': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'place_of_pub': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'publisher': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'projects.researchline': {
            'Meta': {'object_name': 'ResearchLine'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'research_lines'", 'null': 'True', 'to': u"orm['projects.Project']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'subtitle': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'projects.section': {
            'Meta': {'object_name': 'Section'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'research_lines': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sections'", 'to': u"orm['projects.ResearchLine']"}),
            'text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'projects.subsection': {
            'Meta': {'object_name': 'Subsection'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'subsections'", 'to': u"orm['projects.Section']"}),
            'text': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['projects']