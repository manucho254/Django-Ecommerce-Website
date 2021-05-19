from io import BytesIO
from PIL import Image
from django.db import models
from django.shortcuts import reverse
from django.core.files import File
from vendor.models import Vendor

class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200)
    ordering = models.IntegerField(default=0)

    class Meta:
        ordering = ['ordering']

    def __str__(self):
        return self.title

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, related_name='products', on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True) 
    product_image = models.ImageField(upload_to='media/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='media/', blank=True, null=True)

    class Meta:
        ordering = ["-date_added"]

    def __str__(self):
        return self.title

    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.product_image:
                self.thumbnail = self.make_thumbnail(self.product_image)
                self.save()
                return self.thumbnail.url
            else:
                return 'https://via.placeholder.com/240px180.jpg'

    def make_thumbnail(self, product_image, size=(300, 200)):
        img = Image.open(product_image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io , 'JPEG', quality=85)
        thumbnail = File(thumb_io, name=product_image.name)

        return thumbnail
        


    
