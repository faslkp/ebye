from .models import *
from .views import *


def count(request):
    item_count = 0
    if 'admin' in request.path:
        return {}
    else:
        try:
            ct = cartlist.objects.filter(cart_id=cart_idx(request))
            cti = CartItems.objects.all().filter(cart=ct[:1])
            for c in cti:
                item_count += c.quantity
        except cartlist.DoesNotExist:
            item_count = 0
        return dict(cart_count=item_count)
