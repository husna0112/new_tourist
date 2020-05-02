from django.db import models
from django.urls import reverse
from decimal import Decimal
from django.db.models import Q
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Province(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class TouristAttraction(models.Model):
    name = models.CharField(max_length=100)
    #slug = models.SlugField(null=True)
    contact = models.CharField(max_length=100, blank=True, null=True)
    time = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    detail = models.TextField(null=True, blank=True)
    img = models.URLField(blank=True)
    lat = models.DecimalField(max_digits=9, decimal_places=6, default=Decimal('0.000000'))
    lng = models.DecimalField(max_digits=9, decimal_places=6, default=Decimal('0.000000'))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    province = models.ForeignKey(Province, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])

    def get_add_to_plan_url(self):
        return reverse('add-to-plan', args=[str(self.id)])

class Rank(models.Model):
    rank_number = models.IntegerField()
    rank_province = 'ระดับจังหวัด'
    rank_country = 'ระดับประเทศ'
    TYPE2 = (
        (rank_province, 'ระดับจังหวัด'),
        (rank_country, 'ระดับประเทศ')
    )
    rank_type = models.CharField(max_length=50, choices=TYPE2, default=rank_country)
    touristattraction = models.ForeignKey(TouristAttraction, on_delete=models.CASCADE)


    def __str__(self):
        return self.rank_type