
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from contact.views import  TaskViewSet

router = routers.DefaultRouter()
router.register(r'contact', TaskViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
    url(r'^admin/', admin.site.urls),
]
