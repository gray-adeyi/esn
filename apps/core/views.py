from django.shortcuts import render
from django.views.generic import TemplateView
import logging

logger = logging.getLogger(__name__)

# Create your views here.
class Index(TemplateView):
    template_name = 'core/index.html'


def handler404(request, exception):
    logger.error("Could not resolve path: ", str(exception.get('path')))
    return render(request, 'core/404.html')


def handler500(request):
    return render(request, 'core/500.html')