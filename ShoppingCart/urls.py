from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^store/', views.store, name="store"),
    url(r'^rent/(?P<item_id>[0-9]+)/$', views.rent, name="rent"),
    url(r'^return/(?P<item_id>[0-9]+)/$', views.return_item, name="return"),
]
