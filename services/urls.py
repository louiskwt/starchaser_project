from django.urls import path
from .views import about_view, services_view
from django.conf.urls import handler404, handler500

app_name = 'services' # This is used to namespace the urls.

urlpatterns = [
    path("about", about_view, name="about"),
    path("services", services_view, name="services")
]

handler404 = 'services.views.error_404_view'
handler500 = 'services.views.error_500_view'