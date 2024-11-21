from datetime import datetime as dt
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Booking(db.Model):
    __tablename__ = 'bookings'
    
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, nullable = False)
    service_provider_id = db.Column(db.Integer)
    service_type = db.Column(db.Integer, nullable = False)
    status = db.Column(db.Integer, nullable = False)
    scheduled_time = db.Column(db.DateTime, nullable = False)
    created_at = db.Column(db.DateTime, default = dt.now)
    updated_at = db.Column(db.DateTime, default = dt.now, onupdate = dt.now)
    
    def to_dict(self):
        return {
            'booking_id': self.id,
            'user_id': self.user_id,
            'service_provider_id': self.service_provider_id,
            'service_type': self.service_type,
            'status': self.status,
            'scheduled_time': self.scheduled_time,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }