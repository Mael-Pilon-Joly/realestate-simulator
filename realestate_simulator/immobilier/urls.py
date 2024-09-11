from django.urls import path

from . import views

urlpatterns = [
    path("habitants", views.liste_habitants)
]