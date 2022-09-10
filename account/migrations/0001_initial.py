# Generated by Django 4.0.6 on 2022-09-10 07:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('phone_num', models.CharField(blank=True, max_length=8)),
                ('gender', models.CharField(choices=[('F', '女'), ('M', '男'), ('NONE', '--請選擇--')], default='NONE', max_length=7)),
                ('role', models.CharField(choices=[('S', '學生'), ('T', '導師'), ('NONE', '--請選擇--')], default='NONE', max_length=7)),
                ('status', models.CharField(blank=True, max_length=56)),
                ('description', models.TextField()),
                ('member_type', models.CharField(choices=[('FREE', '一般會員'), ('PAID', '星級會員')], default='FREE', max_length=4)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
