from django.contrib import admin
from .models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'display_categories',
        'price',
        'rating',
        'image',
    )

    def display_categories(self, obj):
        # Return a comma-separated list of related category names
        return ', '.join([category.name for category in obj.category.all()])

    display_categories.short_description = 'Categories'  # Adjusts the display name for the admin column

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('friendly_name', 'name')  # Standard list display for Category model

# Register the models with their respective admin classes
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
