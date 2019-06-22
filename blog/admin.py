from django.contrib import admin
from . models import Tags, Category, Blog
# Register your models here.

@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
    list_display_links = ('id', 'name')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
    list_display_links = ('id', 'name')
    search_fields = ('name',)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'category', 'created_time', 'views', 'show_tags')
    readonly_fields = ('views',)
    list_display_links = ('id','title')
    list_filter = ['category', 'created_time',]
    list_per_page = 20
    search_fields = ['title', 'content']
    raw_id_fields = ('category','tag')
    filter_horizontal = ['tag', ]
    list_editable = ['views']
    ordering = ['-created_time', 'category','title']
    autocomplete_fields = ['category']

    def show_tags(self, obj):
        tag_list = []
        for tag in obj.tag.all():
            tag_list.append(tag.name)
        return '、'.join(tag_list)

    show_tags.short_description = '标签'