# Generated by Django 3.0.5 on 2020-04-22 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attraction', '0002_touristattraction_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='touristattraction',
            name='quantity',
        ),
    ]
