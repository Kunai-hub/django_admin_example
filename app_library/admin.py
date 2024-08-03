from django.contrib import admin
from app_library.models import Publisher, Author


class PublisherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'city']
    list_filter = ['is_active', 'city']


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name']
    search_fields = ['first_name', 'last_name', 'biography']


admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Author, AuthorAdmin)
