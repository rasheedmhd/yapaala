from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
   path('', views.blog_home, name="blog_home"),
   path('full-post-of-/<str:slug>/', views.blog_detail.as_view(), name="blog_detail"),
   path('placentanetwork/yapaala/mission', views.mission_view, name="mission"),
   path('help-and-FAQs', views.help_and_faq_view, name="help_and_faq"),
   path('privacy-terms-refunds', views.privacy_and_terms_view, name="terms"),
   path('how-to/writing/author', views.writing_view, name="writing"),
]
