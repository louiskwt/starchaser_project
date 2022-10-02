from django.http.response import JsonResponse, HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView
from .models import PaymentRecord
from django.contrib.auth.models import User
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
        try:
            checkout_session = stripe.checkout.Session.create(
                client_reference_id=request.user.id if request.user.is_authenticated else None,
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

@csrf_exempt
def stripe_webhook(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    endpoint_secret = settings.STRIPE_ENDPOINT_SECRET  #TODO: Need to get that
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)

    if event['type'] == 'checkout.session.completed':
        print(f"event data: {event.data.object}")
        user_id = event.data.object["client_reference_id"]
        user = User.objects.get(id=user_id)
        print(f"found user: {user}")
        try:
            record = PaymentRecord(user=user, name=event.data.object.customer_details["name"], email=event.data.object.customer_details["email"])
            record.save()
        except KeyError as e:
            print(e)
            # Maybe loggin it

        print("All went well : )")

    
    return HttpResponse(status=200)