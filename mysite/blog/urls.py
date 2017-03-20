from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.hello, name="hello"),
    url(r'^blog/$', views.blog, name="blog"),
    url(r'^blog/post_list/$', views.post_list, name="post_list"),
    url(r'^time/$', views.current_datetime),  # /blog/time
]