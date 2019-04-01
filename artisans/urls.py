from django.urls import path

from . import views

app_name = "artisans"

urlpatterns = [
   path('', views.artisans_home, name="artisans_home"),
   path('all-artisans', views.all_artisans_view, name="all_artisans"),
]
