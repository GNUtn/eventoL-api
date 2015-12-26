from django.conf.urls import include, url
from rest.router import router


urlpatterns = [
    url(r'^', include(router.urls)),
]
