from django.shortcuts import get_object_or_404, render
from .models import Post, Comment
from taggit import models as taggit_models
from .forms import CommentForm

# class HomePageView(TemplateView):
#     posts = Post.published_posts.all()
#     template_name: str = 'posts/home.html'
#     extra_context = { 'posts': posts }

def home_display(request, tag_slug=None):
    tags = taggit_models.Tag.objects.all()
    context = {
        'tags': tags,
    }
    return render(request, 'posts/home.html', context)

def post_list(request, tag_slug=None):
    object_list = Post.published_posts.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(taggit_models.Tag, slug=tag_slug)
        posts = object_list.filter(tags__in=[tag])
    else:
        posts = object_list
    
    context = {
        'posts': posts,
        'tag': tag,
    }

    return render(request, 'posts/post_list.html', context)

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published', publish__year=year, publish__month=month, publish__day=day)
    comments = post.comments.filter(active=True)

    comment_form = CommentForm
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        else:
            comment_form = CommentForm()
            new_comment = None
            
    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
        'new_comment': new_comment,
    }
    return render(request, 'posts/post_detail.html', context)
    