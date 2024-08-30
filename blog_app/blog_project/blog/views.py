from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import Post

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    
    
class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
# Create your views here.
