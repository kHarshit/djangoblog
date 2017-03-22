from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.hello, name="hello"),
    # url(r'^blog/$', views.blog, name="blog"),
    url(r'^blog/$', views.post_list, name="post_list"),
    # url(r'^blog/post/(?P<pk>\d+)/$', views.post_list, name="post_detail"),
    url(r'^time/$', views.current_datetime),  # /blog/time
]