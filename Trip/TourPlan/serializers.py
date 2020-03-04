from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from rest_framework.authtoken.models import Token

from Trip.TourPlan.models import TourPlan
from Trip.models import Tourist, Guide, Trip
from account.models import UserProfile
from account.api.serializers import ProfileSerializer, UserSerializer
from account.models import User

class TourPlanSerializer(ModelSerializer):
    class Meta:
        model = TourPlan
        fields = '__all__'
