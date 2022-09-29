from django.conf import settings
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView
import stripe

class PaymentPageView(TemplateView):
    template_name = 'payment/payment.html'

class SuccessView(TemplateView):
    template_name = 'payment/success.html'

class CancelledView(TemplateView):
    template_name = 'payment/cancelled.html'


@csrf_exempt
def stripe_config(request):
    if request.method == "GET":
        stripe_config = {
            'publicKey': settings.STRIPE_PUBLISHABLE_KEY
        }
        return JsonResponse(stripe_config, safe=False)

@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':
        domain_url = settings.DOMAIN_URL
        stripe.api_key = settings.STRIPE_SECRET_KEY
        print('fired')
        try:
            checkout_session = stripe.checkout.Session.create(
                success_url= domain_url + '/payment/success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url= domain_url + '/payment/cancelled/',
                payment_method_types=['card'],
                mode='payment',
                line_items=[
                    {
                        'price_data': {
                            'currency': 'hkd',
                            'unit_amount': '6800',
                            'product_data': {
                                'name': "StarChaser 星級會員",
                                "description": "成為星級會員去享受自由搵導師或學生的體驗",
                            }
                        },
                        'quantity': 1,
                    }
                ]
            )
            print(f'session: {checkout_session}')
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            print(f'error: {e}')
            return JsonResponse({'error': str(e)})