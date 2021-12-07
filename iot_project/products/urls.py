from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.home, name='products-home'),
    path('products/about/', views.about, name='products-about'),
]