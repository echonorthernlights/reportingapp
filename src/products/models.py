from django.db import models


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='products', default='no_image.png')
    price = models.FloatField(help_text="In US dollars")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(f"{self.name}, {self.created.__format__("%d/%m/%Y")}")
