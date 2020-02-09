from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes

from rest_framework.authtoken.models import Token
from rest_framework.views import APIView

from .serializers import UserSerializer, ProfileSerializer
from account.models import UserProfile


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserPartialUpdateView(GenericAPIView, UpdateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class ProfileViewSet(generics.ListCreateAPIView, generics.UpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer
    # authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated]


class ProfileUpdateAPIView(generics.UpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer
    # authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'


class ProfileDetailsAPIView(generics.RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer
    # authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

    # def get_object(self):
    #     queryset = self.filter_queryset(self.get_queryset())
    #     # make sure to catch 404's below
    #     obj = queryset.get(pk=self.request.user.id)
    #     self.check_object_permissions(self.request, obj)
    #     return obj


class ManageUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated]

    def get_object(self):
        """ Retrieve and the authenticated user """
        return self.request.user


@api_view(['POST', ])
@permission_classes([])
@authentication_classes([])
def login(request):
    context = {}

    user = eval(request.body)

    username = user['username']
    password = user['password']

    account = authenticate(username=username, password=password)
    if account:
        try:
            token = Token.objects.get(user=account)
        except Token.DoesNotExist:
            token = Token.objects.create(user=account)
        context['response'] = 'Successfully authenticated.'
        context['id'] = account.pk
        context['username'] = username.lower()
        context['token'] = token.key
    else:
        context['response'] = 'Error'
        context['error_message'] = 'Invalid credentials'

    return Response(context)

# @api_view(['POST', ])
# def registration_view(request):
#     if request.method == 'POST':
#         data = {}
#         serializer = RegistrationSerializer(data=request.data)
#
#         if serializer.is_valid():
#             user = serializer.save()
#             data['response'] = 'successfully registered new user.'
#             data['email'] = user.email
#             data['username'] = user.username
#             data['id'] = user.pk     #data['pk'] = user.pk
#             token = Token.objects.get(user=user).key
#             data['token'] = token
#         else:
#             data = serializer.errors
#         return Response(data)
#
