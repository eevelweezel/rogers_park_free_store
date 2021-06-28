from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import (
    include,
    path
)
from . import views
from .views import (
    about,
    all_products,
    ContactUs,
    item_detail,
    successView,
    VolunteerSignup
)

app_name = 'rpfs'

urlpatterns = [
 #   path('', views.all_products, name='all_products'),
    path('search/', views.category_list, name='category_list'),
    path('admin/', admin.site.urls),
    path('', all_products, name ="home"),
    path('contact/', ContactUs.as_view(), name ="contact"),
    path('volunteer/', VolunteerSignup.as_view(), name ="volunteer"),
    path('about/', about, name ="about"),
    path('item/<slug:slug>/', item_detail, name ="items"), 
    path('success/', successView, name='success'),
    path('captcha/', include('captcha.urls')),
]
 

if settings.DEBUG:
     urlpatterns += \
         static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
     urlpatterns += \
         static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

