from django.urls import path

from . import views

app_name = "artisans"

urlpatterns = [
   #path('', views.artisans_home, name="artisans_home"),
   path('', views.all_artisans_view, name="artisans"),
]
