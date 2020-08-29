from django.urls import path,include
from rest_framework import routers
from .models import Quarterback
from .views import QuarterbackViewSet,RunningbackViewSet,WidereceiverViewSet,TightendViewSet,DefenseViewSet,KickerViewSet,UserViewSet,PlayerViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('quarterback',QuarterbackViewSet)
router.register('runningback',RunningbackViewSet)
router.register('widereceiver',WidereceiverViewSet)
router.register('tightend',TightendViewSet)
router.register('defense',DefenseViewSet)
router.register('kicker',KickerViewSet)
router.register('player',PlayerViewSet,basename=PlayerViewSet)
router.register('user',UserViewSet)

urlpatterns = [
    path('', include(router.urls))
]