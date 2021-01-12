from flask import Blueprint, request, jsonify
from database import db, ma

# Init Blueprint
booking = Blueprint('booking', __name__)


# Product Class/Model
class Booked(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    slot = db.Column(db.Integer)
    name = db.Column(db.String(25), unique=True)

    def __init__(self, slot, name):
        self.slot = slot
        self.name = name


# Booking Schema
class BookingSchema(ma.Schema):
    class Meta:
        fields = ('slot', 'name')


# Init schema
booking_schema = BookingSchema()
bookings_schema = BookingSchema(many=True)


# create a Booking
@booking.route('/booking', methods=['POST'])
def add_booking():
    """Add booking"""
    # Error Handling if not supported POST
    try:
        slot = request.json['slot']
        name = request.json['name']
    except KeyError:
        return jsonify(dict(status="invalid request"))

    # Not more than 24 hours
    if slot > 23:
        return jsonify(dict(status="Invalid Slot"))
    else:
        # Booked slot not more than 2
        if Booked.query.filter_by(slot=slot).count() < 2:
            # Add Booking
            new_booking = Booked(slot, name)

            db.session.add(new_booking)
            db.session.commit()

            # Return response
            return jsonify(dict(status="confirmed booking for " + name + " in slot " + str(slot)))
        else:
            return jsonify(dict(status="slot full, unable to save booking for " + name + " in slot " + str(slot)))


# Get all Bookings
@booking.route('/booking', methods=['GET'])
def get_bookings():
    """Get all bookings"""
    # Get all Bookings
    all_products = Booked.query.all()
    result = bookings_schema.dump(all_products)

    # Return response
    return jsonify(result)


# Delete Booking
@booking.route('/cancel', methods=['POST'])
def delete_booking():
    """Delete booking"""
    # Error Handling if not supported POST
    try:
        slot = request.json['slot']
        name = request.json['name']
    except KeyError:
        return jsonify(dict(status="invalid request"))

    # Check if given slot and name exists
    exists = Booked.query.filter_by(slot=slot, name=name).scalar() is not None
    if exists:
        # Delete such row
        Booked.query.filter_by(slot=slot, name=name).delete()
        db.session.commit()

        # Return response
        return jsonify(dict(status="canceled booking for " + name + " in slot " + str(slot)))

    return jsonify(dict(status="no booking for the name " + name + " in slot " + str(slot)))


# run server
if __name__ == '__main__':
    booking.run(host='127.0.0.1', port=8000, debug=True)
