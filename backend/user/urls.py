from django.urls import path
from . import views


urlpatterns = [
    path('users/', views.getAllUsers, name='AllUsers'),
    path('user/<str:pk>/', views.getSingleUser, name='SingleUser'),
    path('add-user/', views.addUser, name='AddUser'),
    path('delete-user/<str:pk>/', views.deleteUser, name='DeleteUser'),
]
