from django.urls import path
from . import views_web

urlpatterns = [
    path('', views_web.knjizna_polica, name='knjizna_polica'),
    path('<int:id>/', views_web.knjiga_detalji, name='knjiga_detalji'),
    path('dodaj/', views_web.knjiga_dodaj, name='knjiga_dodaj'),
]