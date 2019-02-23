from django.contrib.auth.models import User, Permission
from django.test import TestCase, Client
from django.urls import reverse

from books.models import Book


class BookListTestSuite(TestCase):

    '''Tests for index view which takes only GET requests and has to give back list of books'''

    def setUp(self):
        self.client = Client()

    def test_redirect_from_root(self):
        resp = self.client.get('/')
        self.assertRedirects(resp, reverse('login'), fetch_redirect_response=False)

    def test_get_request_with_empty_db(self):
        resp = self.client.get('/books/')
        self.assertIn(b'Nothing to display here', resp.content)

    def test_post_request(self):
        resp = self.client.post('/books/')
        self.assertEqual(resp.status_code, 405)

    def test_books_are_shown(self):
        Book.objects.create(title='First book')
        Book.objects.create(title='Second book')
        resp = self.client.get('/books/')
        self.assertIn(b'First book', resp.content)
        self.assertIn(b'Second book', resp.content)


class AddBookTestSuite(TestCase):

    '''Test adding new book via form'''

    def setUp(self):
        self.client = Client()
        user_with_perm = User.objects.create_user('test_user', password='test_pass')
        user_with_perm.user_permissions.add(Permission.objects.get(content_type__app_label='books', codename='add_book'))
        user_without_perm = User.objects.create_user('new_user', password='new_pass')

    def test_get_form(self):
        self.client.login(username='test_user', password='test_pass')
        resp = self.client.get('/books/new')
        self.assertIn(b'form', resp.content)

    def test_create_book_by_form(self):
        self.client.login(username='test_user', password='test_pass')
        old_books_number = Book.objects.count()
        self.client.post('/books/new', {'title': 'test_title'})
        new_books_number = Book.objects.count()
        self.assertGreater(new_books_number, old_books_number)

    def test_redirect_to_the_booklist(self):
        self.client.login(username='test_user', password='test_pass')
        resp = self.client.post('/books/new', {'title': 'test_title'})
        self.assertRedirects(resp, '/books/')

    def test_isbn_validation(self):
        self.client.login(username='test_user', password='test_pass')
        resp = self.client.post('/books/new', {'title': 'new_book',
                                                'isbn': 'no_value'})
        self.assertIn(b'Only digits and hyphens are allowed', resp.content)

    def test_redirect_witout_permissions(self):
        self.client.login(username='new_user', password='new_pass')
        resp = self.client.get('/books/new')
        self.assertRedirects(resp, '/accounts/login?next=/books/new', target_status_code=301)


class UpdateBookTestSuite(TestCase):

    '''Test updating information about existing book'''

    def setUp(self):
        self.client = Client()
        Book.objects.create(title='test_book')
        user_with_perm = User.objects.create_user('test_user', password='test_pass')
        user_with_perm.user_permissions.add(Permission.objects.get(content_type__app_label='books', codename='change_book'))
        user_without_perm = User.objects.create_user('new_user', password='new_pass')

    def test_response_with_update_form(self):
        self.client.login(username='test_user', password='test_pass')
        resp = self.client.get('/books/1')
        self.assertIn(b'form', resp.content)

    def test_404_for_notexistent_index(self):
        self.client.login(username='test_user', password='test_pass')
        resp = self.client.get('/books/100')
        self.assertEqual(resp.status_code, 404)

    def test_update_data_on_post(self):
        self.client.login(username='test_user', password='test_pass')
        resp = self.client.post('/books/1', {'title': 'new_title'})
        self.assertEqual(resp.status_code, 302)
        book = Book.objects.get(pk=1)
        self.assertEqual(book.title, 'new_title')

    def test_redirect_without_permisions(self):
        self.client.login(username='new_user', password='new_pass')
        resp = self.client.get('/books/1')
        self.assertRedirects(resp, '/accounts/login?next=/books/1', target_status_code=301)