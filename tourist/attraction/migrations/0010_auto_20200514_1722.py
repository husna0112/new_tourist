# Generated by Django 3.0.5 on 2020-05-14 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attraction', '0009_province_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='province',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, null=True, unique=True),
        ),
    ]
