from django.urls import path
from news import views
from .views import TestFormView

urlpatterns = [
   
   path('', views.listNews, name='listNews'),
   path('<int:news_id>/', views.news_detail, name='news_detail'),
   path('test-forms/', TestFormView.as_view(), name="test-form")
]
