from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.shortcuts import get_object_or_404, render
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
    product = get_object_or_404(Product, slug=slug, active=True)
    return render(request, 'rpfs/products/detail.html', {'product': product})   

def home(request):
    return render(request, 'home.html', {})  

def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "email.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')

#def contact(request): 
    #if request.method == "POST":
        #message_name = request.POST['message-name']
        #message_subject = request.POST['message-subject']
        #message_email = request.POST['message-email']
        #message = = request.POST['message']

        # send an email 
        #send_mail(
            #'message_name', # subject
            #message, # message
            #message_email, # from email
            #[rfps@email,com], #To Email

        )

        #return render(request, 'contact.html', {'message_name'})
    #else:
        #return render(request, 'contact.html', {})   

def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "email.html", {'form': form})              

def volunteer(request): 
    if request.method == "POST":
        your_name
        your_phone
        your_email
        your_pronouns



        #message_name = request.POST['message-name']
        #message_subject = request.POST['message-subject']
        #message_email = request.POST['message-email']
        #message = = request.POST['message']

        # send an email 
        #send_mail(
            #'message_name', # subject
            #message, # message
            #message_email, # from email
            #[rfps@email,com], #To Email

        )

        #return render(request, 'volunteer.html', {})
    #else:
        #return render(request, 'volunteer.html', {})   