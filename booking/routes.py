from flask import Blueprint, jsonify, request

from booking import db
from booking.models import User, Booking
from booking.services import find_available_provider, process_payment

booking_bp = Blueprint('booking', __name__)

@booking_bp.route('/bookings', methods = ['GET', 'POST'])
def create_booking():
    if request.method == 'GET':
        return jsonify({
            'message': 'GET Request'
        })
    
    req_data = request.get_json()
    user_id = req_data.get('user_id')
    service_type = req_data.get('service_type')
    scheduled_time = req_data.get('scheduled_time')

    user = User.query.get(user_id)

    if not user:
        return jsonify({
            'error': 'User not found!'
        }), 404
    
    provider = find_available_provider(service_type, scheduled_time)

    if not provider:
        return jsonify({
            'error': 'No available providers for this service'
        }), 404
    
    booking = Booking(
        user_id = user_id,
        service_provider_id = provider.id,
        service_type = service_type,
        scheduled_time = scheduled_time
    )
    
    payment_status = process_payment(user_id, service_type)

    if not payment_status:
        return jsonify({
            'error': 'Payment Failed'
        }), 400
    
    db.session.add(booking)
    db.session.commit()

    return jsonify({
        'message': 'Booking created successfully',
        'booking_id': booking.id
    }), 201

@booking_bp.route('/bookings/<int:booking_id>', methods = ['GET'])
def get_booking(booking_id):
    booking = Booking.query.get(booking_id)

    if not booking:
        return jsonify({
            'error': 'Booking not found'
        }), 404
    
    return jsonify({
        'user_id': booking.user_id,
        'service_provider_id': booking.service_provider_id,
        'service_type': booking.service_type,
        'scheduled_time': booking.scheduled_time,
        'status': booking.status
    })