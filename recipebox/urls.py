from django.urls import path

from recipebox import views

urlpatterns = [
    path("", views.index),
    path('recipes/<int:pk>/', views.recipe_detail, name="recipe_detail"),
    path('authors/<int:pk>/', views.author_detail, name="author_detail")
]

