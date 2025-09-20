from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'menu', views.MenuViewSet)
router.register(r'booking/tables', views.BookingViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('', include(router.urls)),
]