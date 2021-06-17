from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(is_active=True)

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255,unique=True)

    class Meta:
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)        
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(max_length=255)
    status = models.CharField(max_length=50, choices=[('A', 'Active'), ('I', 'Inactive')])
    post_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ['title']
     
    def __str__(self):
        return self.title

#    class Contact(models.Model):
#        char = models.CharField(verbose_name="Name", max_length=220, unique=True, help_text="added help text")    
#        email = models.EmailField()
#        subject = models.CharField(max_length=255)
#        message = models.TextField()

#    def __str__(self):
#        return self.email    

      



