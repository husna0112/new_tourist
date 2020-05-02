from django.contrib import admin
from .models import TouristAttraction, Category, Province, Rank
# Register your models here.
class TouristAttractionAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'province', 'img']
    list_editable = ['img']

    list_per_page = 30

    list_filter = ['province']
    search_fields = ['name', 'detail']

admin.site.register(TouristAttraction, TouristAttractionAdmin)

admin.site.register(Category)
admin.site.register(Province)

class RankAdmin(admin.ModelAdmin):
    list_display = ['rank_number', 'rank_type', 'touristattraction', 'get_province']
    list_per_page = 20

    def get_province(self, obj):
        return obj.touristattraction.province
    get_province.short_description = 'Province'
    get_province.admin_order_field = 'touristattraction__province'

admin.site.register(Rank, RankAdmin)