from django.test import TestCase, Client


class RequestsListTestSuite(TestCase):

    '''Test listing last requests'''

    def setUp(self):
        self.client = Client()

    def test_page_richability(self):
        resp = self.client.get('/requests/')
        self.assertEqual(resp.status_code, 200)

    def test_show_requests(self):
        self.client.get('/books/')
        resp = self.client.get('/requests/')
        self.assertIn(b'GET to /books/', resp.content)

    def test_post_not_allowed(self):
        resp = self.client.post('/requests')
        self.assertEqual(resp.status_code, 405)