from django.views.generic.base import TemplateView

class PaymentPageView(TemplateView):
    template_name = 'payment/payment.html'