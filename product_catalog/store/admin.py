from django.contrib import admin
from .models import Category, Tag, Product

# Register your models here.

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Product)

