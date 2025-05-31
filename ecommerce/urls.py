
from django.urls import path
from .views import Index,ProductDetail

app_name = 'ecommerce'

urlpatterns = [
    path('',Index.as_view(),name='index'),
    path('category/<slug:category_slug>/',Index.as_view(),name='get_all_products_by_category'),
    path('product/detail/<int:product_id>/',ProductDetail.as_view(),name='product_detail')
]
