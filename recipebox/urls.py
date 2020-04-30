from django.urls import path

from recipebox import views

urlpatterns = [
    path("", views.index),
    path('recipes/<str:recipe_url>/', views.recipe_detail, name="recipe_detail"),
    path('authors/<str:author_url>/', views.author_detail, name="author_detail")
]

