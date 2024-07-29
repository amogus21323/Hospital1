from django.contrib import admin

from product.models import Product

admin.site.register(Product)
# Register your models here.
# @admin.register(Product)



# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('name', 'slug')
#     ordering = ('name',)

#     def get_prepopulated_fields(self, request, obj=None):
#         return {'slug': ('name',)}
# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     list_display = (
#         'title',
#         'brand',
#         'price',
#         'available',
#         'created_at',
#         'updated_at',
#     )
#     list_filter = ('available', 'created_at', 'updated_at')
#     ordering = ('title',)
#
#
#     def get_prepopulated_fields(self, request, obj=None):
#         return {
#             'slug': ('title',)
#         }