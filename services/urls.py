from django.urls import path
from .views import revolving_door_view,create_revolving_door_view,detail_revolving_door_view,GeneratePDF
urlpatterns = [
    path('',revolving_door_view,name='revolvingdoor'),
    path('olustur/',create_revolving_door_view,name='createrevolvingdoor'),
    path('detay/<id>/',detail_revolving_door_view,name='detailrevolvingdoor'),
    path('detay/<id>/pdf/',GeneratePDF.as_view(),name='pdf'),
]
