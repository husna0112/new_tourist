
from django.urls import path

from attraction import views
from attraction.views import RatingScore

urlpatterns = [
   
   path('', views.listAttraction, name='listAttraction'),
   path('<int:attraction_id>', views.attraction_detail, name='detail'),
   path('add-to-plan/<int:attraction_id>', views.add_to_plan, name='add-to-plan'),
   path('rating-score', RatingScore.as_view, name='rating-score')

   #path(r'^attraction/detail/(?P<attraction_id>\d+)/$', views.attraction_detail, name='detail'),



 
]