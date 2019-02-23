from django.contrib.admin import AdminSite

from .models import Book

class BooksAdminSite(AdminSite):

    '''Custom site admin for managing the books'''

    site_header = 'Bookstore management'
    site_title = 'Bookstore'
    site_url = None
    index_title = 'Welcome'


    def has_permission(self, request):
        
        '''Returns true if user is manager'''

        return 'managers' in request.user.groups.values_list('name', flat=True)


admin_site = BooksAdminSite(name='booksadmin')
admin_site.register(Book)

