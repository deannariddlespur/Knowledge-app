from django.conf.urls import include, url
from django.contrib import admin

from instructional_assessment import urls as ia_urls
from instructional_assessment.views import Profile

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^profile/(?P<pk>[0-9]+)/$', Profile.as_view()),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^', include(ia_urls)),
]
