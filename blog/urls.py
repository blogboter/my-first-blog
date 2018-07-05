from . import views
from django.urls import path, include
from .feeds import LatestPostsFeed

app_name='blog'
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<str:year>/<str:month>/<str:day>/<str:title>', views.post_detail, name='post_detail'),
    path('tag/<tag_slug>', views.post_list, name='post_list_by_tag'),
    path('feed/', LatestPostsFeed(), name='post_feed'),
    path('search/', views.search_form, name='search_form')
   
]
