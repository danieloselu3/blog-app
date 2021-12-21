# imports
from django.urls import path

from .views import BlogPageListView

app_name = 'blog'
urlpatterns = [
    path('', BlogPageListView.as_view(), name='home'),
]