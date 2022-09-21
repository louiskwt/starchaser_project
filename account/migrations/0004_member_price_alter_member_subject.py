# Generated by Django 4.0.6 on 2022-09-18 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_member_subject_alter_member_gender'),
    ]

    operations = [
        migrations.AddField(
           model_name='member',
            name='price',
            field=models.CharField(default='', max_length=32),
        ),
        migrations.AlterField(
            model_name='member',
            name='subject',
            field=models.CharField(choices=[('biology', 'DSE-生物'), ('chinese', 'DSE-中文'), ('english', 'DSE-英文'), ('c-hist', 'DSE-中史'), ('hist', 'DSE-世史'), ('ielts', 'IELTS'), ('math', 'DSE-數學'), ('chem', 'DSE-化學'), ('it', 'DSE-資訊科技'), ('ls', 'DSE-通識'), ('sat', 'SAT'), ('a-level', 'A-Level'), ('uni', '大專補習')], default='NONE', max_length=8),
        ),
        migrations.AlterField(
            model_name='member',
            name='role',
            field=models.CharField(choices=[('S', '學生'), ('T', '導師')], default='NONE', max_length=7),
        ),
    ]