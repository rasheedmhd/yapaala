from django.urls import path, re_path

from . import views

from .views import (
	house_details,
	home_view,
	all_areas_view,
	PostCategory,
	category_list
	)

app_name = "home"

urlpatterns = [
    path('', home_view.as_view(), name="home"),
    path('all', all_areas_view.as_view(), name="all"),
	path('property/category/<str:slug>/', PostCategory.as_view(), name="post_by_category"),
	#re_path('property/category/(?P<pk>[\d]+)/$', PostCategory.as_view(), name="post_by_category"),
    path('property/<int:pk>/details/', house_details.as_view(), name="details"),
    path('about', views.about, name="about"),
	path('cat-list', category_list, name="category_list"),
    path('contact', views.contact, name="contact"),

	path('comming-soon', views.comming_soon_view, name="comming_soon"),
]
