from django.urls import path
from .views import about_view, services_view

app_name = 'services' # This is used to namespace the urls.

urlpatterns = [
    path("about", about_view, name="about"),
    path("services", services_view, name="services")
]