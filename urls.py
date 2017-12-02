from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<uuid>[0-9A-Fa-f-]+)/$', views.check, name='check'),
]
