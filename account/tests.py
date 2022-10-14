from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
# Create your tests here.

class UserSignUpTests(TestCase):
    username = "newuser"
    email = "newuser@gmail.com"

    def test_signup_page_status_code(self):
        response = self.client.get("/member/register")
        self.assertEqual(response.status_code, 301)
    
    def test_view_url_by_name(self):
        response = self.client.get(reverse("register"))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse("register"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "registration/register.html")
    
    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(self.username, self.email)

        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)

class UserLogInTests(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret',
        }
        User.objects.create_user(**self.credentials)

    def test_user_login_form(self):
        response = self.client.post('/member/login', self.credentials, follow=True)
   
        self.assertTrue(response.status_code == 200)