from django.urls import path
from . views import *

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('careers/', careers, name='careers'),
    path('contact/', contact, name='contact'),
    path('faq/', faq, name='faq'),
    path('features/', features, name='features'),
    path('privacy-policy/', privacy_policy, name='privacy-policy'),
]

