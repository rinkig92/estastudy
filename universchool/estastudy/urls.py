from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^insert/', views.insert, name='insert'),
    url(r'^(?P<pk>\d+)/update/', views.update, name='update'),
    url(r'^delete/', views.delete, name='delete'),
    url(r'^view/', views.view, name='view'),
]
