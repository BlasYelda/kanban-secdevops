from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'super-secreto-para-el-trabajo'

# Simulación de "base de datos" de usuarios
USERS = {
    "admin": {"password": "123", "role": "admin"},
    "user": {"password": "123", "role": "normal"}
}

@app.route('/')
def login():
    return '''
        <form action="/auth" method="post">
            Usuario: <input name="username"><br>
            Clave: <input name="password" type="password"><br>
            <input type="submit" value="Entrar">
        </form>
    '''

@app.route('/auth', methods=['POST'])
def auth():
    username = request.form.get('username')
    password = request.form.get('password')
    
    user = USERS.get(username)
    if user and user['password'] == password:
        session['username'] = username
        session['role'] = user['role']
        return redirect(url_for('dashboard'))
    return "Login fallido"

@app.route('/dashboard')
def dashboard():
    role = session.get('role', 'normal')
    # Requisito: Si es admin, hace algo diferente 
    bg_color = "#333" if role == "admin" else "#fff"
    text_color = "white" if role == "admin" else "black"
    title = "PANEL ADMINISTRADOR" if role == "admin" else "Mis Notas"
    
    return f'''
        <body style="background-color: {bg_color}; color: {text_color};">
            <h1>{title}</h1>
            <p>Identificado como: {session.get('username')} ({role})</p>
            <hr>
            <ul><li>Nota de ejemplo 1</li></ul>
        </body>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)