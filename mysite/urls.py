"""mysite URL Configuration
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('wall/', include('blog.urls')),
    path('', include('polls.urls')),
]