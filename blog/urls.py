from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
   path('', views.blog_home, name="blog_home"),
   path('full-post-of-/<str:slug>/', views.blog_detail.as_view(), name="blog_detail"),
]
