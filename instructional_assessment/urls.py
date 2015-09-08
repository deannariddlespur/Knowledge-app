from django.conf.urls import url

from .views import Index, Detail

urlpatterns = [
    url(r'^$', Index.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', Detail.as_view(), name='detail'),
]
