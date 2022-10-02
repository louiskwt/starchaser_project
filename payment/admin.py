from django.contrib import admin
from .models import PaymentRecord

class PaymentAdmin(admin.ModelAdmin):
    readonly_fields = ('payment_date',)
# Register your models here.
admin.site.register(PaymentRecord, PaymentAdmin)