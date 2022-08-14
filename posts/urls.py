from django.urls import path
from .views import home_display, post_list, post_detail

app_name = 'posts' # This is used to namespace the urls.

urlpatterns = [
    path("", home_display, name="home"),
    path("category/<slug:tag_slug>", post_list, name="post_list"),
    path("<int:year>/<int:month>/<int:day>/<slug:post>/", post_detail, name="post_detail"),
]