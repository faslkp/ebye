from django.urls import path
from . import views

urlpatterns = [
    path('cart', views.cart, name='cart'),
    path('add/<int:product_id>/', views.add_to_cart, name='addcart'),
    path('dec/<int:product_id>/', views.cart_decrement, name='cart_decrement'),
    path('del/<int:product_id>/', views.cart_delete, name='cart_delete'),
]