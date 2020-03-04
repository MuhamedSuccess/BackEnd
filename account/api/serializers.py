from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.authtoken.models import Token
from account.models import User, UserProfile


class ProfileSerializer(ModelSerializer):
    id = serializers.IntegerField(required=False)
    password = serializers.IntegerField(required=False)
    class Meta:
        model = UserProfile
        exclude = ('user', 'last_login', 'date_joined')
        # fields = '__all__'  # ['id', 'username', 'password', 'is_admin', 'is_guide']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

        read_only_fields = ['user']


class UserSerializer(ModelSerializer):
    profile = ProfileSerializer(required=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'profile']
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

    # def update(self, instance, validated_data):
    #     password = validated_data.pop('password', None)
    #     user = self.update(instance, validated_data)
    #
    #     if password:
    #         user.set_password(password)
    #         user.save()
    #
    #     return user



    def partial_update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        # user = self.partial_update(instance, validated_data)

        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)

        profile_data = validated_data.pop('profile')
        profile = UserProfile.objects.get(user=instance.id)
        # profile.first_name = profile_data.first_name
        # profile.last_name = profile_data.last_name

        pro = UserProfile.objects.get(user=instance.id)

        pro.first_name = profile_data.get('first_name', pro.first_name)
        pro.last_name = profile_data.get('first_name', pro.last_name)
        pro.is_guide = profile_data.get('is_guide', pro.is_guide)
        pro.is_tourist = profile_data.get('is_tourist', pro.is_tourist)
        pro.is_admin = profile_data.get('is_admin', pro.is_admin)
        pro.city = profile_data.get('city', pro.city)
        pro.birth_date = profile_data.get('birth_date', pro.birth_date)
        # user.profile = profile_data
        if password:
            instance.set_password(password)
            instance.save()
            pro.save()

        return instance

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
