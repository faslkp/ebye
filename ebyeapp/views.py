from django.shortcuts import render, get_object_or_404
from .models import *
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, InvalidPage


# Create your views here.
def home(request):
    obj_products = product.objects.all().filter(available=True)
    obj_categories = Categ.objects.all()
    return render(request, 'index.html', {'products': obj_products, 'categories': obj_categories})


def checkout(request):
    return render(request, 'checkout.html')


def detail(request, c_slug, p_slug):
    try:
        prodt = product.objects.get(categ__slug=c_slug, slug=p_slug)
    except Exception as e:
        raise e
    obj_categories = Categ.objects.all()
    return render(request, 'detail.html', {'product': prodt, 'categories': obj_categories})


def category(request, c_slug=None):
    c_page = None
    prodt = None
    if c_slug != None:
        c_page = get_object_or_404(Categ, slug=c_slug)
        prodt = product.objects.filter(categ=c_page, available=True)
    else:
        prodt = product.objects.all().filter(available=True)
    obj_categories = Categ.objects.all()
    paginator = Paginator(prodt, 9)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        pro = paginator.page(page)
    except(EmptyPage, InvalidPage):
        pro = paginator.page(paginator.num_pages)
    return render(request, 'shop.html', {'products': prodt, 'categories': obj_categories, 'pages': pro})


def all_category(request):
    obj_products = product.objects.all()
    obj_categories = Categ.objects.all()
    paginator = Paginator(obj_products, 9)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        pro = paginator.page(page)
    except(EmptyPage, InvalidPage):
        pro = paginator.page(paginator.num_pages)
    return render(request, 'shop.html', {'products': obj_products, 'categories': obj_categories, 'pages': pro})


def searching(request):
    prod = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        prod = product.objects.all().filter(Q(name__contains=query) | Q(desc__contains=query))
    paginator = Paginator(prod, 9)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        pro = paginator.page(page)
    except(EmptyPage, InvalidPage):
        pro = paginator.page(paginator.num_pages)
    obj_categories = Categ.objects.all()
    return render(request, 'shop.html', {'qr': query, 'products': prod, 'categories': obj_categories, 'pages': pro})


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')
