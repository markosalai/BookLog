from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('books/dodaj/', views.book_create, name='book_create'),
    path('books/<int:id>/', views.book_detail, name='book_detail'),
    path('books/<int:id>/uredi/', views.book_update, name='book_update'),
    path('books/<int:id>/obrisi/', views.book_delete, name='book_delete'),
    path('books/<int:id>/reviews/', views.book_reviews, name='book_reviews'),
    path('reviews/<int:id>/obrisi/', views.review_delete, name='review_delete'),
]