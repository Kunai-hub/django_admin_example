from django.contrib import admin

from app_goods.models import Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'weight']


admin.site.register(Item, ItemAdmin)
