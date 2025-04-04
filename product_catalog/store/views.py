from django.shortcuts import render
from .models import Category, Tag, Product


def product_list(request):


    '''
    View to dispplay and filter out products based on search query, catefory and tags.
    - Product Search based off name
    - Filter by Category
    - Filter by multiple tags
    '''

    # Get query parameters from URL
    query = request.GET.get('q', '')
    categoryId = request.GET.get('category')
    tagIds= request.GET.getlist('tags')

    # Fetch all products initially
    products= Product.objects.all()

    # For search filter
    if query:
        products= products.filter(description__icontains= query)

    # For filtering by category
    if categoryId:
        products= products.filter(category_id = categoryId)

    # For filtering by multiple tags
    if tagIds:
        products= products.filter(tags__id__in= tagIds).distinct()

    
    # Fetch categories and tags based off filter
    categories = Category.objects.all()
    tags= Tag.objects.all()

    return render(request, 'store/products.html', {
        'products': products,
        'categories': categories,
        'tags': tags,
        'query':query,
        'selected_category': categoryId,
        'selected_tags': tagIds
    })

