from datetime import datetime as dt

from flask import Blueprint, jsonify, request

from booking import db
from booking.models import Booking

booking_bp = Blueprint('bookings', __name__, url_prefix = '/bookings')

@booking_bp.route('/', methods = ['POST'])
def create_booking():
    req_data = request.get_json()
    user_id = req_data.get('user_id')
    service_type = req_data.get('service_type')
    scheduled_time = dt.strptime(req_data.get('scheduled_time'), '%Y-%m-%d_%H-%M-%S')
    
    booking = Booking(
        user_id = user_id,
        service_type = service_type,
        status = 0,
        scheduled_time = scheduled_time
    )
    
    try:
        db.session.add(booking)
        db.session.commit()
    
    except Exception as e:
        print(e)
        
        return jsonify({
            'message': 'Booking failed!'
        }), 500
    
    return jsonify({
        'message': 'Booking created successfully',
        'booking': booking.to_dict()
    }), 201

@booking_bp.route('/user/<int:user_id>', methods = ['GET'])
def get_booking_by_user(user_id):
    user_bookings = Booking.query.filter_by(user_id = user_id).all()
    
    if not user_bookings:
        return jsonify({
            'message': 'No booking found for this user!'
        }), 404
    
    return jsonify([
        booking.to_dict() for booking in user_bookings
    ]), 200

@booking_bp.route('/<int:booking_id>', methods = ['PUT'])
def update_booking(booking_id):
    req_data = request.get_json()
    booking = Booking.query.get(booking_id)
    
    if not booking:
        return jsonify({
            'message': 'Booking not found'
        }), 404
    
    if 'service_provider_id' in req_data:
        booking.service_provider_id = req_data['service_provider_id']
    
    if 'status' in req_data:
        booking.status = req_data['status']
    
    try:
        db.session.commit()
    
    except:
        return jsonify({
            'message': 'Booking failed!'
        }), 500
    
    return jsonify({
        'message': 'Booking updated successfully!',
        'booking': booking.to_dict()
    }), 200