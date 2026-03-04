# 📋 Kanban Board - SecDevOps Project

Este es un proyecto de tablero Kanban desarrollado bajo una metodología **SecDevOps**, integrando análisis de seguridad automatizado (SAST), pruebas de integración y un despliegue resiliente basado en contenedores Docker con persistencia en MySQL. 🚀

---

## 🚀 1. Cómo ejecutar el proyecto

Este proyecto utiliza **Docker Compose** para orquestar los microservicios de Frontend, Backend y Base de Datos de forma aislada. Hemos implementado **Healthchecks** para asegurar que la API no inicie hasta que la base de datos esté lista.

### 🛠️ Prerrequisitos

- **Docker Desktop** (incluye Docker Compose)
- **Git** para la gestión de versiones

### 🏁 Pasos para el despliegue

1. **Clona el repositorio:**

   ```bash
   git clone <url-de-tu-repositorio>
   cd kanban-secdevops
   ```

2. **Levanta el entorno (Modo Limpio):**

   Este comando limpia volúmenes antiguos y construye las imágenes desde cero.

   ```bash
   docker compose down -v
   docker compose up --build -d
   ```

3. **Verificación de estado:**

   ```bash
   docker compose ps
   ```

   > El contenedor `kanban-db` debe aparecer como **(healthy)**.

---

## 🔑 2. Configuración de Acceso y Usuarios

### 👤 Usuarios de la Aplicación (Frontend)

| Rol              | Usuario     | Contraseña |
|------------------|-------------|------------|
| Administrador    | `admin`     | `admin123` |
| Usuario Estándar | `user_test` | `user123`  |

### 🗄️ Acceso a Base de Datos (MySQL)

| Parámetro     | Valor                 |
|---------------|-----------------------|
| Host Local    | `localhost:3307`      |
| Base de Datos | `kanban_db`           |
| Usuario DB    | `kanban_user`         |
| Password DB   | `kanban_password_123` |

---

## 🌐 3. Puntos de Acceso (Endpoints)

| Servicio    | URL                   | Descripción                    |
|-------------|-----------------------|--------------------------------|
| Frontend    | http://localhost:8080 | Interfaz de usuario (Flask)    |
| Backend API | http://localhost:5000 | API REST de datos (Flask)      |

---

## 🛡️ 4. Informe de Seguridad (OWASP & SAST)

Se han implementado controles basados en el estándar **OWASP Top Ten** y un ciclo de seguridad automatizada.

### 🔒 Controles Implementados

- **A01:2021 - Broken Access Control:** Lógica de autorización que diferencia interfaces según el rol (`admin`/`user`) en la sesión.
- **A02:2021 - Cryptographic Failures:** Uso de `app.secret_key` para cifrar y firmar cookies de sesión.
- **A07:2021 - Identification and Authentication Failures:** Estructura preparada para integración de hashes de contraseñas seguros.

### 🤖 Análisis Estático (Bandit)

Integrado en el pipeline de CI/CD para detectar riesgos en Python:

| ID    | Descripción               | Mitigación                                                                 |
|-------|---------------------------|----------------------------------------------------------------------------|
| B104  | Bind `0.0.0.0`            | Mitigado con `# nosec` tras validar necesidad en Docker.                   |
| B105  | Hardcoded password        | Riesgo aceptado para desarrollo; documentado para migración a `.env`.      |

---

## 🧪 5. Informe de Pruebas y Calidad

### ✅ Prerrequisitos de Integración

- **Orquestación:** Validada mediante Docker Network. Los servicios se comunican internamente sin exponer puertos sensibles innecesariamente.
- **Resiliencia:** El Backend utiliza `depends_on: condition: service_healthy` para evitar errores de conexión inicial.

### 🧪 Pruebas Unitarias (`unittest`)

Las pruebas se ejecutan automáticamente en **GitHub Actions** en cada push:

| Test           | Descripción                                           |
|----------------|-------------------------------------------------------|
| Frontend Test  | Valida disponibilidad de ruta `/` (Status 200).       |
| Backend Test   | Valida respuesta JSON y mensaje de salud de la API.   |

---

## 🏗️ 6. Estructura del Proyecto

```plaintext
├── .github/workflows/   # CI/CD (GitHub Actions)
├── backend/             # API REST y Lógica de BBDD
├── frontend/            # Interfaz de Usuario
├── tests/               # Suite de Pruebas Unitarias
├── docker-compose.yml   # Orquestación de Contenedores
├── SECURITY.md          # (Opcional) Registro detallado de mitigación
└── TESTING.md           # (Opcional) Estrategia extendida de QA
```