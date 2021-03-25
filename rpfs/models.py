from django.db import models


class Category(models.Model):
    product_category = models.CharField(max_length=30)

    def __str__(self):
        return self.product_category


class Prouct(models.Model):
    product_name = models.CharField(max_length=50)
    product_description = models.TextField(max_length=500)
    status = models.CharField(max_lenth=50, choices=[('A', 'Active'), ('I', 'Inactive')])
    post_date = models.DateField()
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name

    class Meta:
        ordering = ['product_name']



