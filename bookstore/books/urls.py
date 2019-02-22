from django.urls import path

from . import views


app_name = 'books'


urlpatterns = [
    path('', views.index, name='index'),
    path('new', views.add_new_book, name='new-book'),
]