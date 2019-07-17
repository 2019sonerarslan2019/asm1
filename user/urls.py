
from django.urls import path
from user.views import history_view,mr30_history_view,mr30_update_views,mr30_delete_views

urlpatterns = [
    path('',history_view,name="history"),
    path('mr30/',mr30_history_view,name='mr30_history'),
    path('mr30/guncelle/<id>',mr30_update_views,name='updatemr30'),
    path('mr30/sil/<id>',mr30_delete_views,name='deletemr30'),

]
