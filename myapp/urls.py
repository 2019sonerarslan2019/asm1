
from django.contrib import admin
from django.urls import path,include
from home.views import home_view
from services.views import revolving_door_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view,name='home'),
    path('',include('services.urls')),
]
