from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class TestPaymentPage(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get('/payment/')
        self.assertEqual(response.status_code, 200)
    
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('payment'))
        self.assertTemplateUsed(response, "payment/payment.html")