from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from rest_framework.authtoken.models import Token

from Trip.models import Tourist, Guide, Trip, Tourism_Type
from account.models import UserProfile
from account.api.serializers import ProfileSerializer, UserSerializer
from account.models import User


class TouristSerializer(ModelSerializer):
    class Meta:
        model = Tourist
        fields = '__all__'


class TripSerializer(ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'

        depth= 1

        # fields = [
        #     'id',
        #     'name',
        #     'description',
        #     'check_in_date',
        #     'check_out_date',
        #     'no_of_ratings',
        #     'avg_ratings',
        #     'no_of_days',
        #     'guide',
        # ]


class TourismTypeSerializer(ModelSerializer):
    class Meta:
        model = Tourism_Type
        fields = '__all__'


class GuideSerializer(ModelSerializer):
    trip = TripSerializer(required=False, many=True)
    # profile = ProfileSerializer(required=False)
    user = UserSerializer(required=False)
    class Meta:
        model = Guide
        fields = ['id', 'trip', 'user']

    # def save(self, **kwargs):
    #     # # profile = validated_data.pop('profile', None)
    #     # profile_data = validated_data.pop('user')
    #     # profile = UserProfile.objects.update(
    #     #     # user=profile_data['user'],
    #     #     is_guide=True
    #     #     # etc...
    #     # )
    #
    #     guide = Guide(
    #         user=
    #     )
    #     guide.user.profile.is_guide = True
    #     guide.save()
    #     guide = Guide.objects.create()
    #     return guide
