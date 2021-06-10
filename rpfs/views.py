from django.http import TemplateResponse
from django.shortcuts import get_object_or_404, render
from django.views.generics import FormView

from .forms import CaptchaContactForm
from .models import Category, Product


def categories(request):
    return {
        'categories': Category.objects.all()
    }

def all_products(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'category.html', {'category': category, 'products': products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, still_avail=True)
    return render(request, 'detail.html', {'product': product})    


class VolunteerSignup(FormView):
    # TODO: you can use this class as a model to add views for other
    # contact forms. 
    form_class = CaptchaContactForm
    template_name = 'volunteer.html'
    success_url = '/thanks/' # TODO: this view/url doesn't exist yet... 
    # we need a view/template/route for it... a function-based view is fine.

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        return TemplateResponse(
                   request,
                   'volunteer.html',
                   context={'form': self.form_class()},
                   status=200)
