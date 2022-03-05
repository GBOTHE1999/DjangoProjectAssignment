from django.contrib import admin
from . import views
from django.urls import path, include
from .views import Dashboard,PostListView,UserRegisterView,AddPostView
 
urlpatterns = [
     
    path('', Dashboard, name='dashboard'),
    path('post-list/',PostListView, name='post-list'),
    path('register/',UserRegisterView.as_view(),name='register'),
    path('add_post/', AddPostView.as_view(), name="add_post"),
]
