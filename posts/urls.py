from django.urls import path
from .views import home_display, post_list, post_detail
from django.contrib.sitemaps.views import sitemap
from posts.sitemaps import PostSitemap

app_name = 'posts' # This is used to namespace the urls.

sitemaps = {
    'posts': PostSitemap
}

urlpatterns = [
    path("", home_display, name="index"),
    path("category/<slug:tag_slug>", post_list, name="post_list"),
    path("<int:year>/<int:month>/<int:day>/<slug:post>/", post_detail, name="post_detail"),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'  )
]