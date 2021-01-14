from rest_framework import serializers
from .models import Booking

#Model Serializer
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['slot', 'name']
