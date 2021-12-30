from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

# Create your views here.
from products.models import Product, ProductReal
from questions.models import Question


def index(request):
    page = request.GET.get('page', '1')  # GET방식으로 호출 된 url에서 page값을 가져온다.(defult값은 1로 설정한다.)

    product_list = Product.objects.all().order_by('-id')

    paginator = Paginator(product_list, 8)  # Paginator 클래스 사용, 한 페이지당 5개씩 보여주기
    page_obj = paginator.get_page(page)  # 요청된 page에 해당되는 객체를 page_obj에 담는다.

    context = {'product_list': page_obj}
    return render(request, 'products/product_list.html', context)


def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    product_real_list = ProductReal.objects.filter(product=product)
    question_list = Question.objects.filter(
        content_type=ContentType.objects.get(app_label='products', model='product')).filter(
        object_id=product_id)
    context = {'product': product,
               'question_list': question_list,
               'product_real_list': product_real_list}
    return render(request, 'products/product_detail.html', context)


def search(request):
    product_list = Product.objects.all()
    q = request.GET.get('q', '')
    product_list = product_list.filter(display_name__icontains=q)
    context = {'product_list': product_list, 'q': q}
    return render(request, 'products/product_list.html', context)
