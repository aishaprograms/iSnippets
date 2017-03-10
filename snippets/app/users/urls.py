from django.conf.urls import url
from . import views

#mapping urls to controllers
#think routes
#r stands for raw
#(route, which controller to go, to name of route)
urlpatterns = [
    url(r'^home/$',views.home,name='home')
]