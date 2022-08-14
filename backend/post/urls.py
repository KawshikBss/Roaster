from django.urls import path
from . import views


urlpatterns = [
    path('posts/', views.getAllPosts, name='AllPosts'),
    path('post/<str:pk>', views.getSinglePost, name='SinglePost'),
    path('add-post/', views.addPost, name='AddPost'),
    path('delete-post/<str:pk>', views.deletePost, name='DeletePost'),
]
