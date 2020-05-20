# Generated by Django 3.0.5 on 2020-05-14 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attraction', '0011_rank_province'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rank',
            name='rank_type',
            field=models.CharField(choices=[('ระดับจังหวัด', 'ระดับจังหวัด'), ('ระดับประเทศ', 'ระดับประเทศ')], default='ระดับจังหวัด', max_length=50),
        ),
    ]
