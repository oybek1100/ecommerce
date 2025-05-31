from django.contrib import admin
from .models import Category,Product,Image
# Register your models here.

# admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Image)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','image','slug']
    
    prepopulated_fields = {"slug": ("title",)}