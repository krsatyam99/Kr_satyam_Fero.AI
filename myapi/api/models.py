from django.db import models
from django.db import IntegrityError




class Customer(models.Model):
    name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    weight = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Order(models.Model):
    order_number = models.CharField(max_length=10, unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateField()
    address = models.CharField(max_length=255)

   
    def save(self, *args, **kwargs):
        # Auto-generate order number with prefix ORD and sequential number
        if not self.order_number:
            last_order = Order.objects.order_by('-id').first()
            if last_order:
                last_number = int(last_order.order_number[3:])  # Extract the numeric part
                new_number = last_number + 1
            else:
                new_number = 1

            self.order_number = f'ORD{new_number:05d}'

            try:
                # Try to save the order
                super().save(*args, **kwargs)
            except IntegrityError:
                # If a IntegrityError occurs (order_number is not unique), generate a new one
                while True:
                    new_number += 1
                    self.order_number = f'ORD{new_number:05d}'
                    try:
                        super().save(*args, **kwargs)
                        break
                    except IntegrityError:
                        pass
        else:
            super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product.name} - {self.quantity} units"
