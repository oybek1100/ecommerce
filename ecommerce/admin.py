from django.contrib import admin
from .models import Category, Product, Image, AttributeKey, AttributeValue, Attribute , Customers
from import_export.admin import ImportExportModelAdmin
# Register your models here.

# admin.site.register(Category)


admin.site.register(Product)
admin.site.register(Image)
admin.site.register(AttributeKey)
admin.site.register(AttributeValue)
admin.site.register(Attribute)
admin.site.register(Customers)

@admin.register(Category)
class CategoryAdmin( ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['title','image','slug']
    
    prepopulated_fields = {"slug": ("title",)}