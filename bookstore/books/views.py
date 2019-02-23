from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseNotAllowed, HttpResponseRedirect
from django.urls import reverse

from .models import Book
from .forms import BookForm


def index(request):

    '''Index page of site with the list of all books'''

    #Only GET requests are accepted by this view
    if request.method == 'GET':
        books = Book.objects.all()
        return render(request, 'books/index.html', {'books': books})
    else:
        #For other request methods return response with status 405 and
        #list with only allowed method
        return HttpResponseNotAllowed(['GET'])


def add_new_book(request):

    '''Cretion of the new book instance'''

    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('books:index'))
    else:
        form = BookForm()
    return render(request, 'books/new_book.html', {'form': form})


def update_book(request, book_id):

    '''Update information about the existing book'''
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('books:index'))
    else:
        form = BookForm(instance=book)
    return render(request, 'books/update_book.html', {'form': form})    
