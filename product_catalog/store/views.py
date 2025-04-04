from django.shortcuts import render
from .models import Category, Tag, Product
# Create your views here.


def product_list(request):

    query = request.GET.get('q', '')
    categoryId = request.GET.get('category')
    tagIds= request.GET.getlist('tags')

    products= Product.objects.all()

    if query:
        products= products.filter(description__icontains= query)

    if categoryId:
        products= products.filter(category_id = categoryId)

    if tagIds:
        products= products.filter(tags__id__in= tagIds).distinct()

    
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

