from flask import Blueprint, jsonify, request
from extension import db
from models import Apartment

apartments_bp = Blueprint('apartments', __name__, url_prefix='/api')

@apartments_bp.route('/apartments', methods=['GET'])
def get_apartments():
    query = Apartment.query
    location = request.args.get('location')
    price = request.args.get('price')
    if location:
        query = query.filter_by(location=location)
    if price:
        query = query.filter(Apartment.price_per_day <= int(price))
    apartments = query.all()
    result = [
        {
            'id': apt.id,
            'name': apt.name,
            'location': apt.location,
            'price_per_day': apt.price_per_day,
            'description': apt.description,
            'image_url': apt.image_url
        } for apt in apartments
    ]
    return jsonify(result)

@apartments_bp.route('/apartments/<int:id>', methods=['GET'])
def get_apartment(id):
    apt = Apartment.query.get_or_404(id)
    return jsonify({
        'id': apt.id,
        'name': apt.name,
        'location': apt.location,
        'price_per_hour': apt.price_per_hour,
        'price_per_day': apt.price_per_day,
        'description': apt.description,
        'image_url': apt.image_url
    })

# Fungsi:
# - Menampilkan daftar dan detail apartemen
# - Mendukung filter berdasarkan lokasi dan harga