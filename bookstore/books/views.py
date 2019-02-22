from django.shortcuts import render
from django.http import HttpResponseNotAllowed

from .models import Book


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
