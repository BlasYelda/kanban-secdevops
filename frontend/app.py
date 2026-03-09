from flask import Flask, render_template, request, redirect, url_for, session
import requests
import os

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'dev_key')
BACKEND_URL = os.getenv('BACKEND_URL', 'http://kanban-backend:5000')

@app.route('/')
def login():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/auth', methods=['POST'])
def auth():
    username = request.form.get('username')
    password = request.form.get('password')
    try:
        response = requests.post(f"{BACKEND_URL}/login", json={
            "username": username, "password": password
        }, timeout=5)

        if response.status_code == 200:
            data = response.json()
            session['username'] = data['user']['username']
            session['role'] = data['user']['role']
            return redirect(url_for('dashboard'))
        return "<h3>Error de login</h3><a href='/'>Volver</a>", 401
    except:
        return "Error de conexión con el backend", 500

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))

    role = session.get('role', 'user')
    username = session.get('username')
    
    # Configuración visual según rol
    config = {
        "role": role,
        "username": username,
        "bg_color": "#1a1a1a" if role == "admin" else "#ffffff",
        "text_color": "#e0e0e0" if role == "admin" else "#333333",
        "title": "ADMIN PANEL" if role == "admin" else "Kanban Dashboard",
        "users_list": []
    }

    # Si es admin, pedimos los usuarios al backend
    if role == "admin":
        headers = {'X-Role': 'admin'}
        res = requests.get(f"{BACKEND_URL}/debug/users", headers=headers)
        if res.status_code == 200:
            config["users_list"] = res.json().get('users', [])

    return render_template('dashboard.html', **config)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)