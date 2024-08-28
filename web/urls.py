from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('services/', services, name='services'),
    path('careers/', careers, name='careers'),
    path('contact/', contact, name='contact'),
    path('privacy_policy/', privacy_policy, name='privacy_policy'),
    path('features/', features, name='features'),
    path('faq/', faq, name='faq'),
]