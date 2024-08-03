from django.contrib import admin
from app_library.models import Publisher, Author, Book


class BookInLine(admin.StackedInline):
    model = Book


class PublisherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'city']
    list_filter = ['is_active', 'city']
    inlines = [BookInLine]


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name']
    search_fields = ['first_name', 'last_name', 'biography']
    fieldsets = (
        ('Основные сведения', {
            'fields': ('first_name', 'last_name', 'second_name', 'country', 'city')
        }),
        ('Биографические данные', {
            'fields': ('university', 'birth_date', 'biography'),
            'description': 'Данные из биографии автора',
            'classes': ['collapse']
        }),
        ('Контакты', {
            'fields': ('email', 'phone', 'facebook', 'twitter', 'personal_page'),
            'description': 'Контактные данные автора'
        })
    )


class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'publisher']


admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
