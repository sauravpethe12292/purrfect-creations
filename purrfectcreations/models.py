from django.db import models

class Order(models.Model):
    order_id = models.CharField(max_length=255)
    order_placed = models.DateField()
    product_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.TextField()
    email = models.EmailField()
    order_status = models.CharField(max_length=255)