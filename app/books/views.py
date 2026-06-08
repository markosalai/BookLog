from django.shortcuts import render, get_object_or_404
from .models import Knjiga

# Create your views here.

def book_list(request):
    books = Knjiga.objects.find_all()
    return render(request, "books/list.html", {'books': books})