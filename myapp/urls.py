
from django.contrib import admin
from django.urls import path,include
from home.views import home_view,view_401
from services.views import revolving_door_view
from user.views import login_view,logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view,name='home'),
    path('giris/',login_view,name='login'),
    path('cikis/',logout_view,name="logout"),
    path('401/',view_401,name='401'),
    path('',include('services.urls')),
]
