from django.template.response import TemplateResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic.edit import FormView
from django.utils.translation import gettext as _
from django.conf import settings
from django.core.mail import send_mail
from .forms import (
    ContactForm, 
    VolunteerForm
) 
from .models import Category, Product, Post


def categories(request):
    return {
        'categories': Category.objects.all()
    }

def all_products(request):
    products = Product.objects.all()
    post = Post.objects.filter(page='Home')
    return render(request, 'home.html', {'products': products, 'title': _('Home'), 'post': post})

def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'category.html', {'category': category, 'products': products})

#def item_detail(request, slug):
    #product = get_object_or_404(Product, slug=slug, still_avail=True)
    #return render(request, 'items.html', {'product': product})    


class VolunteerSignup(FormView):
    # TODO: you can use this class as a model to add views for other
    # contact forms. 
    form_class = VolunteerForm
    template_name = 'volunteer.html'
    success_url = '/success/' 

    def form_valid(self, form):
        super().form_valid(form)
        return form.send_email()
        
    def get(self, request, *args, **kwargs):
        post = Post.objects.filter(page='volunteer')
        return TemplateResponse(
                   request,
                   'volunteer.html',
                   context={'form': self.form_class(*args, **kwargs),
                       'post': post},
                   status=200)

class ContactUs(FormView):
    # TODO: you can use this class as a model to add views for other
    # contact forms. 
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = '/success/' 

    def form_valid(self, form):
        super().form_valid(form)
        return form.send_email()
        
    def get(self, request, *args, **kwargs):
        return TemplateResponse(
                   request,
                   'contact.html',
                   context={'form': self.form_class(*args, **kwargs)},
                   status=200)

def about(request):
    post = Post.objects.filter(page='about')
    return render(request, 'about.html', {'post': post})    

def successView(request):
    return render(request, 'success.html', {}) 

def items_needed(request):
    post = Post.objects.filter(page='items')
    return render(request, 'items.html', {'post': post})        

#does there not need to be a class here for "Posts?" But there would not be an actual page for it so do I need to define a class regarless of this?


#def some_view(request, *args, **kwargs):
   #post = <...something...>
    #return TemplateResponse(
               #request,
               #'thing.html',
               #context={'post': post}
               #status=200)
