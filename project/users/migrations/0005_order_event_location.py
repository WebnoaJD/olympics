# Generated by Django 5.1.2 on 2024-10-24 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_order_ticket_nb'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='event_location',
            field=models.CharField(default='', max_length=255),
        ),
    ]
