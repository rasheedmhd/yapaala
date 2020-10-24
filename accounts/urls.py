from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = "accounts"

urlpatterns = [
   #path('login', views.login_view, name="login"),
   path('login', auth_views.LoginView.as_view(), name="login"),
   path('register', views.register_view, name="register"),
   path('dashboard', views.dashboard_view, name="dashboard"),
   path('logout', views.logout_view, name="logout"),
]
