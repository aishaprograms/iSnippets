from django.conf.urls import url
from . import views
#mapping urls to controllers
#(route, which controller to go, to name of route)
app_name = 'snippets'

urlpatterns = [
    url(r'^$',views.SnippetListView.as_view(),name='home'),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.SnippetDetailView.as_view(), name='detail'),
    url(r'^add/$', views.add, name='add'),
]