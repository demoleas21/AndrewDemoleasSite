"""Andrew Site URLs"""
from django.conf.urls import url
from . import views

urlpatterns = [ #pylint:  disable=invalid-name
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^/andrew/$', views.DetailView.as_view(), name='detail')
]
