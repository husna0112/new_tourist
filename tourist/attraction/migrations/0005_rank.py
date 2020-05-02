# Generated by Django 3.0.5 on 2020-04-28 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attraction', '0004_auto_20200426_1400'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank_number', models.IntegerField()),
                ('rank_type', models.CharField(choices=[('ระดับจังหวัด', 'ระดับจังหวัด'), ('ระดับประเทศ', 'ระดับประเทศ')], default='ระดับประเทศ', max_length=50)),
                ('province', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attraction.Province')),
                ('touristattraction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attraction.TouristAttraction')),
            ],
        ),
    ]
