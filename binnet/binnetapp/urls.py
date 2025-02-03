from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('detail/', views.detail, name='detail'),
    path('', views.test_react, name='test_react'),
]
