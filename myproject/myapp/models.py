from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

class Product_list(models.Model):
    types = (
        ("14", "iPhone 14"),
        ("14+", "iPhone 14 Plus"),
        ("14P", "iPhone 14 Pro"),
        ("14PM", "iPhone 14 Pro Max"),
        )

    name = models.CharField(max_length=50)
    presub = models.CharField(max_length=30, null=True, blank=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    type_product = models.CharField(max_length=4, choices=types)
    price = models.IntegerField()
    image=models.ImageField(upload_to='product_images')
    def __str__(self):
        return "%s"%(self.name)

class customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,default=None)
    email = models.EmailField()
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=11, blank=True)
    surname = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, default="N")
    country = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    joined_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Transaction(models.Model):
    customer = models.ForeignKey(customer, on_delete=models.SET_NULL, default=None, blank=True, null=True)
    transaction = models.CharField(max_length=50)
    total = models.PositiveIntegerField(default=0)
    stats = models.PositiveIntegerField(default=0)
    image = models.ImageField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.transaction

class Order(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    product = models.ForeignKey(Product_list, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return "ID:%s Quantity: %s name: %s"%(self.transaction, self.quantity, self.product)

class Report_issue(models.Model):
    email = models.CharField(max_length=100)
    problem = models.CharField(max_length=200)
    product_id = models.CharField(max_length=10)
    info = models.CharField(max_length=1000)

    def __str__(self):
        return self.problem