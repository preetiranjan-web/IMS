from django.db import models

# Create your models here.
class ProductModel(models.Model):
    carmodel=models.CharField(max_length=100)
    variant=models.CharField(max_length=100)
    mdate=models.DateField()
    car_serial_no=models.AutoField(primary_key=True)
    chasis_no=models.IntegerField(unique=True)
    engine_no = models.IntegerField(unique=True)
    status = models.CharField(max_length=100,default="active")


class OrderModel(models.Model):
    shipping_date = models.DateField()
    track_id = models.AutoField(primary_key=True)
    product=models.ForeignKey(ProductModel,on_delete=models.CASCADE)

