# Generated by Django 4.0.6 on 2022-10-02 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_paymentrecord_payment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentrecord',
            name='payment_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
