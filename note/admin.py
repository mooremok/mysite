from django.contrib import admin
from . models import NoteStatus, NoteType, PDVersion, Note
# Register your models here.

@admin.register(NoteStatus)
class NoteStatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'notestatus')

@admin.register(NoteType)
class NoteTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'notetype')

@admin.register(PDVersion)
class PDVersionAdmin(admin.ModelAdmin):
    list_display = ('pdversion', )

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'notetype', 'pdversion', 'notestatus', 'erinfo', 'created_time', 'views')
    list_display_links = ('id', 'title')