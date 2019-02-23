from django.test import TestCase, Client

from books.models import Book


class BookListTestSuite(TestCase):

    '''Tests for index view which takes only GET requests and has to give back list of books'''

    def setUp(self):
        self.client = Client()

    def test_redirect_from_root(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 302)

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

    def test_get_form(self):
        resp = self.client.get('/books/new')
        self.assertIn(b'form', resp.content)

    def test_create_book_by_form(self):
        old_books_number = Book.objects.count()
        self.client.post('/books/new', {'title': 'test_title'})
        new_books_number = Book.objects.count()
        self.assertGreater(new_books_number, old_books_number)

    def test_redirect_to_the_booklist(self):
        resp = self.client.post('/books/new', {'title': 'test_title'})
        self.assertRedirects(resp, '/books/')

    def test_isbn_validation(self):
        resp = self.client.post('/books/new', {'title': 'new_book',
                                                'isbn': 'no_value'})
        self.assertIn(b'Only digits and hyphens are allowed', resp.content)


class UpdateBookTestSuite(TestCase):

    '''Test updating information about existing book'''

    def setUp(self):
        self.client = Client()
        Book.objects.create(title='test_book')

    def test_response_with_update_form(self):
        resp = self.client.get('/books/1')
        self.assertIn(b'form', resp.content)

    def test_404_for_notexistent_index(self):
        resp = self.client.get('/books/100')
        self.assertEqual(resp.status_code, 404)

    def test_update_data_on_post(self):
        resp = self.client.post('/books/1', {'title': 'new_title'})
        self.assertEqual(resp.status_code, 302)
        book = Book.objects.get(pk=1)
        self.assertEqual(book.title, 'new_title')
