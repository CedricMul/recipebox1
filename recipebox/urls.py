from django.urls import path

from recipebox import views

urlpatterns = [
    path("", views.index)
]