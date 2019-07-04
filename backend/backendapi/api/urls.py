from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import UserViewSet, BookViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]