from django.shortcuts import render
from .models import Product 
from django.views.generic import  CreateView 
from .forms import  ProductForm
 
def ProductListView(request):
    product_menu_list = Product.objects.all()
    return render(request, 'Product/ProductView.html', {'product_menu_list': product_menu_list})
# Create your views here.

class AddProductView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'Product/add_product_view.html'
