from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('web.urls')),
    path('', include('dashboard.urls')),
    path('', include('blog.urls')),
    path('admin/', admin.site.urls),
]
