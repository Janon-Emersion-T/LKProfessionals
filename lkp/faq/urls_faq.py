from django.urls import path
from .views import *

urlpatterns = [
    path('/faq', faq, name='faq'),
]
