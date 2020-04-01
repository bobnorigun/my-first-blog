from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views

app_name = 'csvfile'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.profile_upload, name="profile_upload"),
]