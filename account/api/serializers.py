from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.authtoken.models import Token
from account.models import User, UserProfile


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        exclude = ('user', 'last_login', 'date_joined')
        # fields = '__all__'  # ['id', 'username', 'password', 'is_admin', 'is_guide']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}


class UserSerializer(ModelSerializer):
    profile = ProfileSerializer(required=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'profile']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    # overwrite create method and register new user
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        # create token for that user
        token = Token.objects.create(user=user)

        # for user in User.objects.all():
        # Token.objects.get_or_create(user=user)
        print(token.key)
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = self.update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user

# class RegistrationSerializer(serializers.ModelSerializer):
#     password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
#
#     class Meta:
#         model = User
#         fields = ['email', 'username', 'password', 'password2']
#         extra_kwargs = {
#             'password': {'write_only': True},
#         }
#
#     def save(self):
#         user = User(
#             email=self.validated_data['email'],
#             username=self.validated_data['username']
#         )
#
#         password = self.validated_data['password']
#         password2 = self.validated_data['password2']
#
#         if password != password2:
#             raise serializers.ValidationError({'password': 'Passwords don not match.'})
#         user.set_password(password)
#         user.save()
#         return user
#
#
#
#
#
# class LoginSerializer(ModelSerializer):
#     token = Char
