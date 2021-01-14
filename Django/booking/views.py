from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Booking
from .serializers import BookingSerializer


# Create your views here.
class bookingView(APIView):

    def get(self, request, format=None):
        bookings = Booking.objects.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data, status=200)

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        try:
            if data['slot'] > 23:
                return Response({"status": "invalid slot"}, status=400)
            if isinstance(data['name'], str) != True:
                return Response({"status": "invalid name"}, status=400)
        except KeyError:
            return Response({"status": "invalid request"}, status=400)

        serializer = BookingSerializer(data=data)

        resp = "for " + data['name'] + " in slot " + str(data['slot'])
        if Booking.objects.filter(slot=data['slot']).count() < 1:
            if serializer.is_valid():
                serializer.save()
                return Response({"status": "confirmed booking " + resp}, status=201)
            return Response(serializer.errors, status=400)
        else:
            return Response({"status": "slot full, unable to save booking " + resp}, status=400)


class cancelView(APIView):
    def post(self, request, format=None):
        data = JSONParser().parse(request)
        try:
            if data['slot'] > 23:
                return Response({"status": "invalid slot"}, status=400)
            if isinstance(data['name'], str) != True:
                return Response({"status": "invalid name"}, status=400)
        except KeyError:
            return Response({"status": "invalid request"}, status=400)

        resp = data['name'] + " in slot " + str(data['slot'])

        try:
            Booking.objects.filter(slot=data['slot'], name=data['name']).get()
        except Booking.DoesNotExist:
            return Response(dict(status="no booking for the name " + resp), status=400)
        else:
            Booking.objects.filter(slot=data['slot'], name=data['name']).delete()
            return Response(dict(status="canceled booking for " + resp), status=400)
