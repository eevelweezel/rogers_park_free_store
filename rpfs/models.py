# Here was one attempt but I went back and did the others below it once we spoke. Still sending you my initial confusion fort clarity

from django.db import models
from datetime import datetime


class ProductCategory(models.Model):
    product_category = models.Charfield(max_Length=200)
    category_summary = models.Textfield(max_Length=500)
    category_slug = models.Charfield(max_Length=200)

    class Meta:
        verbose_name_plural = "Categories"

        def __str__)

            self:
        return self.product_category


class ProductDescription(model.Models):
    product_description = models.TextField(max_Length=500)
    product_category = models.ForeignKey(ProductCategory, default=1, verbose_name="Category", on
    delete = models.SET_DEFAULT)
    product_title = models.CharField(max_Length=100)

    class Meta:
        verbose_name_plural = "Title"

        def __str__)

            self:
        return self.product_title


# Should this actually be labled "Product Description"? Or flip (or delete) the code for "Product Title" with "Project Description"?
class ProductTitle(model.Model):
    product_title = models.CharField(max_Length=100)
    product_description = models.TextField(max_Length=500)
    # product_status = models.???
    # product_neighborhood =
    product_dateposted
    models.DateTimeField("date posted", default=datetime.now())

    # Do I need to have another copy of the below code in order to tie product title
    product_categtory = models.ForeignKey(ProductCategory, default=1, verbose_name="Category", on
    delete = models.SET_DEFAULT)
    product_slug = = models.CharField(max_Length=200, default=1)

    def __str__(self):
        return self.product_description


# ORIGINAL VERSION >>>
from django.db import models


class Category(models.Model):
    product_category = models.CharField(max_length=30)

    # Not sure how to modify the below 2 lines of code
    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Prouct(models.Model):
    product_name = models.CharField(max_length=50)
    product_description = models.TextField(max_length=500)
    # status = models.??? ()
    post_date = models.DateField()
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name

    class Meta:
        ordering = ['product_name']

    # Next is where they lost me as I am not quite sure how to "save" and test these various models yet; copied and pasted all:

>> > c = Category(product_category='household goods')
>> > c.save()

>> > c2 = Category(product_category='clothing & shoes')
>> > c2.save()

>> > c3 = Category(product_category='electronics')
>> > c3.save()

>> > c4 = Category(product_category='toys')
>> > c4.save()

>> > c5 = Category(product_category='furniture')
>> > c5.save()

