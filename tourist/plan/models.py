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

    def get_id(self):
        return self.id

    

    def get_create_plan_url(self):
        return reverse('plan_create')

    def get_place_delete(self):
        return reverse('place_delete', args=[str(self.id)])

    def get_plan_detail(self):
        return reverse('plan_detail', args=[str(self.id)])

    
    # def get_absolute_url(self):
    #     return reverse('attraction:detail', kwargs={'pk': self.plan.touristattractions.id})


