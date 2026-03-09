from flask import Flask, request, jsonify
from models import db, User
import os
from functools import wraps

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # 🛡️ Control de Acceso basado en Roles (RBAC)
        # Verificamos si la cabecera X-Role indica que es admin
        user_role = request.headers.get('X-Role') 
        
        if user_role != 'admin':
            return jsonify({
                "status": "error", 
                "message": "Acceso denegado: Se requieren permisos de administrador"
            }), 403
            
        return f(*args, **kwargs)
    return decorated_function

def create_app():
    app = Flask(__name__)

    # CARGA DE CONFIGURACIÓN DESDE EL ENTORNO (.env)
    database_url = os.getenv('DATABASE_URL', 'sqlite:///fallback.db')
    secret_key = os.getenv('SECRET_KEY', 'default_unsafe_key_change_me')

    app.config.update(
        SQLALCHEMY_DATABASE_URI=database_url,
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        SECRET_KEY=secret_key
    )

    db.init_app(app)

    # Inicialización de la DB y Semillas
    with app.app_context():
        db.create_all()
        
        # Semilla: Admin
        if not User.query.filter_by(username='admin').first():
            admin = User(username='admin', role='admin')
            admin.set_password('admin123') 
            db.session.add(admin)
        
        # Semilla: Pepe
        if not User.query.filter_by(username='pepe').first():
            pepe = User(username='pepe', role='user')
            pepe.set_password('pepe123')
            db.session.add(pepe)
            
        db.session.commit()
        print("✅ Base de datos sincronizada y protegida con variables de entorno.")

    # --- RUTAS ---

    @app.route('/')
    def home():
        return {"message": "API Backend Funcionando con Base de Datos"}

    # 🛡️ Ruta protegida: Solo accesible si se envía la cabecera X-Role: admin
    @app.route('/debug/users')
    @admin_required
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
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)