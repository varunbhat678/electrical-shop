from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('Bulbs', 'Bulbs'),
        ('Plugs', 'Plugs'),
        ('Switches', 'Switches'),
        ('Wires', 'Wires'),
        ('Fans', 'Fans'),
        ('MCB', 'MCB'),
        ('Sockets', 'Sockets'),
        ('Holders', 'Holders'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES,default='bulbs')
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name
