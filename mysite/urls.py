"""mysite URL Configuration
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('polls.urls')),
    path('wall/', include('blog.urls')),
    path('files/', include('files.urls')),
    path('csvfile/', include('csvfile.urls')),
    path('caldist/', include('caldist.urls')),
    path('distsum/', include('distsum.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)