# imports
from django.views.generic import ListView, DetailView

from .models import Post

# Create your views here.
class BlogPageListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    

class BlogPageDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

