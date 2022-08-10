from django.urls import path
from .views import post_list, post_detail

app_name = 'posts' # This is used to namespace the urls.

urlpatterns = [
    path("", post_list, name="home"),
    path("<int:year>/<int:month>/<int:day>/<slug:post>/", post_detail, name="post_detail"),
]