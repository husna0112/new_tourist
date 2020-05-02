from django.contrib import admin
from .models import Plan, PlanTouristAttraction


# Register your models here.

admin.site.register(Plan)
admin.site.register(PlanTouristAttraction)


# class PlanTouristAttractionAdmin(admin.ModelAdmin):
#     list_display = ['user', 'touristattraction']
#     list_per_page = 20

# admin.site.register(PlanTouristAttraction, PlanTouristAttractionAdmin)