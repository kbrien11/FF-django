from django.shortcuts import render

# Create your views here.
from .models import Quarterback,Runningback,Widereceiver,Tightend,Defense,Kicker,Player
from rest_framework import viewsets,generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.views import Response
from rest_framework.decorators import action




from .serializers import QuarterbacksSerializer,RunningbackSerialier,WidereceiverSerializer,TightendSerializer,\
    DefenseSerializer,KickerSerializer,PlayerSerializer,UserSerializer


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
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Player.objects.all()


    def get_queryset(self):
        queryset = Player.objects.all()
        user = self.request.query_params.get('user',None)
        if user is not None:
            queryset = queryset.filter(user=user)
        return queryset

    # @action(detail=True, methods='PUT')
    # def draft(self, request):
    #     serializer_class = DraftSerializer
    #     instance = Player.objects.all()
    #     output = instance.objects.filter(user=request.data['user'])
    #     output.is_drafted = True
    #     if output.is_valid():
    #         output.save()
    #         return Response({"message": "mobile number updated successfully"})
    #
    #     else:
    #         return Response({"message": "failed", "details": output.errors})

class ExampleUpdateView(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    @action(detail=True, methods='PUT')
    def draft(self,request,*args, **kwargs):
        instance = Player.objects.all()
        output = instance.objects.filter(user=kwargs['user'],id=kwargs['name'])
        output.is_drafted=True
        if output.is_valid():
            output.save()
            return Response({"message": "mobile number updated successfully"})

        else:
            return Response({"message": "failed", "details": output.errors})

    #
    # def put(self, request,format=None):
    #     drafted = Player.objects.filter(user = request.data['user'],name=request.data['name'])
    #     drafted.is_drafted=True
    #     drafted.save()
    #     serializer = PlayerSerializer(drafted)
    #     return serializer

#
# class RosterViewSet(viewsets.ModelViewSet):
#     serializer_class = RosterSerializer
#     queryset = Roster.objects.all()
#
#     def create(self,request):
#         serializer_class = RosterSerializer(data=request.data)
#         if serializer_class.is_valid():
#             serializer_class.save()
#             return Response(serializer_class.data, status=status.HTTP_201_CREATED)
#         return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def get_queryset(self):
#         queryset = Roster.objects.all()
#         user = self.request.query_params.get('user',None)
#         if user is not None:
#             queryset = queryset.filter(user=user)
#         return queryset


