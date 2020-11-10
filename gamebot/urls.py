from django.urls import path

from gamebot import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
]