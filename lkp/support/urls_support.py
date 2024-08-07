from django.urls import path
from .views import *

urlpatterns = [
    path('/privacy', privacy, name='privacy'),
    path('/terms_of_service', terms_of_service, name='terms_of_service'),
    path('/cookie_policy', cookie_policy, name='cookie_policy'),
    path('/right_of_withdrawal', right_of_withdrawal, name='right_of_withdrawal'),
]
