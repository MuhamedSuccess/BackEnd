from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
# from api.models import Movie, Rating
from Trip.TourPlan.models import TourPlan
from Trip.models import Trip, Tourist, Guide, Schedule, Location, Tourism_Type

admin.site.register(Trip)
admin.site.register(TourPlan)
admin.site.register(Schedule)

admin.site.register(Tourist)
admin.site.register(Guide)
admin.site.register(Location)
admin.site.register(Tourism_Type)
# admin.site.register(Rating)
