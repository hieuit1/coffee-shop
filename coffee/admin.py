from django.contrib import admin
from .models import Coffee,Cart, CartItem

class CoffeeAdmin(admin.ModelAdmin):
    list_display = ('name','price', 'quantity')


class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0

class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemInline]

admin.site.register(Coffee, CoffeeAdmin)
admin.site.register(Cart, CartAdmin, )

