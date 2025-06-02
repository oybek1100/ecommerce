from django.contrib import admin
from .models import Category, Product, Image, AttributeKey, AttributeValue, Attribute
# Register your models here.

# admin.site.register(Category)


admin.site.register(Product)
admin.site.register(Image)
admin.site.register(AttributeKey)
admin.site.register(AttributeValue)
admin.site.register(Attribute)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','image','slug']
    
    prepopulated_fields = {"slug": ("title",)}