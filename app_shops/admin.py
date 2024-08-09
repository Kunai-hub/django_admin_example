from django.contrib import admin

from app_shops.models import Shop


class ShopAdmin(admin.ModelAdmin):
    list_display = ['name', 'id']


admin.site.register(Shop, ShopAdmin)
