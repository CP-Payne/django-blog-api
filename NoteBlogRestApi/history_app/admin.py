from django.contrib import admin
from .models import *

class PostHistoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'description')
    # list_display_links = ('id', 'title')
    # search_fields = ('title', 'user')
    # list_editable = ('is_public',)

# Register your models here.

admin.site.register(PostHistory, PostHistoryAdmin)
