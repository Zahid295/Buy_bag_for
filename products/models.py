from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image_url = models.CharField(max_length=255, blank=True, null=True)
    stock = models.IntegerField(default=0) 

    def __str__(self):
        return self.name


    def is_in_stock(self):
        """Check if the product is in stock."""
        return self.stock > 0
