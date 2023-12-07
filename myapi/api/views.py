from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework import filters
from rest_framework import generics
from .models import *
from .serializers import *




############################## Product Apis #####################

class CreateProduct(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveAPIView):  # Extra api For having details about a particular Product.
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class AllProductlist(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer




############################### Customer Apis #########################


class AllCustomerList(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class Createcustomer(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerUpdate(generics.UpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer



####################### Order Apis ###################################


class Createorder(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class ListOrders(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderListByCustomerView(generics.ListAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        customer_name = self.request.query_params.get('customer', None)
        if customer_name:
            # Filter orders based on the customer's name
            return Order.objects.filter(customer__name__iexact=customer_name)
        return Order.objects.all()
    
class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderListByProductView(generics.ListAPIView):
    serializer_class = OrderSerializer

  
    def get_queryset(self):
        products = self.request.query_params.get('products', None)
        if products:
            product_list = products.split(',')
            # Use double underscores to traverse the relationship from Order to OrderItem to Product
            return Order.objects.filter(orderitem__product__name__in=product_list)
        return Order.objects.all()