from django.db import models


class TourPlan(models.Model):
    # guide = models.ForeignKey(guide, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True)
    schedule = models.ForeignKey('Trip.Schedule', on_delete=models.CASCADE)

    def budget(self):
        pass

    def __str__(self):
        return self.name
