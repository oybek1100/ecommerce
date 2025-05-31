from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView

from .models import Category,Product
# Create your views here.


def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categories':categories,
        'products':products
    }
    return render(request,'ecommerce/index.html',context)


class Index(View):
    def get(self,request,category_slug=None):
        categories = Category.objects.all()
        products = Product.objects.all()
        context = {
            'categories':categories,
            'products':products
        }
        if category_slug:
            products = Product.objects.filter(category__slug = category_slug)
            return render(request,'ecommerce/product-list.html',{'products':products})
        
        return render(request,'ecommerce/index.html',context)
      
        
    
    

class ProductDetail(DetailView):
    model = Product
    template_name = 'ecommerce/product-detail.html'   
    pk_url_kwarg = 'product_id'

