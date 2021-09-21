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
    items_needed,
    successView,
    VolunteerSignup
)

app_name = 'rpfs'

urlpatterns = [
 #   path('', views.all_products, name='all_products'),
    path('search/', views.category_list, name='category_list'),
    path('admin/', admin.site.urls),
    path('contact/', ContactUs.as_view(), name ="contact"),
    path('volunteer/', VolunteerSignup.as_view(), name ="volunteer"),
    path('about/', about, name ="about"),
    path('item/<slug:slug>/', items_needed, name ="items"), 
    path('success/', successView, name='success'),
    path('captcha/', include('captcha.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
    path('tinymce/', include('tinymce.urls')),
    path('', all_products, name ="home"),
]
 

if settings.DEBUG:
     urlpatterns += \
         static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
     urlpatterns += \
         static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

