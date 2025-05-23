from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('staff', 'Staff'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='staff')

    def __str__(self):
        return self.username
    
class Product(models.Model):
    product_id=models.AutoField(primary_key=True)
    product_name=models.CharField(max_length=50)
    product_img=models.ImageField(upload_to="Product")
    product_price=models.IntegerField()
    product_category=models.ForeignKey('Category',on_delete=models.CASCADE)


class Category(models.Model):
    category_id=models.AutoField(primary_key=True)
    cate_name=models.CharField(max_length=50)
    location=models.ForeignKey('Location',on_delete=models.CASCADE)

class Location(models.Model):
    location_id=models.AutoField(primary_key=True)
    location_address=models.CharField(max_length=50)


class Stock(models.Model):
    stock_id=models.AutoField(primary_key=True)
    pro_name=models.ForeignKey(Product,on_delete=models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    loc=models.ForeignKey(Location,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    updated_at=models.DateTimeField(auto_now_add=True)

class Supplier(models.Model):
    supplier_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=100)
    address=models.CharField(max_length=50)

class PurchaseOrder(models.Model):
    purchaseorder=models.AutoField(primary_key=True)
    supplier=models.ForeignKey(Supplier,on_delete=models.CASCADE)
    order_date=models.DateField(auto_now_add=True)    
    expected_arrival=models.DateField(null=True, blank=True)
    status=models.CharField(max_length=50,choices=[('pending', 'Pending'), ('received', 'Received')])

class StockTransaction(models.Model):
    stocktransaction=models.AutoField(primary_key=True)
    TRANSACTION_TYPES = [
        ('IN', 'Stock In'),
        ('OUT', 'Stock Out'),
        ('TRANSFER', 'Transfer'),
    ]

    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    warehouse = models.ForeignKey(Location, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    note = models.TextField(blank=True)

