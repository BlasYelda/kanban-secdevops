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

> Si no tienes `openssl` instalado, usa el comando de Docker compartido en la documentación técnica.

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
- **Hashing de Contraseñas:** Almacenamiento seguro en MySQL usando `PBKDF2` con salt.
- **RBAC (Role-Based Access Control):** Decoradores `@admin_required` que protegen endpoints sensibles (borrado de tareas, listado de usuarios).
- **Hardening de Red:** Solo los puertos 80/443 están expuestos; el Backend y la DB son invisibles desde el exterior.

---

## 🌐 3. Puntos de Acceso (Infraestructura)

| Servicio | URL Pública | Protocolo |
|---|---|---|
| Frontend / App | https://localhost | HTTPS (Cifrado) |
| API Backend | https://localhost/tasks | Proxy Pass Interno |
| Redirección | http://localhost | Redirige a 443 |

---

## 🛡️ 4. Informe de Seguridad (OWASP & SAST)

### 🔒 Cumplimiento OWASP Top Ten

- **A01:2021 - Access Control:** Validación de headers `X-Role` en el servidor.
- **A02:2021 - Cryptographic Failures:** Cifrado en tránsito (SSL) y en reposo (Hashes).
- **A05:2021 - Security Misconfiguration:** Deshabilitación de puertos de desarrollo (5000/8080) en producción.

### 🤖 Análisis Estático (Bandit)

| ID | Riesgo | Mitigación |
|---|---|---|
| B104 | Bind `0.0.0.0` | Validado para orquestación de Docker. |
| B105 | Hardcoded PWD | Resuelto: Migrado a `.env` y carga dinámica de secretos. |

---

## 🏗️ 5. Estructura del Proyecto

```plaintext
├── backend/            # API REST (Flask) y Lógica CRUD
├── frontend/           # Interfaz de Usuario y JS (Rutas relativas seguras)
├── nginx/              # Configuración de Proxy y Certificados SSL
│   ├── default.conf    # Reglas de ruteo y hardening TLS
│   └── certs/          # Certificados .crt y .key (Ignorados en Git)
├── docs/               # Colección de Postman para pruebas de API
├── docker-compose.yml  # Orquestación de toda la pila SecDevOps
└── .env.example        # Plantilla de configuración segura
```