
from django.urls import path

from attraction import views


urlpatterns = [
   
   path('', views.listAttraction, name='listAttraction'),
   path('<int:attraction_id>', views.attraction_detail, name='detail'),
   path('add-to-plan/<int:attraction_id>', views.add_to_plan, name='add-to-plan'),
   path('myplan/<int:attraction_id>', views.my_plan, name='my_plan'),

]