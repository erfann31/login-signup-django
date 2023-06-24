from django.contrib import admin
from django.urls import path
from user.views import CustomUserViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'custom-users', CustomUserViewSet)

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('custom-users/teachers/', CustomUserViewSet.as_view({'get': 'teachers'}), name='teachers-list'),
                  path('custom-users/check-password/', CustomUserViewSet.as_view({'post': 'check_password'}), name='check-password'),
              ] + router.urls
