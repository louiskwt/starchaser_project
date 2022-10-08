from django.test import TestCase


# Create your tests here.
class UrlTest(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get('/payment/')
        self.assertEqual(response.status_code, 200)