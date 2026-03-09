from flask import Flask, request, jsonify
from models import db, User, Task 
import os
from functools import wraps
from flask_cors import CORS

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
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
    CORS(app)

    database_url = os.getenv('DATABASE_URL', 'sqlite:///fallback.db')
    secret_key = os.getenv('SECRET_KEY', 'default_unsafe_key_change_me')

    app.config.update(
        SQLALCHEMY_DATABASE_URI=database_url,
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        SECRET_KEY=secret_key
    )

    db.init_app(app)

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

        # Semilla: Tarea de ejemplo (opcional)
        if not Task.query.first():
            task = Task(title="Configurar Postman", description="Hacer pruebas de API", status="Doing")
            db.session.add(task)
            
        db.session.commit()
        print("Base de datos sincronizada y protegida con variables de entorno.")

    # --- RUTAS DE USUARIO ---

    @app.route('/')
    def home():
        return {"message": "API Backend Funcionando con Base de Datos"}

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

    # --- RUTAS DE TAREAS (KANBAN) ---

    @app.route('/tasks', methods=['GET'])
    def get_tasks():
        tasks = Task.query.all()
        return jsonify([t.to_dict() for t in tasks])

    @app.route('/tasks', methods=['POST'])
    def add_task():
        data = request.get_json()
        if not data or 'title' not in data:
            return jsonify({"status": "error", "message": "Falta el título"}), 400
        
        new_task = Task(
            title=data['title'], 
            description=data.get('description', ''),
            status=data.get('status', 'To Do'),
            user_id=data.get('user_id') # Opcional por ahora
        )
        db.session.add(new_task)
        db.session.commit()
        return jsonify(new_task.to_dict()), 201

    @app.route('/tasks/<int:id>', methods=['DELETE'])
    @admin_required # 🛡️ Solo los admins pueden borrar tareas
    def delete_task(id):
        task = Task.query.get(id)
        if not task:
            return jsonify({"status": "error", "message": "Tarea no encontrada"}), 404
        db.session.delete(task)
        db.session.commit()
        return jsonify({"status": "success", "message": "Tarea eliminada"}), 200

    return app

app = create_app()

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)