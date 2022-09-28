from django.conf import settings
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView

class PaymentPageView(TemplateView):
    template_name = 'payment/payment.html'


@csrf_exempt
def stripe_config(request):
    if request.method == "GET":
        stripe_config = {
            'publicKey': settings.STRIPE_PUBLISHABLE_KEY
        }
        return JsonResponse(stripe_config, safe=False)