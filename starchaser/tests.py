from django.test import TestCase
from django.urls import resolve, reverse


class HomePageTests(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_url_available_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
    
    def test_template_name_correct(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, "pages/home.html")


class NotePageTests(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/notes/")
        self.assertEqual(response.status_code, 200)
    
    def test_url_available_by_name(self):
        response = self.client.get(reverse('notes'))
        self.assertEqual(response.status_code, 200)
    
    def test_template_name_correct(self):
        response = self.client.get(reverse('notes'))
        self.assertTemplateUsed(response, "pages/notes.html")
    