from flask import Flask, render_template, session
from extension import db, jwt
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///apartemen.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'IniSecretKeyYangPanjangDanSusah1234!@$'
    app.config['SECRET_KEY'] = 'rahasia-kuat-dan-unik-disini'  
    CORS(app)
    db.init_app(app)
    jwt.init_app(app)

    from routes.auth import auth_bp
    from routes.apartements import apartments_bp
    from routes.bookings import bookings_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(apartments_bp)
    app.register_blueprint(bookings_bp)
    
    # ✅ Route register (tampilan HTML)
    @app.route('/login')
    def login_page():
        return render_template('login.html')
    
    # ✅ Route register (tampilan HTML)
    @app.route('/register')
    def register_page():
        return render_template('register.html')

    # ✅ Route login (tampilan HTML)
    @app.route('/')
    def home():
        from models import User
        user = None
        if 'user_id' in session:
            user = User.query.get(session['user_id'])  # Ambil user dari database jika login
        return render_template('index.html', user=user)  # Kirim ke template

    return app


if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)

