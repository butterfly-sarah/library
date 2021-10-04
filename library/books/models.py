from django.db import models
from datetime import datetime,date,timedelta
from django.utils import timezone

# Create your models here.
class catagory(models.Model):
    name=models.CharField(max_length=100)
    img=models.CharField(max_length=300)
    def __str__(self):
        return self.name
class book(models.Model):
    name=models.CharField(max_length=100)
    img=models.CharField(max_length=100)
    disc=models.CharField(max_length=200)
    price = models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    catagory = models.ForeignKey(catagory, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class student(models.Model):
    name=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    img = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class adminn(models.Model):
    name=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    img = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class burrowedbook(models.Model):
    name=models.CharField(max_length=100)
    img=models.CharField(max_length=100)
    disc=models.CharField(max_length=200)
    price = models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    returntime=models.DateField(default=datetime.now()+timedelta(days=3))
    num=models.FloatField()
    catagory = models.ForeignKey(catagory, on_delete=models.CASCADE)
    def __str__(self):
        return self.name