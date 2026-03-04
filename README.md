# 📋 Kanban Board - SecDevOps Project

Este es un proyecto de tablero Kanban desarrollado bajo una metodología **SecDevOps**, integrando análisis de seguridad automatizado, pruebas de integración y un despliegue basado en contenedores. 🚀

---

## 🚀 Cómo ejecutar el proyecto

Este proyecto utiliza **Docker Compose** para orquestar los microservicios de Frontend y Backend de forma aislada y segura.

### 🛠️ Prerrequisitos

- **Docker Desktop** (incluye Docker Compose)
- **Git** para la gestión de versiones

### 🏁 Pasos para el despliegue

1. **Clona el repositorio:**

   ```bash
   git clone <url-de-tu-repositorio>
   cd kanban-secdevops
   ```

2. **Levanta el entorno:**

   ```bash
   docker compose down -v
   docker compose up --build -d
   ```

3. **Verificación:**

   ```bash
   docker compose ps
   ```

---

## 🔑 Configuración de Acceso y Usuarios

Para las pruebas de desarrollo y validación de seguridad, utiliza las siguientes credenciales:

### 👤 Usuarios de la Aplicación (Frontend/Login)

| Rol              | Usuario     | Contraseña |
|------------------|-------------|------------|
| Administrador    | `admin`     | `admin123` |
| Usuario Estándar | `user_test` | `user123`  |

### 🗄️ Acceso a Base de Datos (MySQL)

| Parámetro     | Valor                  |
|---------------|------------------------|
| Host Local    | `localhost:3307`       |
| Base de Datos | `kanban_db`            |
| Usuario DB    | `kanban_user`          |
| Password DB   | `kanban_password_123`  |
| Root Password | `root_password_segura` |

---

## 🌐 Puntos de Acceso

| Servicio    | URL                   |
|-------------|-----------------------|
| Frontend    | http://localhost:8080 |
| Backend API | http://localhost:5000 |

---

## 🛡️ Seguridad y Calidad (CI/CD)

- **Análisis SAST:** Integración de `Bandit` para detectar vulnerabilidades en Python.
- **Resiliencia:** El Backend espera a la DB mediante `service_healthy`.
- **Tests Unitarios:** Suite automatizada que valida rutas críticas en cada push.

---

## 🏗️ Estructura del Proyecto

```plaintext
├── .github/workflows/   # CI/CD Actions
├── backend/             # API REST (Flask)
├── frontend/            # UI (Flask)
├── tests/               # Unit tests
├── docker-compose.yml   # Orquestación
├── SECURITY.md          # Registro de mitigación
└── TESTING.md           # Estrategia de pruebas
```