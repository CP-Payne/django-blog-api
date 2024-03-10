from django.contrib import admin
from .models import *
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'created_at', 'is_public')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'user')
    list_editable = ('is_public',)

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(BlogTag)
admin.site.register(Image)
