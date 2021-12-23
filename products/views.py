from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, get_object_or_404

# Create your views here.
from products.models import Product
from questions.models import Question


def index(request):
    product_list = Product.objects.all()
    context = {'product_list': product_list}
    return render(request, 'products/product_list.html', context)


def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {'product': product,
               'question_list': Question.objects.filter(
                   content_type=ContentType.objects.get(app_label='products', model='product')).filter(
                   object_id=product_id)}
    return render(request, 'products/product_detail.html', context)
