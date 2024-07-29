from django.db import models

# Create your models here.
class Product(models.Model):
    CATEGORY_CHOICES = (
        ('Mens', 'Mens'),
        ('Kids', 'Kids'),
    )
    product_id = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=200)
    price = models.FloatField(blank=True, null=True)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    color = models.CharField(max_length=100, blank=True)
    packing = models.CharField(max_length=100, blank=True)
    sizes = models.TextField(blank=True)      
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    main_image = models.ImageField(upload_to='products/')
    image_1 = models.ImageField(upload_to='products/', blank=True, null=True)
    image_2 = models.ImageField(upload_to='products/', blank=True, null=True)
    image_3 = models.ImageField(upload_to='products/', blank=True, null=True)
    image_4 = models.ImageField(upload_to='products/', blank=True, null=True)
    priority = models.IntegerField(default=0)

    def __str__(self):
        return self.title

