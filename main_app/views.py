from django.shortcuts import render
from django.views.generic.edit import CreateView
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

def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'books/detail.html', {'book':book})

class BookAdd(CreateView):
    model = Book
    fields = '__all__'
    success_url = '/wan2read'