from django.contrib import admin
from .models import TouristAttraction, Category, Province, Rank
# Register your models here.
class TouristAttractionAdmin(admin.ModelAdmin):
    list_display = ['name', 'province', 'category']

    

    list_per_page = 30

    list_filter = ['category', 'province']
    search_fields = ['name', 'detail']
    autocomplete_fields = ['province', 'category']

admin.site.register(TouristAttraction, TouristAttractionAdmin)


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
admin.site.register(Category, CategoryAdmin)

class ProvinceAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name', 'slug']
    list_editable = ['slug']
admin.site.register(Province, ProvinceAdmin)

class RankAdmin(admin.ModelAdmin):
    list_display = ['rank_number', 'rank_type', 'touristattraction', 'get_province']
    list_filter = ['rank_type', 'province']
    list_per_page = 20
    autocomplete_fields = ['touristattraction']

    def get_province(self, obj):
        return obj.touristattraction.province
    get_province.short_description = 'Province'
    get_province.admin_order_field = 'touristattraction__province'

admin.site.register(Rank, RankAdmin)
