from flask import Flask, render_template, request, redirect, url_for, session
import requests  # Importante para hablar con el backend

app = Flask(__name__)
app.secret_key = 'super-secreto-para-el-trabajo'

# La URL de tu API Backend dentro de la red de Docker
BACKEND_URL = "http://kanban-backend:5000"

@app.route('/')
def login():
    return '''
        <h2>Acceso al Tablero Kanban</h2>
        <form action="/auth" method="post">
            Usuario: <input name="username"><br>
            Clave: <input name="password" type="password"><br><br>
            <input type="submit" value="Entrar">
        </form>
    '''

@app.route('/auth', methods=['POST'])
def auth():
    username = request.form.get('username')
    password = request.form.get('password')
    
    # Enviamos los datos al Backend real
    try:
        response = requests.post(f"{BACKEND_URL}/login", json={
            "username": username,
            "password": password
        }, timeout=5)

        if response.status_code == 200:
            data = response.json()
            session['username'] = data['user']['username']
            session['role'] = data['user']['role']
            return redirect(url_for('dashboard'))
        else:
            return "<h3>Login fallido: Usuario o contraseña incorrectos en la DB.</h3><a href='/'>Volver</a>"
            
    except requests.exceptions.ConnectionError:
        return "<h3>Error: No se pudo conectar con el Backend de la Base de Datos.</h3>"

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))

    role = session.get('role', 'user')
    bg_color = "#333" if role == "admin" else "#f4f4f4"
    text_color = "white" if role == "admin" else "black"
    title = "PANEL ADMINISTRADOR" if role == "admin" else "Tablero Kanban de Usuario"
    
    return f'''
        <body style="background-color: {bg_color}; color: {text_color}; font-family: sans-serif;">
            <h1>{title}</h1>
            <p>Sesión activa: <b>{session.get('username')}</b> (Perfil: {role})</p>
            <hr>
            <h3>Tus Tareas:</h3>
            <ul><li>[Ejemplo] Configurar Persistencia SQLite ✅</li></ul>
            <br>
            <a href="/logout" style="color: {text_color};">Cerrar Sesión</a>
        </body>
    '''

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)