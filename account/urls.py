from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # post views
    path('register/', views.register, name="register"),
    path('login/', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('setup/', views.setup, name="setup"),
    path('profile/', views.edit_profile, name="profile"),
    path('case/', views.case_list, name="case"),
    path('case/<int:slug>', views.case_detail_view, name="case_detail"),
    path('logout-user/', views.logout_user, name="logout_user")
]