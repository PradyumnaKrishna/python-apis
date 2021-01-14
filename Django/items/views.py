from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class itemsView(APIView):

    def post(self, request, format=None):
        input_list=[]
        try:
            for i in request.data:
                input_list.append(i)
        except TypeError:
            return Response({"status": "Wrong Method"}, status=status.HTTP_400_BAD_REQUEST)

        data = make_data(input_list)
        return Response(data, status=status.HTTP_200_OK)

def make_data(input_list):
    """To make data sense"""
    valid_list = []
    # if variable is positive digit then append to a list
    for i in input_list:
        if str(i).isdigit():
            if i > 0:
                valid_list.append(i)

    # Data Required
    x = len(input_list)
    y = len(valid_list)
    z = sum(valid_list)/y

    # Data required in a dictionary
    data = {
             "valid_entries": y,
             "invalid_entries": x-y,
             "min": min(valid_list),
             "max": max(valid_list),
             "average": z
           }

    return data
