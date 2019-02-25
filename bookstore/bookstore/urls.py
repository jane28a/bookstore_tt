"""bookstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

from books.admin import admin_site


def redirect_from_root(request):

    '''Redirecting logged-in users to booklist from the root.
    Anonymous users goes to login page'''

    if request.user.is_authenticated:
        return redirect('books:index')
    else:
        return redirect('login')



urlpatterns = [
    path('', redirect_from_root),
    path('books/', include('books.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('management/', admin_site.urls),
]
