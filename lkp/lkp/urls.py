from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('web.urls_web')),
    path('', include('app.urls_app')),
    path('admin/', admin.site.urls),
]
