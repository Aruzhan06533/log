from django.urls import path
from. import views

urlpatterns = [
    path('login', views.indexPage, name='indexPage'),
    path('loginerr/', views.loadPage, name='loadPage'),
    ]
