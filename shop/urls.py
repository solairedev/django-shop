from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.shop_list, name='shop_list'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.shop_detail, name='shop_detail')
    ]