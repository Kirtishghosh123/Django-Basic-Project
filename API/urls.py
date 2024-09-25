from rest_framework_simplejwt.views import (
    TokenObtainPairView,TokenRefreshView
)
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.Homeview.as_view(),name='home'),
    path('login/', views.Login.as_view(),name='login'),
    path('createrecipe/', views.Recipe.as_view(), name='create_recipe'),
    path('showrecipe/', views.RecipeView.as_view(), name='show_recipe'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.RegisterView.as_view(), name='register-user'),
]
