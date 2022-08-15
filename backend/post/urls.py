from django.urls import path
from . import views


urlpatterns = [
    path('posts/', views.getAllPosts, name='AllPosts'),
    path('post/<str:pk>', views.getSinglePost, name='SinglePost'),
    path('add-post/', views.addPost, name='AddPost'),
    path('update-post/<str:pk>', views.updatePost, name='updatePost'),
    path('delete-post/<str:pk>', views.deletePost, name='DeletePost'),
    
    path('comments/', views.getAllComments, name='AllComments'),
    path('comment/<str:pk>', views.getSingleComment, name='SingleComment'),
    path('add-comment/', views.addComment, name='AddComment'),
    path('update-comment/<str:pk>', views.updateComment, name='updateComment'),
    path('delete-comment/<str:pk>', views.deleteComment, name='DeleteComment'),
]
