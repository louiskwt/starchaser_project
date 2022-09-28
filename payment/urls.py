from django.urls import path

from . import views

urlpatterns = [
    path('', views.PaymentPageView.as_view(), name="payment"),
    path('config/', views.stripe_config),
    path('create-checkout-session/', views.create_checkout_session)
]