# imports
from django.urls import path

from .views import BlogPageListView, BlogPageDetailView

app_name = 'blog'
urlpatterns = [
    path('', BlogPageListView.as_view(), name='home'),
    path('post/<int:pk>/', BlogPageDetailView.as_view(), name='post_detail'),
]