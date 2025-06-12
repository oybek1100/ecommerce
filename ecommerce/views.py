from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView
from django.core.paginator import Paginator
from .models import Category,Product , Customers
import csv, json
from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponse

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
        paginator = Paginator(products,3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'categories':categories,
            'page_obj':page_obj
        }
        if category_slug:
            products = Product.objects.filter(category__slug = category_slug)
            return render(request,'ecommerce/product-list.html',{'products':products})
        
        return render(request,'ecommerce/index.html',context)
      
        
    
    

class ProductDetail(DetailView):
    model = Product
    template_name = 'ecommerce/product-detail.html'   
    pk_url_kwarg = 'product_id'



class CustomerList(View):   
    def get(self, request):
        export_format = request.GET.get('export')

        if export_format == 'csv':
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="customers.csv"'
            writer = csv.writer(response)
            writer.writerow(['full_name', 'email']) 
            for c in Customers.objects.all():
                writer.writerow([c.full_name, c.email])  
            return response

        elif export_format == 'json':
            data = list(Customers.objects.values('full_name', 'email'))
            response = HttpResponse(json.dumps(data, indent=4), content_type='application/json')
            response['Content-Disposition'] = 'attachment; filename="customers.json"'  
            return response

      
        customers = Customers.objects.all()
        return render(request, 'ecommerce/cutomers.html', {'customer': customers})

    def post(self, request):
        file = request.FILES['file']
        format = request.POST['format']

        if format == 'csv':
            decoded = file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded)
            for row in reader:
                Customers.objects.create(**row)

        elif format == 'json':
            data = json.loads(file.read().decode('utf-8'))
            for item in data:
                Customers.objects.create(**item)

        return redirect('customers')