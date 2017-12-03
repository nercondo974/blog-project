"""projet URL Configuration"""

from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from articleRS import views


router = routers.DefaultRouter()
router.register(r'articles', views.ArticleViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
]
