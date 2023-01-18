from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

# Create your views here.
def home(request):
    return HttpResponse('<h1>hello world</h1>')
def about(request):
    return render(request, 'about.html')

def wan2read_index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books})