"""starchaser URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from re import template
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('account.urls')),
    path('about/', TemplateView.as_view(template_name="about.html"), name="about"),
    path('blog/', TemplateView.as_view(template_name="blog_index.html"), name="blog"),
    path("resource/", TemplateView.as_view(template_name="resource.html"), name="resource"),
    path("terms/", TemplateView.as_view(template_name="member/consent.html"), name="terms"),
    path('', TemplateView.as_view(template_name="home.html"), name="home"),
]
