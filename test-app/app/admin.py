from django.contrib import admin
from .models import Category, Subcategory, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    llist_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    
@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'category',)
    prepopulated_fields = {'slug': ('name',)}
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'category', 'subcategory',)
    prepopulated_fields = {'slug': ('name',)}
    
