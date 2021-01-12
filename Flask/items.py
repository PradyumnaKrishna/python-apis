from flask import Blueprint, request, jsonify

# Init Blueprint
items = Blueprint('items', __name__)


@items.route('/items', methods=['POST'])
def item():
    """Main API route"""
    input_list = []

    # Error Handling if not supported POST
    try:
        for i in request.json:
            input_list.append(i)
    except TypeError:
        return jsonify(dict(status="Wrong Method"))

    # Return Data as json
    data = make_data(input_list)
    return jsonify(data)


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


if __name__ == "__main__":
    items.run(host='127.0.0.1', port=8000)
