from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cart/checkout', views.checkout, name='checkout'),
    path('<slug:c_slug>/<slug:p_slug>', views.detail, name='details'),
    path('<slug:c_slug>/', views.category, name='category'),
    path('all-category', views.all_category, name='all-category'),
    path('search', views.searching, name='search'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register')
]
