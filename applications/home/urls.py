from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.PruebaView.as_view()),
    path('lista/', views.PruebaListView.as_view()),
    path('homeprueba/', views.ListarPrueba.as_view()),
    path('add/', views.PruebaCreateView.as_view()),
    path('resumen/', views.ResumenFoundationView.as_view())

]