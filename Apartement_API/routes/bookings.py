# === routes/bookings.py (Versi Hybrid API + UI) ===
from flask import Blueprint, render_template, request, jsonify
from extension import db
from models import Booking
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime

bookings_bp = Blueprint('bookings', __name__, url_prefix='/booking')

# 🔐 API: Buat booking (dengan JWT)
@bookings_bp.route('/api', methods=['POST'])
@jwt_required()
def create_booking():
    data = request.get_json()
    user_id = get_jwt_identity()
    booking = Booking(
        apartment_id=data['apartment_id'],
        user_id=user_id,
        start_time=datetime.fromisoformat(data['start_time']),
        end_time=datetime.fromisoformat(data['end_time']),
        total_price=data['total_price'],
        status='confirmed'
    )
    db.session.add(booking)
    db.session.commit()
    return jsonify({'message': 'Booking created successfully'})

# 🔐 API: List booking user (dengan JWT)
@bookings_bp.route('/api', methods=['GET'])
@jwt_required()
def list_bookings():
    user_id = get_jwt_identity()
    bookings = Booking.query.filter_by(user_id=user_id).all()
    result = [
        {
            'id': b.id,
            'apartment_id': b.apartment_id,
            'start_time': b.start_time.isoformat(),
            'end_time': b.end_time.isoformat(),
            'total_price': b.total_price,
            'status': b.status
        } for b in bookings
    ]
    return jsonify(result)

# 🖼️ UI: List apartemen yang bisa dibooking
@bookings_bp.route('/', methods=['GET'])
def show_apartments():
    return render_template('booking_list.html')

# 🖼️ UI: Detail tiap apartemen + tombol WhatsApp
@bookings_bp.route('/<string:apartment_name>', methods=['GET'])
def detail_apartment(apartment_name):
    data = {
    "SENTUL_TOWER": {
        "desc": """📍 Apartemen Sentul Tower, Sentul City
Ruko STA Niaga Blok B/5, Citaringgul, Babakan Madang

✨ Paket Transit Hemat:
- 2 Jam: Rp100.000
- 3 Jam: Rp125.000
- 4 Jam: Rp165.000
- 5 Jam + 1 Jam Gratis: Rp200.000
- 7 Jam: Rp225.000

🌙 Paket Malam (21:00 - 10:00)
- Weekday: Rp170.000
- Weekend: Rp250.000

☀ Full Day (14:00 - 12:00)
- Weekday: Rp200.000
- Weekend: Rp350.000

🏢 Tersedia unit 2 BR, nyaman dan private
📲 Booking via WhatsApp: 0858-6007-9700""",
        "harga": [],
        "image_url": "/static/images/sentul_tower.jpg"
    },
    "BOGOR_VALLEY": {
        "desc": """📍 Bogor Valley Apartment
Jl. Sholeh Iskandar, Kedungbadak, Tanah Sereal, Kota Bogor

✨ Paket Transit Hemat:
- 2 Jam: Rp80.000
- 3 Jam: Rp100.000
- 4 Jam: Rp130.000
- 5 Jam + 1 Jam Gratis: Rp150.000
- 7 Jam: Rp170.000

🌙 Paket Malam (21:00 - 10:00)
- Weekday: Rp150.000
- Weekend: Rp220.000

☀ Full Day (14:00 - 12:00)
- Weekday: Rp200.000
- Weekend: Rp250.000

🏢 Tersedia unit 2 BR, nyaman dan private
📲 Booking via WhatsApp: 0858-6007-9700""",
        "harga": [],
        "image_url": "/static/images/bopal.png"
    },
    "BOGORIENZE": {
        "desc": """📍 Bogorienze Apartment
Bogor Nirwana Residence, LOT XXI, Sukamantri, Tamansari

✨ Paket Transit Hemat:
- 2 Jam: Rp80.000
- 3 Jam: Rp100.000
- 4 Jam: Rp130.000
- 5 Jam + 1 Jam Gratis: Rp170.000
- 7 Jam: Rp190.000

🌙 Paket Malam (21:00 - 10:00)
- Weekday: Rp140.000
- Weekend: Rp200.000

☀ Full Day (14:00 - 12:00)
- Weekday: Rp170.000
- Weekend: Rp230.000

🏢 Tersedia unit 2 BR, nyaman dan private
📲 Booking via WhatsApp: 0858-6007-9700""",
        "harga": [],
        "image_url": "/static/images/bogorienze.jpg"
    },
    "APARTEMEN_PODOMORO_GOLF_VIEW": {
        "desc": """📍 Podomoro Golf View Apartment
Cimanggis, dekat Masjid At-Thohir

✨ Paket Transit Hemat:
- 2 Jam: Rp80.000
- 3 Jam: Rp100.000
- 4 Jam: Rp130.000
- 5 Jam + 1 Jam Gratis: Rp150.000
- 7 Jam: Rp170.000

🌙 Paket Malam (21:00 - 10:00)
- Weekday: Rp165.000
- Weekend: Rp220.000

☀ Full Day (14:00 - 12:00)
- Weekday: Rp225.000
- Weekend: Rp250.000

🏢 Tersedia unit 2 BR, nyaman dan private
📲 Booking via WhatsApp: 0858-6007-9700""",
        "harga": [],
        "image_url": "/static/images/podomoro.jpg"
    }
}


    apt_data = data.get(apartment_name, {
        "desc": "Informasi apartemen tidak ditemukan.",
        "harga": []
    })

    return render_template('booking_detail.html',
                           name=apartment_name,
                           desc=apt_data["desc"],
                           harga=apt_data["harga"],
                           image_url=apt_data["image_url"])
