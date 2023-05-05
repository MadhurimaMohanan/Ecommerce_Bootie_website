from django.db import models

# Create your models here.
class P_admin(models.Model):
    id=models.AutoField(primary_key=True)
    email=models.CharField(max_length=100,default='')
    password=models.CharField(max_length=100,default='')

class P_product(models.Model):
    id=models.AutoField(primary_key=True)
    product_name=models.CharField(max_length=100,default='')
    image=models.FileField(upload_to='image',default='',null=True,blank=True)
    price=models.CharField(max_length=100,default='')

class P_user(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,default='')
    email=models.CharField(max_length=100,default='')
    password=models.CharField(max_length=100,default='')
    phone_no=models.CharField(max_length=100,default='')

class cart(models.Model):
    id=models.AutoField(primary_key=True)
    user = models.ForeignKey(P_user, on_delete=models.CASCADE)
    product = models.ForeignKey(P_product, on_delete=models.CASCADE)