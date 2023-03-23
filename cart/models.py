from django.db import models
from ebyeapp.models import *

# Create your models here.
class cartlist(models.Model):
    cart_id = models.CharField(max_length=250, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cart_id


class CartItems(models.Model):
    item = models.ForeignKey(product, on_delete=models.CASCADE)
    cart = models.ForeignKey(cartlist, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    # def __str__(self):
    #     return self.item

    def subtotal(self):
        return self.item.price*self.quantity
