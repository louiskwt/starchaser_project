from django.views.generic import TemplateView
from .models import Post
class HomePageView(TemplateView):
    posts = Post.published_posts.all()
    template_name: str = 'posts/home.html'
    extra_context = { 'posts': posts }