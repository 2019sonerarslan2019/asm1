from django.urls import path
from .views import revolving_door_view,create_revolving_door_view,detail_revolving_door_view
urlpatterns = [
    path('mr30/',revolving_door_view,name='mr30'),
    path('mr30/olustur/',create_revolving_door_view,name='createmr30'),
    path('mr30/detay/<id>/',detail_revolving_door_view,name='detailmr30'),
]
