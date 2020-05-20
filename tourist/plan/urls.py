from django.urls import path
from plan import views

urlpatterns = [
   path('', views.plan_list_view, name='listPlan'),
   path('<int:plan_id>/', views.plan_detail_view, name="plan_detail"),
   path('<int:plan_id>/edit/', views.plan_update_view, name="plan_update"),
   path('<int:plan_id>/delete/', views.plan_delete_view, name="plan_delete"),
   path('new/', views.plan_create_view, name="plan_create"),

   
]