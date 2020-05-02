from django.contrib import admin
from .models import News

# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'detail', 'updated', 'timestamp']
    list_per_page = 20

    list_filter = ['updated', 'timestamp']
    search_fields = ['title', 'detail']
admin.site.register(News, NewsAdmin)