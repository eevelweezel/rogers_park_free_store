from django.template.response import TemplateResponse
from django.views.generic.base import View


class HomeView(View):
    
    def get(self, request, *args, **kwargs):
        context = {}
        return TemplateResponse(
                   request,
                   'home.html',
                   context=context,
                   status=200)        
