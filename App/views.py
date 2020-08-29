from django.shortcuts import render

# Create your views here.
from .models import Quarterback,Runningback,Widereceiver,Tightend,Defense,Kicker,Player
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

from rest_framework.decorators import action

from .serializers import QuarterbacksSerializer,RunningbackSerialier,WidereceiverSerializer,TightendSerializer,DefenseSerializer,KickerSerializer,PlayerSerializer,UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class QuarterbackViewSet(viewsets.ModelViewSet):
    serializer_class = QuarterbacksSerializer
    queryset = Quarterback.objects.all()
    #
    # @action( detail = True, methods = ['GET'])
    # def get_qb(self,request,id=None):
    #     if 'id' in request.data:
    #         player = Quarterback.objects.retrieve(id=id)
    #         return player.name

class SingleQBViewSet(viewsets.ModelViewSet):
    serializer_class = QuarterbacksSerializer
    def qb(self, request, id):
        obj = Quarterback.objects.get(id=id)
        return obj




class RunningbackViewSet(viewsets.ModelViewSet):
    serializer_class = RunningbackSerialier
    queryset = Runningback.objects.all()

class WidereceiverViewSet(viewsets.ModelViewSet):
    serializer_class = WidereceiverSerializer
    queryset = Widereceiver.objects.all()

class TightendViewSet(viewsets.ModelViewSet):
    serializer_class = TightendSerializer
    queryset = Tightend.objects.all()

class DefenseViewSet(viewsets.ModelViewSet):
    serializer_class = DefenseSerializer
    queryset = Defense.objects.all()

class KickerViewSet(viewsets.ModelViewSet):
    serializer_class = KickerSerializer
    queryset = Kicker.objects.all()

class PlayerViewSet(viewsets.ModelViewSet):
    serializer_class =  PlayerSerializer

    def get_queryset(self):
        authentication_classes = (TokenAuthentication,)
        permission_classes = (IsAuthenticated,)
        queryset = Player.objects.all()
        pos = self.request.query_params.get('position',None)
        if pos is not None:
            queryset = queryset.filter(position=pos)
        return queryset



