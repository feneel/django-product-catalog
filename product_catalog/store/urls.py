from django.urls import path
from .views import product_list


# Home page for products list with filters
urlpatterns = [
    path('', product_list, name='product_list')
]
