from django.urls import path

from . import views

app_name = "lands"

urlpatterns = [
   path('', views.lands, name="lands"),
  # path('full-post-of-/<str:slug>/', blog_detail.as_view(), name="blog_detail"),
   path('yapaala/mission', views.mission_view, name="mission"),
   path('help-and-FAQs', views.help_and_faq_view, name="help_and_faq"),
   path('privacy-terms-refunds', views.privacy_and_terms_view, name="terms"),
]
