from django.contrib import admin
from .models import Plan, PlanTouristAttraction


# Register your models here.
class PlanAdmin(admin.ModelAdmin):
    list_display = ['name', 'user']
    list_per_page = 20
    search_fields = ['name']

admin.site.register(Plan, PlanAdmin)

class PlanTouristAttractionAdmin(admin.ModelAdmin):
    list_display = ['touristattraction', 'user']
    list_per_page = 20

admin.site.register(PlanTouristAttraction, PlanTouristAttractionAdmin)


