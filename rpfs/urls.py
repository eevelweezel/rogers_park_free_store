from django.contrib import admin
from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('item/<slug:slug>/', views.product_detail, name='product_detail'),
    path('search/<slug:category_slug>/', views.category_list, name='category_list'),
    path('admin/', admin.site.urls),
    path('', include ('sendemail.urls')),
    path('home.html', views.home, name ="home"),
    path('contact.html', views.contact, name ="contact"),
    #path('about.html', views.about, name ="about"),
    #path('items.html', views.items, name ="items"), 
        #I want to rename the "detail.html" to "items.html"
    #path('volunteer.html', views.volunteer, name ="volunteer"),
    #path('signup.html', views.signup, name ="signup"),

]   

