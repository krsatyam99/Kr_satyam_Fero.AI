from rest_framework import serializers
from .models import Customer, Product, Order, OrderItem
from django.utils import timezone
from .models import Order, OrderItem


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

        def validate_name(self, value):
        # Check if a customer with the same name already exists
            existing_customer = Customer.objects.filter(name__iexact=value).first()

            # If updating an existing instance, make sure it's not the current instance
            if existing_customer and getattr(self, 'instance', None) and existing_customer != self.instance:
                raise serializers.ValidationError("Customer with this name already exists.")

            return value



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def validate_name(self, value):
        # Check if a product with the same name already exists
        existing_product = Product.objects.filter(name__iexact=value).first()

        # If updating an existing instance, make sure it's not the current instance
        if existing_product and existing_product != getattr(self, 'instance', None):
            raise serializers.ValidationError("Product with this name already exists.")

        return value

    def validate_weight(self, value):
        if value <= 0 or value > 25:
            raise serializers.ValidationError("Weight must be a positive decimal not exceeding 25kg.")
        return value








class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    orderitem_set = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'customer', 'order_date', 'address', 'orderitem_set']

    def validate_order_date(self, value):
        """
        Validate that the order date is not in the past.
        """
        if value < timezone.now().date():
            raise serializers.ValidationError("Order date cannot be in the past.")
        return value

    def validate(self, data):
        """
        Validate the cumulative weight of the order.
        """
        orderitems_data = data.get('orderitem_set', [])
        cumulative_weight = sum(item['quantity'] * item['product'].weight for item in orderitems_data)

        if cumulative_weight > 150:
            raise serializers.ValidationError("Cumulative weight of the order items cannot exceed 150kg.")

        return data

    def create(self, validated_data):
        orderitems_data = validated_data.pop('orderitem_set')
        order = Order.objects.create(**validated_data)
        
        for orderitem_data in orderitems_data:
            OrderItem.objects.create(order=order, **orderitem_data)

        return order

    def update(self, instance, validated_data):
        instance.customer = validated_data.get('customer', instance.customer)
        instance.order_date = validated_data.get('order_date', instance.order_date)
        instance.address = validated_data.get('address', instance.address)

        # Update order items
        orderitems_data = validated_data.get('orderitem_set', [])
        existing_orderitems = instance.orderitem_set.all()

        for orderitem_data in orderitems_data:
            orderitem_id = orderitem_data.get('id', None)
            if orderitem_id:
                # Update existing order item
                orderitem = OrderItem.objects.get(id=orderitem_id, order=instance)
                orderitem.product = orderitem_data.get('product', orderitem.product)
                orderitem.quantity = orderitem_data.get('quantity', orderitem.quantity)
                orderitem.save()
            else:
                # Create new order item
                OrderItem.objects.create(order=instance, **orderitem_data)

        return instance
