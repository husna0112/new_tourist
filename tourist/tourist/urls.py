"""tourist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from attraction.views import Home, rank_country, search, rank_province, rank_province_item


urlpatterns = [
    path('', Home, name='home'),
    path('admin/', admin.site.urls),
    path('attraction/', include('attraction.urls')),
    path('plan/', include('plan.urls')),
    path('', include('authen.urls')),
    path('news/', include('news.urls')),
    path('rank_country/', rank_country, name='rank_country'),
    path('rank_province/', rank_province, name='rank_province'),
    path('rank_province/<int:province_id>', rank_province_item, name='rank_province_item'),
    path('search/', search, name='search'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)