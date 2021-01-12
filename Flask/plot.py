from flask import Blueprint, session, jsonify, request
from itertools import combinations

plot = Blueprint('plot', __name__)


# Add Coordinates
@plot.route('/plot', methods=['POST'])
def Plot():
    """Plotting API"""
    coord = session.get('coord')

    # Error Handling if not supported POST
    try:
        x = request.json['x']
        y = request.json['y']
    except KeyError:
        return jsonify(dict(status="invalid request"))

    # if coord variable exists
    if isinstance(coord, list):
        response_status = "Success "
        RectCoord = session.get('RectCoord')

        # if RectCoord variable exists then check its coordinates
        if isinstance(RectCoord, list):
            if is_rect(session['RectCoord']):
                for i in range(len(session['RectCoord'])):
                    response_status += str(session['RectCoord'][i]) + " "
                return jsonify(dict(status=response_status))

        # Append coordinates
        coord = session['coord']
        coord.append((x, y))
        session['coord'] = coord

        # if more than 3 coordinates then check its coordinates
        if len(coord) > 3:
            coords = rect_coord()
            if coords:
                for i in range(len(coords)):
                    response_status += str(coords[i]) + " "
                return jsonify(dict(status=response_status))

        # else return response
        return jsonify(dict(status="accepted"))
    else:
        # Not exists, create coord variable
        session['coord'] = []
        session['coord'].append((x, y))
        return jsonify(dict(status="accepted"))


# check for all combinations for rectangle coordinates
def rect_coord():
    """find all Combinations for Rectangle Coordinates"""
    b = combinations(session['coord'], 4)
    for i in list(b):
        if is_rect(i):
            c = []
            for j in list(i):
                c.append(j)
            session['RectCoord'] = c
            return session['RectCoord']
    else:
        return False


# Check coordinates of rectangle
def is_rect(coords):
    """Check Coordinates Creates a rectangle"""
    if len(coords) != 4:
        return False
    ca, cb, cc, cd = sorted(coords)
    return ca[0] == cb[0] and cc[0] == cd[0] and ca[1] == cc[1] and cb[1] == cd[1]


if __name__ == '__main__':
    plot.run(port=8000, debug=True)
