from config import Config

from booking.models import db

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    from booking.routes import booking_bp
    app.register_blueprint(booking_bp)

    return app