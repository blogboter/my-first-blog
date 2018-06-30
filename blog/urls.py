from . import views
from django.urls import path, include
app_name='blog'
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<str:year>/<str:month>/<str:day>/<str:title>', views.post_detail, name='post_detail'),
   
]
