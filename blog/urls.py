from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.post_list, name='post_list'),
   
]
