from django.views.generic import TemplateView, ListView, DetailView
from .models import Post

# Create your views here.

class HelloDjango(TemplateView):
    template_name = 'home.html'

class PostListView(ListView):
    model = Post
    template_name = "home.html"

class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
