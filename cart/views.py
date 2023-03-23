from django.shortcuts import render, redirect, get_object_or_404
from ebyeapp.models import *
from .models import *
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def cart(request, total=0, count=0, cart_items=None, shipcharge=0, inclship=0):
    try:
        ct = cartlist.objects.get(cart_id=cart_idx(request))
        ct_items = CartItems.objects.filter(cart=ct)
        for i in ct_items:
            total += i.item.price * i.quantity
            if total < 500:
                shipcharge = 40
                inclship = total + shipcharge
            else:
                shipcharge = 0
                inclship = total
            count += i.quantity
    except ObjectDoesNotExist:
        pass
    return render(request, 'cart.html',
                  {'ct_items': ct_items, 'total': total, 'shipcharge': shipcharge, 'inclship': inclship,
                   'count': count})


def cart_idx(request):
    ct_id = request.session.session_key
    if not ct_id:
        ct_id = request.session.create()
    return ct_id


def add_to_cart(request, product_id):
    prod = product.objects.get(id=product_id)
    try:
        ct = cartlist.objects.get(cart_id=cart_idx(request))
    except cartlist.DoesNotExist:
        ct = cartlist.objects.create(cart_id=cart_idx(request))
        ct.save()
    try:
        c_items = CartItems.objects.get(item=prod, cart=ct)
        if c_items.quantity < c_items.item.stock:
            c_items.quantity += 1
        c_items.save()
    except CartItems.DoesNotExist:
        c_items = CartItems.objects.create(item=prod, quantity=1, cart=ct)
        c_items.save()
    return redirect('cart')


def cart_decrement(request, product_id):
    ct = cartlist.objects.get(cart_id=cart_idx(request))
    prod = get_object_or_404(product, id=product_id)
    c_item = CartItems.objects.get(item=prod, cart=ct)
    if c_item.quantity > 1:
        c_item.quantity -= 1
        c_item.save()
    else:
        c_item.delete()
    return redirect('cart')


def cart_delete(request, product_id):
    ct = cartlist.objects.get(cart_id=cart_idx(request))
    prod = get_object_or_404(product, id=product_id)
    c_item = CartItems.objects.get(item=prod, cart=ct)
    c_item.delete()
    return redirect('cart')
