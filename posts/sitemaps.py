from django.contrib.sitemaps import Sitemap
from posts.models import Post

class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9
    def items(self):
        return Post.published_posts.all()
    def lastmod(self, obj):
        return obj.updated