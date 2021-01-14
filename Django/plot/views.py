from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from itertools import combinations


# Create your views here
class plotView(APIView):

    def post(self, request, format=None):
        # Error Handling if not supported POST
        data = JSONParser().parse(request)
        try:
            x = int(data['x'])
            y = int(data['y'])
        except KeyError:
            return Response({"status": "invalid request"}, status=400)

        if request.session.has_key('coord'):
            response_status = "Success "

            # if RectCoord variable exists then check its coordinates
            if request.session.has_key('RectCoord'):
                if is_rect(request.session['RectCoord']):
                    for i in range(len(request.session['RectCoord'])):
                        response_status += str(request.session['RectCoord'][i]) + " "
                    return Response({"status": response_status}, status=200)

            # Append coordinates
            coord = request.session['coord']
            coord.append([x, y])
            request.session['coord'] = coord

            # if more than 3 coordinates then check its coordinates
            if len(coord) > 3:
                coords = rect_coord(coord)
                if coords:
                    request.session['RectCoord'] = coords
                    for i in range(len(coords)):
                        response_status += str(coords[i]) + " "
                    return Response({"status": response_status}, status=200)

            return Response({"status": "accepted"}, status=200)
        else:
            c = [[x, y]]
            request.session['coord'] = c
            return Response({"status": "accepted"}, status=200)


# check for all combinations for rectangle coordinates
def rect_coord(coords):
    """find all Combinations for Rectangle Coordinates"""
    b = combinations(coords, 4)
    for i in list(b):
        if is_rect(i):
            c = []
            for j in list(i):
                c.append(j)
            return c
    else:
        return False


# Check coordinates of rectangle
def is_rect(coords):
    """Check Coordinates Creates a rectangle"""
    if len(coords) != 4:
        return False
    ca, cb, cc, cd = sorted(coords)
    return ca[0] == cb[0] and cc[0] == cd[0] and ca[1] == cc[1] and cb[1] == cd[1]
