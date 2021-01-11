from flask import Blueprint, request, jsonify
import json

items = Blueprint('items', __name__)


@items.route('/items', methods=['POST'])
def item():
    input_list = []
    for i in request.json:
        input_list.append(i)

    data = make_data(input_list)
    return jsonify(data)


def make_data(input_list):
    valid_list = []
    for i in input_list:
        if str(i).isdigit():
            if i > 0:
                valid_list.append(i)

    x = len(input_list)
    y = len(valid_list)
    z = sum(valid_list)/y

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
