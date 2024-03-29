from django.contrib import admin

from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'post_date', 'updated', 'status']
    list_filter = ['status', 'post_date']
    list_editable = ['status']
    prepopulated_fields = {'slug': ('title',)}
