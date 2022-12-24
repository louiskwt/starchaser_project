from django.urls import path

from .views import notes_index_view

app_name = "notes_app"

urlpatterns = [
    path("", notes_index_view, name="index")
]