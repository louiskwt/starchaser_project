# Generated by Django 4.0.6 on 2022-09-23 15:35

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_alter_member_mode_alter_member_referral'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='referral',
            field=models.CharField(choices=[('A', '接受'), ('D', '拒絕')], default='A', max_length=3),
        ),
        migrations.AlterField(
            model_name='member',
            name='subject',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('biology', 'DSE-生物'), ('chinese', 'DSE-中文'), ('english', 'DSE-英文'), ('c-hist', 'DSE-中史'), ('hist', 'DSE-世史'), ('ielts', 'IELTS'), ('math', 'DSE-數學'), ('chem', 'DSE-化學'), ('it', 'DSE-資訊科技'), ('ls', 'DSE-通識'), ('sat', 'SAT'), ('a-level', 'A-Level'), ('uni', '大專補習')], max_length=7),
        ),
    ]
