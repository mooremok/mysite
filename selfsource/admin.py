from django.contrib import admin
from .models import Book, TecBlog, Collection
# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'lang', 'suit')

@admin.register(TecBlog)
class TecBlogAdmin(admin.ModelAdmin):
    list_display = ('site', 'site_url')

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'site_url', 'coll_time', 'text')