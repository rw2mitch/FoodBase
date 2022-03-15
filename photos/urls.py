from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerUser, name="register"),

    path('', views.gallery, name='gallery'),
    # path('photo/<str:pk>/', views.viewPhoto, name='photo'),
    # path('add/', views.addPhoto, name='add'),

    path('food/<str:pk>/', views.viewFood, name='food'),
    path('add/', views.addFood, name='add'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('calcResourceAllocation/', views.calcResourceAllocation, name='calcResourceAllocation'),
    path('recommendations/', views.getRecommendations, name='recommendations'),
    
]
