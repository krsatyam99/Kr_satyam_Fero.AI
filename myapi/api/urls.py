from django.urls import path
from .views import *

urlpatterns = [
    path('products/', CreateProduct.as_view(), name='product-create'),
    path('detail_products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('list_products/', AllProductlist.as_view(), name='product-list'),



    path('customers/', AllCustomerList.as_view(), name='customer-list'),
    path('customers/create/', Createcustomer.as_view(), name='customer-create'),
    path('customers/<int:pk>/', CustomerUpdate.as_view(), name='customer-update'),



    path('orders/', Createorder.as_view(), name='order-list-create'),
    path('allorders/', ListOrders.as_view(), name='order-list'),
    path('name_wise_orders/', OrderListByCustomerView.as_view(), name='order-list-name'),
    path('product_wise_orders/', OrderListByProductView.as_view(), name='order-list-product'),
    path('updateorder/<int:pk>/', OrderDetailView.as_view(), name='update-order'),








]