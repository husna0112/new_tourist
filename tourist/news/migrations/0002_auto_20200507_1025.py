# Generated by Django 3.0.5 on 2020-05-07 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='height_field',
        ),
        migrations.RemoveField(
            model_name='news',
            name='width_field',
        ),
        migrations.AlterField(
            model_name='news',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='news'),
        ),
    ]
