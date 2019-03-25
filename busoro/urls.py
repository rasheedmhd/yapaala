from django.urls import path

from . import views

app_name = "busoro"

urlpatterns = [
   path('', views.busoro, name="home"),
]
