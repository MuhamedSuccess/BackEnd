from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from Trip.TourPlan.models import TourPlan
from Trip.TourPlan.serializers import TourPlanSerializer


class TourPlanViewSet(viewsets.ModelViewSet):
    queryset = TourPlan.objects.all()
    serializer_class = TourPlanSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated]
