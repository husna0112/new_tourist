from django.db import models
from django.urls import reverse
from attraction.models import TouristAttraction
from django.db.models import Q
# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=200)
    detail = models.TextField(null=True, blank=True)
    img = models.ImageField(upload_to='news', null=True, blank=True,
                            width_field="width_field", height_field="height_field")
    height_field = models.IntegerField(default=100)
    width_field = models.IntegerField(default=100)
    touristattraction = models.ForeignKey(TouristAttraction, on_delete=models.CASCADE, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)
   

    def __str__(self):
        return self.title

    def get_news_url(self):
        return reverse('news_detail', args=[str(self.id)])