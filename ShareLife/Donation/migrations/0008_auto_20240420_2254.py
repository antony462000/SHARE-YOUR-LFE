# Generated by Django 3.1.1 on 2024-04-20 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Donation', '0007_auto_20240420_2253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='surgery',
            name='HealthRecord',
        ),
        migrations.RemoveField(
            model_name='surgery',
            name='is_healthrecord_status',
        ),
        migrations.AddField(
            model_name='organrequest',
            name='HealthRecord',
            field=models.FileField(blank=True, null=True, upload_to='HealthFile'),
        ),
        migrations.AddField(
            model_name='organrequest',
            name='is_healthrecord_status',
            field=models.BooleanField(default=False),
        ),
    ]