# Generated by Django 3.0.5 on 2020-05-14 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attraction', '0010_auto_20200514_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='rank',
            name='province',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='attraction.Province'),
        ),
    ]
