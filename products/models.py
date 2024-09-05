from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image_url = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

