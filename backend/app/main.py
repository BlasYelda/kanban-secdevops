from flask import Flask, request, jsonify
from models import db, User
import os

def create_app():
    app = Flask(__name__)

    # Configuración de rutas y base de datos
    database_url = os.getenv('DATABASE_URL', 'sqlite:///fallback.db')
    
    app.config.update(
        SQLALCHEMY_DATABASE_URI=database_url,
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        SECRET_KEY='dev_key_secdevops_2024'
    )

    db.init_app(app)

    # Inicialización de la DB (Ahora dentro de la app para que funcione)
    with app.app_context():
        db.create_all()
        # Semilla: Admin
        if not User.query.filter_by(username='admin').first():
            admin = User(username='admin', role='admin')
            admin.set_password('admin123')
            db.session.add(admin)
        
        # Semilla: Pepe (Usuario normal)
        if not User.query.filter_by(username='pepe').first():
            pepe = User(username='pepe', role='user')
            pepe.set_password('pepe123')
            db.session.add(pepe)
            
        db.session.commit()
        print("✅ Base de datos sincronizada: 'admin' y 'pepe' listos.")

    # --- RUTAS ---
    @app.route('/')
    def home():
        return {"message": "API Backend Funcionando con Base de Datos"}

    @app.route('/debug/users')
    def list_users():
        users = User.query.all()
        return {"users": [{"id": u.id, "username": u.username, "role": u.role} for u in users]}

    @app.route('/login', methods=['POST'])
    def login():
        data = request.get_json()
        if not data or not data.get('username') or not data.get('password'):
            return jsonify({"status": "error", "message": "Faltan datos"}), 400

        user = User.query.filter_by(username=data.get('username')).first()
        if user and user.check_password(data.get('password')):
            return jsonify({
                "status": "success",
                "message": "Login correcto",
                "user": {"username": user.username, "role": user.role}
            }), 200
        
        return jsonify({"status": "error", "message": "Credenciales inválidas"}), 401

    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)