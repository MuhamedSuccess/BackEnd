from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status, authentication
# Create your views here.
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action, permission_classes

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from Trip.models import Tourist, Guide, Trip
from .serializers import TouristSerializer, GuideSerializer, TripSerializer
from account.models import UserProfile

class TouristViewSet(viewsets.ModelViewSet):
    queryset = Tourist.objects.all()
    serializer_class = TouristSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated]


class GuideViewSet(viewsets.ModelViewSet):
    queryset = Guide.objects.all()
    serializer_class = GuideSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user = request.user
        user_obj = get_object_or_404(User, pk=user.i)
        user_obj.profile.is_guide=True
        user_obj.save()
        # print(user_obj.username)

        # user.user.profile.is_guide=True
        guide = Guide.objects.create(user=user_obj)
        serializer = GuideSerializer(guide, many=False)
        response = {'message': 'guide added Successfully', 'result': serializer.data}
        return Response(response, status=status.HTTP_200_OK)



class TripViewSet(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated]

    # @action(detail=False,methods=['POST'], permission_classes=[IsAuthenticated])
    # @permission_classes((IsAdminUser,))
    def create(self, request, *args, **kwargs):
        data = request.data
        # data['guide'] =  '1'       request.user.pk
        serializer = TripSerializer(data=data)
        data = {}
        if serializer.is_valid():
            trip = serializer.save()
            response = {'message': 'Trip added successfully', 'trip': serializer.data}
            return Response(response, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def get_permissions(self):
    #     if self.action == 'list':
    #         return [IsAuthenticated()]
    #     else:
    #         return super(self, TripViewSet).get_permissions()
