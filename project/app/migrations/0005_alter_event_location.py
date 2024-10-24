# Generated by Django 5.1.2 on 2024-10-20 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_aboutjo_image_credit_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.CharField(choices=[('a', 'Arena Champs de Mars'), ('b', 'Invalides '), ('c', 'Hôtel de Ville de Paris'), ('d', 'La Concorde')], default='a', max_length=10, verbose_name='Lieu'),
        ),
    ]
