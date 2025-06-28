from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.utils import timezone
# Create your models here.
class FoodItems(models.Model):
    id=models.AutoField(primary_key=True)
    food_name=models.CharField(blank=False, max_length=50)
    data=models.JSONField()
    image=models.ImageField(upload_to='food_img/',default='food_img/default.jpg')
    isAvailable=models.BooleanField(default=True)
    date=models.DateField(default=date.today)
    count=models.IntegerField(default=0,blank=True)
class UserDetails(models.Model):
    id=models.AutoField(primary_key=True)
    Customer=models.OneToOneField(User,on_delete=models.CASCADE,related_name="user_detail")
    mobile=models.BigIntegerField(blank=True)
class Orders(models.Model):
    id=models.AutoField(primary_key=True)
    Food=models.JSONField()
    Customer=models.ForeignKey(User,on_delete=models.CASCADE,related_name="order_customer")
    cost=models.FloatField()
    instruction=models.TextField(max_length=255,blank=True)
    pick_up_time=models.TimeField(blank=True,default=timezone.now().time())
    status=models.IntegerField(default=1)
    isCompleted=models.BooleanField(default=False)