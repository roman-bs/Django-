from django.conf import settings
from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
    image = models.ImageField(blank=True, null=True)
    cost = models.IntegerField()


class Purchase(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="purchases", on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product, related_name="purchases", on_delete=models.CASCADE
    )
    count = models.IntegerField()