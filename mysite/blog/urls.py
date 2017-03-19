from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.hello, name="hello"),
    url(r'^time/$', views.current_datetime),  # /blog/time
]