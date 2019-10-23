from django.conf.urls import url
from django.conf import settings
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name="post_list"),
    url(r'^post/(?P<pk>\w+)/?', views.post_single, name="post_single"),
]