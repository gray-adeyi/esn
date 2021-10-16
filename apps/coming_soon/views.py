from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class SoonView(TemplateView):
    template_name = 'coming_soon/index.html'