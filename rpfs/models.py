from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField



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

class Page(models.Model):
    title = models.CharField(max_length=255)
    content = HTMLField()

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

    #class Volunteer(models.Model):
     #   VOLUNTEER_POSITIONS = (
            #('a', 'Working at the Free Store location during "closed to public" times (organizing the space, putting supply packages together, etc.)'),
     #       ('b', 'Working at the Free Store location during "open to public" times (handing out requested supplies, helping neighbors make supply requests, etc.)'),
      #      ('c', 'Delivering supplies either from or to the Free Space (will need a car)'),
       #     ('d', 'Volunteer Coordination/Training/Support (can be working from home)'),
        #    ('e', 'Inventory and/or financial book-keeping (can be working from home)'),
         #   ('f', 'Outreach and/or social media (can be working from home)'),
          #  ('g', 'Translation (Spanish, French, Chinese, others if applicable)'),
           # ('h', 'Other'),

       # )
        #position = MultiSelectField(choices = VOLUNTEER_POSITIONS)


#        char = models.CharField(verbose_name="Name", max_length=220, unique=True, help_text="added help text")    
#        email = models.EmailField()
#        subject = models.CharField(max_length=255)
#        message = models.TextField()

#    def __str__(self):
#        return self.email    

class Post(models.Model):
    # we don't allow dynamic page creation.  
    # You don't have to use SlugField, you can use a ChoiceField, 
    # where the choices are a list of the pages. # is the difference then the ability to type the page name in to search for it vs. having a predetermined list to choose from?
        #page = models.ChoiceField(choices=PAGE_CHOICES)
    HOME = 'Home'
    ABOUT = 'About'
    CONTACT = 'Contact'
    VOLUNTEER = 'Volunteer'
    PAGE_CHOICES = [
        (HOME, 'Home'),
        (ABOUT, 'About'),
        (CONTACT, 'Contact'),
        (VOLUNTEER, 'Volunteer'),
    ]
    page = models.CharField(
        max_length=10, 
        choices=PAGE_CHOICES, 
        default=HOME,
    )
    content = models.TextField(
        blank=True,
        null=True,
        default=' ')
    link_text = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    create_date = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)

    def get_absolute_url(self):
        return f'/pages/{self.slug}/'     



