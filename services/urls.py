
from django.urls import path
from .views import revolving_door_view,create_revolving_door_view,detail_revolving_door_view
urlpatterns = [
    path('doner-kapi/',revolving_door_view,name='revolvingdoor'),
    path('doner-kapi/olustur/',create_revolving_door_view,name='createrevolvingdoor'),
    path('doner-kapi/detay/<id>',detail_revolving_door_view,name='detailrevolvingdoor'),

]
