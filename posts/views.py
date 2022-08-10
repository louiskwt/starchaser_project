from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView
from .models import Post
# class HomePageView(TemplateView):
#     posts = Post.published_posts.all()
#     template_name: str = 'posts/home.html'
#     extra_context = { 'posts': posts }

def post_list(request, tag_slug=None):
    posts = Post.published_posts.all()
    return render(request, 'posts/home.html', {'posts': posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published', publish__year=year, publish__month=month, publish__day=day)
    
    return render(request, 'posts/post_detail.html', {'post': post})