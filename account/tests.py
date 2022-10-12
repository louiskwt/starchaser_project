from django.test import TestCase
from django.urls import reverse
# Create your tests here.

class UserSignUpTests(TestCase):
    username = "newuser"
    email = "newuser@gmail.com"

    def test_signup_page_status_code(self):
        response = self.client.get("/member/register")
        self.assertEqual(response.status_code, 200)
    
    def test_view_url_by_name(self):
        response = self.client.get(reverse("register"))
        self.assertEqual(response.status_code, 301 or 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse("register"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/register.html")
    