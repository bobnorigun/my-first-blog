from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .import views

app_name = 'memo'
urlpatterns = [
    path('', views.memo_list, name='memo_list'),
    path('memo/<int:pk>/', views.memo_detail, name='memo_detail'),
]