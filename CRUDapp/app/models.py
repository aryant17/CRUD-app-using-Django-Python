from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Customer(models.Model):
    customer_name = models.CharField(max_length=200);
    customer_phoneno = models.CharField(max_length=200, null=True);
    customer_email = models.EmailField(max_length=200, null=True);
    date_created = models.DateTimeField(auto_now_add=True);

    def __str__(self):
        return self.customer_name

class tag(models.Model):
    tagschoices = (
        ('OutDoor','OutDoor'),
        ('InDoors','InDoors'),
        ('Appliances','Appliances'),
        ('Phones', 'Phones'),
        ('Electronics', 'Electronics'),
        ('Laptops', 'Laptops'),
    )
    tag_name = models.CharField(max_length=200, null=True, choices=tagschoices);

    def __str__(self):
        return self.tag_name

class Product(models.Model):
    product_category = (
        ('Tools', 'Tools'),
        ('Electronic', 'Electronic'),
        ('Books', 'Books'),
        ('Furniture', 'Furniture')
    )
    product_name = models.CharField(max_length=200, null=False);
    product_price = models.FloatField(max_length=1000000, null=True);
    category = models.CharField(max_length=200, choices=product_category);
    date_created = models.DateTimeField(auto_now_add=True);

    def __str__(self):
        return self.product_name

class Order(models.Model):

    Status = (
        ('Pending', 'Pending'),
        ('Out for Delivery', 'Out for Delivery'),
        ('Delivered', 'Delivered'),
    )
    
    customer_name = models.ForeignKey(Customer , null=True, on_delete=models.SET_NULL);
    order_status = models.CharField(max_length=200, choices=Status);
    products = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL);
    date_created = models.DateTimeField(auto_now_add=True);
    

