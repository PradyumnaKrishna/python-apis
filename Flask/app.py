from flask import Flask
from items import items
from booking import booking
from plot import plot
from database import db, ma
import secrets

app = Flask(__name__)
app.register_blueprint(items)
app.register_blueprint(booking)
app.register_blueprint(plot)

app.secret_key = secrets.token_urlsafe(32)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///booking.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
ma.init_app(app)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)
