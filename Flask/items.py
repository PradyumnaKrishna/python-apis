from flask import Blueprint, request, jsonify
import json

items = Blueprint('items', __name__)


@items.route('/items', methods=['POST'])
def item():
    list = []
    for i in request.json:
        list.append(i)

    data = make_data(list)
    return jsonify(data)


def make_data(list):
    valid_list = []
    for items in list:
        if str(items).isdigit():
            if items > 0:
                valid_list.append(items)

    x = len(list)
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
