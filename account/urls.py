from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # post views
    path('register/', views.register, name="register"),
    path('login/', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('setup/', views.setup, name="setup"),
    path('case/', views.case_list, name="case"),
    path('logout-user/', views.logout_user, name="logout_user")
]