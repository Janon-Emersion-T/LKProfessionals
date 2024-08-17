from django.urls import path
from . views import *

urlpatterns = [
    path('blog/', blog, name='blog'),
    path('blog-single/', blog_single, name='blog-single'),
]

