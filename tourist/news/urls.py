from django.urls import path
from news import views

urlpatterns = [
   
   path('', views.listNews, name='listNews'),
   path('<int:news_id>/', views.news_detail, name='news_detail'),

]
