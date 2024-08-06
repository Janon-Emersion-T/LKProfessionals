from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('blog', blog, name='blog'),
    path('pricing', pricing, name='pricing'),
    path('faq', faq, name='faq'),
    path('/about', about, name='about'),
]
