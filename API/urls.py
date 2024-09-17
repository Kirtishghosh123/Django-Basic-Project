
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('createrecipe/', views.recipe_handle, name='create_recipe'),
    path('showrecipe/', views.recipe_view, name='show_recipe'),
]
