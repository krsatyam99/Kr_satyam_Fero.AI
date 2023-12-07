from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'weight')
    ordering = ('id',)  
admin.site.register(Product, ProductAdmin)



class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'contact_number')
    ordering = ('id',)  
admin.site.register(Customer, CustomerAdmin)



class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_number', 'customer','order_date','address')
    ordering = ('id',)  
admin.site.register(Order, OrderAdmin)


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product','quantity')
    ordering = ('id',)  
admin.site.register(OrderItem, OrderItemAdmin)
