# 📋 Kanban Board - SecDevOps Project

Este es un proyecto de tablero Kanban desarrollado bajo una metodología SecDevOps, integrando análisis de seguridad automatizado (SAST), pruebas de integración y un despliegue resiliente basado en contenedores Docker con persistencia real en MySQL. 🚀

---

## 🚀 1. Cómo ejecutar el proyecto

Este proyecto utiliza Docker Compose para orquestar los microservicios de Frontend, Backend y Base de Datos. Se han implementado Healthchecks y una red aislada para asegurar la integridad del sistema.

### 🛠️ Prerrequisitos

- Docker Desktop
- Git

### 🏁 Pasos para el despliegue

**1. Clona el repositorio:**

```bash
git clone <url-de-tu-repositorio>
cd kanban-secdevops
```

**2. Levanta el entorno (Modo Limpio):**

Este comando limpia volúmenes antiguos para regenerar las tablas de MySQL y construye las imágenes.

```bash
docker compose down -v
docker compose up --build -d
```

**3. Verificación de estado:**

```bash
docker compose ps
```

---

## 🔑 2. Gestión de Usuarios y Seguridad

### 👤 Credenciales de Aplicación

| Rol | Usuario | Contraseña |
|---|---|---|
| Administrador | `admin` | `admin123` |
| Usuario Estándar | `pepe` | `pepe123` |

### 🛡️ Seguridad Implementada

- **Gestión de Secretos:** Uso de archivos `.env` (ignorados en Git) para manejar claves privadas y credenciales de DB.
- **Hashing de Contraseñas:** Las contraseñas se almacenan en MySQL usando `werkzeug.security` (PBKDF2 con salt).
- **RBAC (Role-Based Access Control):** Decoradores personalizados en el Backend que validan el rol del usuario antes de permitir acciones críticas (ej. borrar tareas o ver lista de usuarios).

---

## 🌐 3. Puntos de Acceso y API

| Servicio | URL | Descripción |
|---|---|---|
| Frontend | http://localhost:8080 | Dashboard Kanban dinámico. |
| Backend API | http://localhost:5000 | API REST con soporte CORS. |

### 🧪 Pruebas de API (Postman)

Se ha incluido una colección de pruebas en la carpeta `/docs`. Para ejecutarlas:

1. Importa `docs/Kanban_Tests.postman_collection.json` en Postman.
2. Ejecuta las peticiones para validar los códigos de estado `200 OK`, `201 Created` y el bloqueo de seguridad `403 Forbidden`.

---

## 🛡️ 4. Informe de Seguridad (OWASP & SAST)

### 🔒 Cumplimiento OWASP Top Ten

- **A01:2021 - Broken Access Control:** Implementación de decoradores `@admin_required` que verifican cabeceras de rol.
- **A02:2021 - Cryptographic Failures:** Eliminación de secretos del código fuente; uso de hashing seguro para BD.
- **A03:2021 - Injection:** Uso de SQLAlchemy ORM para prevenir ataques de SQL Injection mediante consultas parametrizadas.

### 🤖 Análisis Estático (Bandit)

| ID | Riesgo Detectado | Mitigación | Estado |
|---|---|---|---|
| B104 | Bind `0.0.0.0` | Necesario para comunicación entre contenedores Docker. | Controlado |
| B105 | Hardcoded Passwords | Solucionado: Migrado totalmente a variables de entorno (`.env`). | Resuelto |

---

## 🏗️ 5. Estructura del Proyecto

```plaintext
├── backend/            # API REST (Flask), Modelos SQLAlchemy y Lógica CRUD
├── frontend/           # Interfaz de Usuario, Templates y JS (Fetch API)
├── docs/               # Colección de Postman y documentación técnica
├── docker-compose.yml  # Orquestación (Frontend, Backend, MySQL)
├── .env.example        # Plantilla para variables de entorno
└── .gitignore          # Exclusión de secretos y entornos virtuales
```