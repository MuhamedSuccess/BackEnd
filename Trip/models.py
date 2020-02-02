from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from account.models import UserProfile


class Guide(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'guide'


class Trip(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    check_in_date = models.DateTimeField(null=False)
    check_out_date = models.DateTimeField(null=False)
    guide = models.ForeignKey(Guide, on_delete=models.CASCADE, related_name='trip')
    no_of_days = models.IntegerField()

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


class TourPlan(models.Model):
    guide = models.ForeignKey(Guide, on_delete=models.CASCADE)

    def budget(self):
        pass


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
