from django.contrib import admin
from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from apps.defaultapp.views.youtube import YoutubeView

router = DefaultRouter()

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^url/', YoutubeView.as_view(), name="url"),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
