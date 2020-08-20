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
    path('rooms/listing', views.upload, name="create_property" ),
    path('rooms', all_areas_view.as_view(), name="all"),
	path('rooms/town/<str:slug>/', PostCategory.as_view(), name="post_by_category"),
	#re_path('property/category/(?P<pk>[\d]+)/$', PostCategory.as_view(), name="post_by_category"),
    path('rooms/<int:pk>/details/', house_details.as_view(), name="details"),
    path('about', views.about, name="about"),
	path('cat-list', category_list, name="category_list"),
	path('comming-soon', views.coming_soon_view, name="comming_soon"),
]
