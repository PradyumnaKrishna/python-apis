from flask import Flask
from items import items
import secrets

app = Flask(__name__)
app.register_blueprint(items)
app.secret_key = secrets.token_urlsafe(32)
#app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///booking.db'
#db = SQLAlchemy(app)
#ma = Marshmallow(app)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000, debug=True)
