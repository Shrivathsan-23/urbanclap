from datetime import datetime as dt
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique = True)

class ServiceProvider(db.Model):
    __tablename__ = 'service_providers'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    available = db.Column(db.Boolean, default = True)
    service_type = db.Column(db.String(100))

class Booking(db.Model):
    __tablename__ = 'bookings'

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    service_provider_id = db.Column(db.Integer, db.ForeignKey('service_providers.id'))
    service_type = db.Column(db.String(100))
    status = db.Column(db.String(50), default = 'pending')
    scheduled_time = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default = dt.now())

    user = db.relationship('User', backref = db.backref('bookings', lazy = True))
    service_provider = db.relationship('ServiceProvider', backref = db.backref('bookings', lazy = True))