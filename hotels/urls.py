from django.urls import path

from . import views

from .views import hotel_page

app_name = "hotels"

urlpatterns = [
    path('', views.hotel_view, name="hotel"),
    path('page/<int:pk>/', hotel_page.as_view(), name="page"),
]
