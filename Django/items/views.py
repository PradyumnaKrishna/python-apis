from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class itemsView(APIView):

    def post(self, request, format=None):
        """Handles POST Request"""

        # Validates the Data
        try:
            if isinstance(request.data, list):
                input_list = [i for i in request.data]
            else:
                return Response({"status": "Invalid List"}, status=status.HTTP_400_BAD_REQUEST)

        except TypeError:
            return Response({"status": "Wrong Method"}, status=status.HTTP_400_BAD_REQUEST)

        # Process Data
        data = make_data(input_list)
        return Response(data, status=status.HTTP_200_OK)


def make_data(input_list):
    """Process Data"""

    # if variable is positive digit then append to a list
    valid_list = [i for i in input_list if str(i).isdigit() and i > 0]

    # Data Required
    x = len(input_list)
    y = len(valid_list)

    if y == 0:
        z = min_value = max_value = 0
    else:
        z = sum(valid_list) / y
        min_value = min(valid_list)
        max_value = max(valid_list)

    # Data required in a dictionary
    data = {
        "valid_entries": y,
        "invalid_entries": x - y,
        "min": min_value,
        "max": max_value,
        "average": z
    }

    return data
