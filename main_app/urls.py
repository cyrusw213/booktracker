from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('wan2read/', views.wan2read_index, name='index'),
    path('wan2read/<int:book_id>/', views.book_detail, name= 'detail'),
    path('books/add', views.BookAdd.as_view(), name='add_book')
]