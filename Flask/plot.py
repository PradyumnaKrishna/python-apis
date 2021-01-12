from flask import Blueprint, session, jsonify, request
from itertools import combinations

plot = Blueprint('plot', __name__)


@plot.route('/plot', methods=['POST'])
def Plot():
    """Plotting API"""
    coord = session.get('coord')
    try:
        x = request.json['x']
        y = request.json['y']
    except KeyError:
        return jsonify(dict(status="invalid axis"))

    if isinstance(coord, list):
        response_status = "Success "
        RectCoord = session.get('RectCoord')
        if isinstance(RectCoord, list):
            if isRect(session['RectCoord']):
                for i in range(len(session['RectCoord'])):
                    response_status += str(session['RectCoord'][i]) + " "
                return jsonify(dict(status=response_status))

        coord = session['coord']
        coord.append((x, y))
        session['coord'] = coord

        if len(coord) > 3:
            coords = RectCoords()
            if coords:
                for i in range(len(coords)):
                    response_status += str(coords[i]) + " "
                return jsonify(dict(status=response_status))

        return jsonify(dict(status="accepted"))
    else:
        session['coord'] = []
        session['coord'].append((x, y))
        return jsonify(dict(status="accepted"))


def RectCoords():
    """find all Combinations for Rectangle Coordinates"""
    b = combinations(session['coord'], 4)
    for i in list(b):
        if isRect(i):
            RectCoord = []
            for j in list(i):
                RectCoord.append(j)
            session['RectCoord'] = RectCoord
            return session['RectCoord']
    else:
        return False


def isRect(coords):
    """Check Coordinates Creates a rectangle"""
    if len(coords) != 4:
        return False
    tA, tB, tC, tD = sorted(coords)
    return tA[0] == tB[0] and tC[0] == tD[0] and tA[1] == tC[1] and tB[1] == tD[1]


if __name__ == '__main__':
    plot.run(port=8000, debug=True)
