from django.db import models

# Create your models here.
class Product(models.Model):

    name = models.CharField(max_length=150, blank=True)
    # price is the one who the client pays
    price = models.FloatField()
    # cost is the one who the providers gives to the store
    cost = models.FloatField()
    store = models.ForeignKey("stores.Store", on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name