from django.db import models
from attraction.models import TouristAttraction
from django.conf import settings
from django.urls import reverse

# Create your models here.
class PlanTouristAttraction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    touristattraction = models.ForeignKey(TouristAttraction, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    planed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.quantity} of {self.touristattraction.name}"
 


class Plan(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    detail = models.TextField(null=True, blank=True)
    touristattractions = models.ManyToManyField(PlanTouristAttraction)
    planed_date = models.DateTimeField(auto_now=False, auto_now_add=True, null=True)
    planed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

