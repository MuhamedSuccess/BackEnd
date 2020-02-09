from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User
from django.db import models
from rest_framework.authtoken.models import Token
# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


# from AdvancedTouristGuide import settings

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    is_tourist = models.BooleanField(default=False, null=True)
    is_guide = models.BooleanField(default=False, null=True)
    is_admin = models.BooleanField(default=False, null=True)
    city = models.CharField(max_length=200, default='', null=True, blank=True)
    phone = models.IntegerField(default=0, null=True)
    birth_date = models.DateField(null=True, verbose_name='birth date')
    avatar = models.ImageField(upload_to='images/', null=True)
    date_joined = models.DateField(null=True)
    last_login = models.DateTimeField(null=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    Country = models.CharField(max_length=50, null=True, blank=True)

    SEX_CHOICES = (
        ('F', 'Female',),
        ('M', 'Male',),
    )

    sex = models.CharField(
        max_length=1,
        choices=SEX_CHOICES,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.user.username

    def fullName(self):
        return self.first_name + ' ' + self.last_name

    def create_profile(sender, **kwargs):
        if kwargs['created']:
            user_profile = UserProfile.objects.create(user=kwargs['instance'])

    post_save.connect(create_profile, sender=User)

    # #update user profile
    # @receiver(post_save, sender=User)
    # def save_user_profile(sender, instance, **kwargs):
    #     instance.profile.save()

# class MyAccountManager(BaseUserManager):
# 	def create_user(self, email, username, password=None):
# 		if not email:
# 			raise ValueError('Users must have an email address')
# 		if not username:
# 			raise ValueError('Users must have a username')
#
# 		user = self.model(
# 			email=self.normalize_email(email),
# 			username=username,
# 		)
#
# 		user.set_password(password)
# 		user.save(using=self._db)
# 		return user
#
# 	def create_superuser(self, email, username, password):
# 		user = self.create_user(
# 			email=self.normalize_email(email),
# 			password=password,
# 			username=username,
# 		)
# 		user.is_admin = True
# 		user.is_staff = True
# 		user.is_superuser = True
# 		user.save(using=self._db)
# 		return user

# #custom user model
# class User(AbstractBaseUser):
# 	email 					= models.EmailField(verbose_name="email", max_length=60, unique=True)
# 	username 				= models.CharField(max_length=30, unique=True)
# 	date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
# 	last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
# 	is_admin				= models.BooleanField(default=False)
# 	is_active				= models.BooleanField(default=True)
# 	is_staff				= models.BooleanField(default=False)
# 	is_superuser			= models.BooleanField(default=False)
#
#
#      #objects = MyAccountManager()
#
# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)
#
