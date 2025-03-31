from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from tracks.views import TrackViewSet

router = routers.DefaultRouter()
router.register(r'tracks', TrackViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # 👈 your API lives under /api/
]

