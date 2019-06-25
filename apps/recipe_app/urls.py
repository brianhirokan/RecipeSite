from django.conf.urls import url
from . import views

urlpatterns=[
    # url(r'^$',views.index),
    url(r'^$',views.test),
    url(r'^home$', views.home),
    url(r'^browse$', views.browse),
    url(r'^recipe/view/(?P<id>\d+)$',views.showrecipe),
    url(r'^search$',views.search)
]