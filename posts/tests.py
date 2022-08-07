from django.test import TestCase
from django.urls import reverse
from .models import Post
from django.contrib.auth.models import User

class BlogPostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.published_posts.create(title='Test Title', body='Test Body', status='published', author=User.objects.create(username='testuser'))

    def test_model_content(self):
        self.assertEqual(self.post.title, 'Test Title')
        self.assertEqual(self.post.body, 'Test Body')
        self.assertEqual(self.post.status, 'published')
        self.assertEqual(self.post.author.username, 'testuser')
    
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'posts/home.html')