from django.urls import path
from authen import views

urlpatterns = [
   path('register/', views.register_view, name='register'),
   path('login/', views.login_view, name='login'),
   path('logout/', views.my_logout, name='logout'),
   path('profile/', views.profile, name='profile'),
]
