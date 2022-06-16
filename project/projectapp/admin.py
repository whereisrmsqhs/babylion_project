from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import Item

class PostAdmin(AdminVideoMixin, admin.ModelAdmin):
    list_display = ('title', 'video')

admin.site.register(Item, PostAdmin)