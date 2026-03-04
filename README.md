# 📋 Kanban Board - SecDevOps Project

Este es un tablero Kanban robusto desarrollado bajo la metodología SecDevOps. Integra microservicios aislados, análisis de seguridad automatizado y una infraestructura resiliente mediante contenedores.

---

## 🚀 Despliegue del Proyecto

Hemos optimizado el orquestador para garantizar que los servicios arranquen en el orden correcto, evitando errores de conexión de base de datos mediante Healthchecks y Networks aisladas.

### Prerrequisitos

- **Docker Desktop** (incluye Docker Compose)
- **Git** para la gestión de versiones

### Pasos para el arranque

1. **Clonar el repositorio:**

   ```bash
   git clone <url-de-tu-repositorio>
   cd kanban-secdevops
   ```

2. **Levantar el entorno (Modo Limpio):**

   Para asegurar un despliegue sin conflictos de caché o volúmenes antiguos, ejecuta:

   ```bash
   docker compose down -v
   docker compose up --build -d
   ```

3. **Verificar estado de salud:**

   ```bash
   docker compose ps
   ```

   > El contenedor `kanban-db` debe marcarse como **healthy** antes de que el backend inicie sus operaciones.

---

## 🌐 Puntos de Acceso

| Servicio     | URL Local              | Descripción                     |
|--------------|------------------------|---------------------------------|
| Frontend     | http://localhost:8080  | Interfaz de usuario Flask       |
| Backend API  | http://localhost:5000  | Lógica de negocio y API REST    |
| Database     | `localhost:3307`       | Acceso externo (mapeado al 3306 interno) |

---

## ⚙️ Configuración y Credenciales

El sistema utiliza las siguientes variables de entorno preconfiguradas para el desarrollo:

| Variable        | Valor                  |
|-----------------|------------------------|
| Base de Datos   | `kanban_db`            |
| Usuario DB      | `kanban_user`          |
| Password DB     | `kanban_password_123`  |
| Red Interna     | `kanban-network`       |

> **Red Interna:** Aísla el tráfico entre servicios.

> [!IMPORTANT]
> El Backend incluye una política de resiliencia: si la base de datos no está lista, el servicio esperará automáticamente gracias a la condición `service_healthy` definida en el `docker-compose.yml`.

---

## 🛡️ Seguridad y Calidad (CI/CD)

El proyecto implementa un pipeline de Integración Continua que garantiza la seguridad en cada cambio:

- **Análisis SAST:** Uso de `Bandit` para detectar vulnerabilidades en el código Python de forma temprana.
- **Healthchecks:** Monitorización activa de la disponibilidad de MySQL (`mysqladmin ping`).
- **Aislamiento de Red:** Los microservicios se comunican a través de una red puente privada, limitando la exposición de puertos innecesarios.
- **Pruebas Automatizadas:** Suite con `unittest` que valida las rutas críticas antes de cada despliegue.

---

## 🏗️ Estructura del Proyecto

```plaintext
├── .github/workflows/   # Automatización CI/CD (GitHub Actions)
├── backend/             # API REST (Flask + SQLAlchemy)
├── frontend/            # Interfaz de Usuario (Flask)
├── tests/               # Pruebas unitarias y de integración
├── docker-compose.yml   # Orquestación de microservicios
├── SECURITY.md          # Registro de mitigación de riesgos
└── TESTING.md           # Estrategia y resultados de pruebas
```