from django.contrib import admin
from .models import Item, Menu


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'menu')


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', )
