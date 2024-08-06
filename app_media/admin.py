from django.contrib import admin

from app_media.models import File


class FileAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'file')


admin.site.register(File, FileAdmin)
