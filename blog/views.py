# imports
from django.views.generic import ListView

from .models import Post

# Create your views here.
class BlogPageListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    

