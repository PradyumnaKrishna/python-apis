from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from itertools import combinations


# Create your views here
class plotView(APIView):

    def post(self, request, format=None):
        """Handles POST request"""

        data = JSONParser().parse(request)

        # Validates the request
        try:
            x = int(data['x'])
            y = int(data['y'])
        except KeyError:
            return Response({"status": "invalid request"}, status=400)

        # Checks coord variable exists in session
        if request.session.has_key('coord'):
            response_status = "Success "

            # Checks RectCoord variable exists
            if request.session.has_key('RectCoord'):
                rect = request.session['RectCoord']

                # Check coordinates creates a Rectangle
                if is_rect(rect):
                    for i in range(len(rect)):
                        response_status += f"{rect[i]} "

                    return Response({"status": response_status}, status=200)

            # Append coordinates
            coord = request.session['coord']
            coord.append([x, y])
            request.session['coord'] = coord

            # if more than 3 coordinates then check its coordinates
            if len(coord) > 3:
                coords = rect_coord(coord)

                # if coordinates of rectangle
                if coords:
                    request.session['RectCoord'] = coords
                    for i in range(len(coords)):
                        response_status += f"{coords[i]} "

                    return Response({"status": response_status}, status=200)

            return Response({"status": "accepted"}, status=200)

        else:
            # Creates coord variable in session
            request.session['coord'] = [[x, y]]
            return Response({"status": "accepted"}, status=200)


# check for all combinations for rectangle coordinates
def rect_coord(coords):
    """find all Combinations for Rectangle Coordinates"""

    # Finds all combinations
    b = combinations(coords, 4)

    # For all combinations in list
    for i in list(b):

        # if rectangle
        if is_rect(i):
            c = [j for j in list(i)]
            return c

    else:
        return False


# Check coordinates of rectangle
def is_rect(coords):
    """Check Coordinates"""

    if len(coords) != 4:
        return False

    # sort coordinates
    ca, cb, cc, cd = sorted(coords)
    return ca[0] == cb[0] and cc[0] == cd[0] and ca[1] == cc[1] and cb[1] == cd[1]
