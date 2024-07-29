from django.contrib import admin
from .models import OrderStatus,Order,OrderItems

admin.site.register(OrderItems)
admin.site.register(Order)



# Register your models here.
