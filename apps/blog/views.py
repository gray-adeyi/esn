from django.views.generic import ListView, DetailView
from . import models
# Create your views here.

class BlogIndex(ListView):
    template_name = 'blog/blog.html'
    model = models.Post


class BlogPost(DetailView):
    template_name = 'blog/blog-single.html'
    model = models.Post

class AuthorDetail(DetailView):
    template_name = 'blog/author.html'
    model = models.Author