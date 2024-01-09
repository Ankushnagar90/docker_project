from django.urls import path, include
from dockerapp import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
""" Comment routes for testing"""
router.register('sumapi',views.SumAPI, basename='sumapi')

urlpatterns = [
    path('', include(router.urls)),
]