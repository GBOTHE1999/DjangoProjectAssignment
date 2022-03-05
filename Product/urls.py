from django.contrib import admin
from . import views
from django.urls import path, include
from .views import ProductListView,AddProductView
 
urlpatterns = [
     
   
    path('product-list/',ProductListView, name='product-list'),
path('add_product/', AddProductView.as_view(), name="add_product"),
]
