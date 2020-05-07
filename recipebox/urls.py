from django.urls import path

from recipebox import views

urlpatterns = [
    path("", views.index, name="homepage"),
    path("add_author/", views.authoradd, name="author_add"),
    path("add_recipe/", views.recipeadd, name="recipe_add"),
    path('recipes/<str:recipe_url>/', views.recipe_detail, name="recipe_detail"),
    path('authors/<str:author_url>/', views.author_detail, name="author_detail"),
    path('login/', views.loginview, name="login"),
    path('logout', views.logoutview, name="logout"),
    path('signup/', views.signup, name='signup')
]

