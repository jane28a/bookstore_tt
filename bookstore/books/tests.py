from django.test import TestCase, Client

from books.models import Book 


class BookListTestSuite(TestCase):

    '''Test for index view which takes only GET requests and has to give back list of books'''

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
