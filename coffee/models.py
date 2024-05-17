from django.db import models
from django.contrib.auth.models import User

class Coffee(models.Model) : 
    name = models.CharField(max_length=255)
    price = models.FloatField()
    quantity = models.IntegerField()
    image = models.CharField(max_length=2083)


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Coffee, through='CartItem')

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    coffee = models.ForeignKey(Coffee, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

