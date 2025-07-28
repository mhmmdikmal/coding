from flask import Blueprint, request, jsonify, redirect, render_template, session
from extension import db
from models import User
from flask_jwt_extended import create_access_token

auth_bp = Blueprint('auth', __name__, url_prefix='/api')

# === REGISTER ===
@auth_bp.route('/register', methods=['POST'])
def register():
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form

    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    if not name or not email or not password:
        return {"error": "Data tidak lengkap"}, 400

    if User.query.filter_by(email=email).first():
        return {"error": "Email sudah terdaftar"}, 400

    user = User(name=name, email=email)
    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    return redirect('/login')  # redirect ke tampilan login (GET)

# === LOGIN ===
@auth_bp.route('/login', methods=['POST'])
def login_auth():
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form

    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        # Simpan data user ke session
        session['user_id'] = user.id
        session['user_name'] = user.name
        # Optional: tetap buat access_token jika kamu mau pakai API juga
        access_token = create_access_token(identity=user.id)
        return redirect('/')
    else:
        return render_template('login.html', error='Email atau password salah')

# === LOGOUT ===
@auth_bp.route('/logout')
def logout():
    session.pop('user_id', None) # Hapus user_id dari session
    return redirect('/')
