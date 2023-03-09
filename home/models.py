from django.db import models
from django.conf import settings

# Create your models here.

class Order(models.Model):
    table = models.CharField(max_length=100)
    custumer = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.table

class Comment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='comment')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)