from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('support.urls_support')),
    path('', include('landing.urls_landing')),
    path('', include('faq.urls_faq')),
    path('', include('blog.urls_blog')),
    path('', include('app.urls_app')),
    path('admin/', admin.site.urls),
]
