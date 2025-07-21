from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Item(models.Model):

    def __str__(self):
        #print("in define")
        return f"{self.item_name} {self.item_desc} {self.item_price}"

    user_id=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    item_name=models.CharField(max_length=100)
    item_desc=models.CharField(max_length=200)
    item_price=models.IntegerField()
    item_image=models.CharField(max_length=500,default="https://static.vecteezy.com/system/resources/previews/003/170/825/original/isolated-food-plate-fork-and-spoon-design-free-vector.jpg")

class Restaurant(models.Model):
    rest_name=models.CharField(max_length=100)
    rest_addrs=models.CharField(max_length=200)
    rest_rating=models.FloatField()


