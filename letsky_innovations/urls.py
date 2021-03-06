from django.conf.urls import url, include
from django.contrib import admin

from views import *

urlpatterns = [
    url(r'^accounts/', include('allauth.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name="home"),
    url(r'^download_firmware', download_firmware, name="download_firmware"),
    url(r'^send_geoinfo/(?P<device_id>[\w]+)$', send_geoinfo, name="send_geoinfo"),    
    url(r'^get_schedule/(?P<device_id>[\w]+)$', get_schedule, name="get_schedule"),
    url(r'^get_pattern/(?P<device_id>[\w]+)$', get_pattern, name="get_pattern"),
]
