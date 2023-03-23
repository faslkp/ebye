from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(cartlist)


class CartAdmin(admin.ModelAdmin):
    list_display = ['item', 'quantity']
    list_editable = ['quantity']


admin.site.register(CartItems, CartAdmin)
