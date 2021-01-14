from django.db import models


# Create your models here.
class Booking(models.Model):
    slot = models.IntegerField(null=False, blank=False)
    name = models.CharField(max_length=50, null=False)

    def __str__(self_):
        return self.slot
