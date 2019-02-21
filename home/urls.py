from django.urls import path

from . import views

from .views import house_details

app_name = "home"

urlpatterns = [
    path('', views.home_view, name="home"),
    path('home/<int:pk>/', house_details.as_view(), name="details"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
]
