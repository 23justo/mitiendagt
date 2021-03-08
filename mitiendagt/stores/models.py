from django.db import models
# Create your models here.

class Store(models.Model):

    name = models.CharField(max_length=150, blank=True)
    address = models.CharField(max_length=250, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
