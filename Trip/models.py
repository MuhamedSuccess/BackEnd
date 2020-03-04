from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from Trip.TourPlan.models import TourPlan
from account.models import UserProfile


# from Trip.TourPlan.models import TourPlan


class Guide(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')

    def __str__(self):
        return self.user.username

    # class Meta:
    #     db_table = 'guide'


class Tourism_Type(models.Model):
    name = models.CharField(max_length=15)


def upload_path(instance, filname):
    return '/'.join(['covers', str(instance.name), filname])


class Trip(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    trip_cover = models.FileField(upload_to=upload_path)
    cost = models.IntegerField(null=True)
    date = models.DateTimeField(null=True)
    days = models.IntegerField(default=0)
    # adults = models.IntegerField(default=0)
    # children = models.IntegerField(default=0)
    trip_plan = models.ForeignKey(TourPlan, on_delete=models.CASCADE)
    tourism_type = models.ForeignKey(Tourism_Type, on_delete=models.CASCADE)
    guide = models.ForeignKey(Guide, on_delete=models.CASCADE, related_name='trip')

    class Meta:
        db_table = 'trip'

    def no_of_tourists(self):
        tourists = Tourist.objects.filter(trip=self)
        return len(tourists)

    def no_of_ratings(self):
        ratings = Rating.objects.filter(trip=self)
        return len(ratings)

    def avg_ratings(self):
        sum = 0
        ratings = Rating.objects.filter(trip=self)
        for rating in ratings:
            sum += rating.stars

        if len(ratings) > 0:
            return sum / len(ratings)
        else:
            return 0

    def __str__(self):
        return self.name


class Rating(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1),
                                            MaxValueValidator(5)])


class Tourist(models.Model):
    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    guide = models.ForeignKey(Guide, on_delete=models.CASCADE)  # one-to-many
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tourist'


class Location(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.IntegerField()

    def locationImages(self):
        pass


class Schedule(models.Model):
    check_in_date = models.DateTimeField(null=False)
    check_out_date = models.DateTimeField(null=False)
    event = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    date = models.DateTimeField(blank=True, null=True, default=None)
