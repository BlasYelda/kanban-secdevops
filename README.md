# 📋 Kanban Board - SecDevOps Project

Este es un proyecto de tablero Kanban desarrollado bajo una metodología SecDevOps, integrando análisis de seguridad automatizado (SAST), despliegue resiliente en contenedores y cifrado de tráfico TLS mediante un Proxy Inverso. 🚀

---

## 🚀 1. Cómo ejecutar el proyecto

Este proyecto utiliza Docker Compose para orquestar los microservicios. La arquitectura está diseñada para que el usuario solo interactúe con el Proxy Seguro, manteniendo el Backend y la BD aislados en una red privada.

### 🛠️ Prerrequisitos

- Docker Desktop
- Git

### 🏁 Pasos para el despliegue

**1. Clona el repositorio:**

```bash
git clone <url-de-tu-repositorio>
cd kanban-secdevops
```

**2. Genera los certificados SSL (Autofirmados):**

Si no tienes `openssl` instalado localmente, ejecuta este comando universal de Docker para generar los archivos necesarios en la carpeta correcta:

```bash
# En Bash / Zsh / Linux / Mac:
docker run --rm -v $(pwd)/nginx/certs:/export alpine/openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /export/selfsigned.key -out /export/selfsigned.crt -subj "/C=ES/ST=Madrid/L=Madrid/O=SecDevOps/OU=IT/CN=localhost"

# En PowerShell (Windows):
docker run --rm -v ${PWD}/nginx/certs:/export alpine/openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /export/selfsigned.key -out /export/selfsigned.crt -subj "/C=ES/ST=Madrid/L=Madrid/O=SecDevOps/OU=IT/CN=localhost"
```

**3. Levanta el entorno (Modo Seguro):**

```bash
docker compose down -v
docker compose up --build -d
```

**4. Acceso:**

Abre tu navegador en `https://localhost`. *(Acepta el aviso de seguridad del certificado autofirmado para entrar).*

---

## 🔑 2. Gestión de Usuarios y Seguridad

### 👤 Credenciales de Aplicación

| Rol | Usuario | Contraseña |
|---|---|---|
| Administrador | `admin` | `admin123` |
| Usuario Estándar | `pepe` | `pepe123` |

### 🛡️ Seguridad Implementada

- **Tráfico Cifrado (HTTPS):** Uso de Nginx como Proxy Inverso con protocolos TLS v1.2/v1.3.
- **Hashing de Contraseñas:** Almacenamiento seguro en MySQL usando `PBKDF2` con salt (Werkzeug).
- **RBAC (Role-Based Access Control):** Decoradores `@admin_required` en el backend que validan cabeceras de rol para acciones críticas.
- **Hardening de Red:** Solo los puertos 80/443 están expuestos; el Backend y la DB son invisibles desde el exterior.

---

## 🤖 3. Automatización CI/CD (GitHub Actions)

El proyecto incluye un pipeline de integración continua que valida cada cambio automáticamente:

- **SAST (Bandit):** Escaneo estático del código Python para detectar vulnerabilidades.
- **Nginx Validation:** Prueba sintáctica automatizada del Proxy Inverso, simulando el entorno de red para asegurar que la configuración TLS es correcta.
- **Unit Testing:** Ejecución de pruebas unitarias sobre la lógica del Backend.
- **Docker Stack Validation:** Verificación de que todas las imágenes construyen correctamente.

---

## 🌐 4. Puntos de Acceso (Infraestructura)

| Servicio | URL Pública | Protocolo |
|---|---|---|
| Frontend / App | https://localhost | HTTPS (Cifrado) |
| API Backend | https://localhost/tasks | Proxy Pass Interno |
| Redirección | http://localhost | Redirige automáticamente a 443 |

---

## 🛡️ 5. Informe de Seguridad (OWASP & SAST)

### 🔒 Cumplimiento OWASP Top Ten

- **A01:2021 - Access Control:** Validación de roles en servidor y ocultación de endpoints administrativos.
- **A02:2021 - Cryptographic Failures:** Cifrado de datos en tránsito y almacenamiento de credenciales no reversibles.
- **A05:2021 - Security Misconfiguration:** Deshabilitación de puertos de debug y exposición mínima de superficie de ataque.

### 🤖 Análisis Estático (Bandit)

| ID | Riesgo | Mitigación |
|---|---|---|
| B104 | Bind `0.0.0.0` | Necesario para Docker; mitigado por el Proxy de Nginx. |
| B105 | Hardcoded PWD | Resuelto: Uso estricto de variables de entorno `.env`. |

---

## 🏗️ 6. Estructura del Proyecto

```plaintext
├── .github/workflows/  # Pipeline CI/CD (GitHub Actions)
├── backend/            # API REST (Flask) y Lógica CRUD
├── frontend/           # Interfaz de Usuario y JS (Fetch API)
├── nginx/              # Configuración de Proxy e Infraestructura SSL
│   ├── default.conf    # Reglas de ruteo y hardening TLS
│   └── certs/          # Certificados SSL (Excluidos de Git)
├── docs/               # Colección de Postman y Documentación
├── docker-compose.yml  # Orquestación de la pila completa
└── .env                # Plantilla de configuración segura
```