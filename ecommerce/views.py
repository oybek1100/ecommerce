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


from django.views import View
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Customers
import csv, json

class CustomerList(View):
    def get(self, request):
        export_format = request.GET.get('export')

        if export_format == 'csv':
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="customers.csv"'
            writer = csv.writer(response)
            writer.writerow(['full_name', 'email', 'phone', 'address']) 
            for c in Customers.objects.all():
                writer.writerow([c.full_name, c.email, c.phone, c.address])
            return response

        elif export_format == 'json':
            data = list(Customers.objects.values('full_name', 'email', 'phone', 'address'))
            return HttpResponse(json.dumps(data, indent=4), content_type='application/json')

        customers = Customers.objects.all()
        return render(request, 'ecommerce/cutomers.html', {'customer': customers})

    def post(self, request):
        file = request.FILES['file']
        format = request.POST['format']

        if format == 'csv':
            decoded = file.read().decode('utf-8').splitlines()
            reader = csv.DictReader(decoded)
            for row in reader:
                full_name = row.get('full_name', '').strip()
                email = row.get('email', '').strip()
                phone = row.get('phone', '').strip()
                address = row.get('address', '').strip()

                if not email or not phone:
                    continue  

                try:
                    Customers.objects.update_or_create(
                        email=email,
                        defaults={
                            'full_name': full_name,
                            'phone': phone,
                            'address': address or None
                        }
                    )
                except KeyError:
                    continue

        elif format == 'json':
            try:
                data = json.loads(file.read().decode('utf-8'))
                for item in data:
                    full_name = item.get('full_name', '').strip()
                    email = item.get('email', '').strip()
                    phone = item.get('phone', '').strip()
                    address = item.get('address', '').strip() if item.get('address') else None

                    if not email or not phone:
                        continue

                    try:
                        Customers.objects.update_or_create(
                            email=email,
                            defaults={
                                'full_name': full_name,
                                'phone': phone,
                                'address': address
                            }
                        )
                    except KeyError:
                        continue
            except json.JSONDecodeError:
                return HttpResponse("❌ err ", status=400)

        return redirect('customers')