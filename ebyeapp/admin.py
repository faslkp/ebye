from django.contrib import admin
from .models import *


# Register your models here.

class CategAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'priority']
    list_editable = ['priority']


admin.site.register(Categ, CategAdmin)


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'mrp', 'price', 'stock', 'available', 'categ']
    list_editable = ['mrp', 'price', 'stock', 'available']


admin.site.register(product, ProductAdmin)
