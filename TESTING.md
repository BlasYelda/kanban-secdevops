# Informe de Pruebas y Calidad de Software

Este documento detalla la estrategia de validación para asegurar que el sistema Kanban cumple con los requisitos funcionales y de seguridad.

## 🏗️ 1. Pruebas de Integración (Entorno Docker)
Se ha validado la orquestación de servicios mediante **Docker Compose**, garantizando que el ecosistema de microservicios (Frontend y Backend) es reproducible y estable.
* **Evidencia**: Los contenedores `kanban-backend` y `kanban-frontend` se comunican correctamente en la red interna de Docker.
* **Comando de verificación**: `docker compose up --build`.

## 🧪 2. Pruebas Unitarias (Framework Unittest)
Se han implementado tests automatizados para validar los puntos de entrada críticos de la aplicación.

### A. Frontend (`tests/test_frontend.py`)
* **Objetivo**: Verificar la disponibilidad de la interfaz de usuario.
* **Resultado**: El test confirma que la ruta raíz (`/`) es accesible y devuelve un código de estado `200 OK`, asegurando que el servidor Flask está listo para recibir usuarios.

### B. Backend (`tests/test_backend.py`)
* **Objetivo**: Validar la integridad de la API.
* **Resultado**: Se verifica que la API responde en formato JSON y que el mensaje de salud del sistema es correcto, confirmando la conectividad del backend.

## 🔄 3. Ejecución en el Pipeline (CI/CD)
Las pruebas unitarias se han integrado en el workflow de **GitHub Actions** (`ci-cd.yml`). Esto garantiza que cualquier cambio en el código sea testeado automáticamente antes de ser integrado en la rama `main`.

## 📊 4. Cobertura y Resultados
Actualmente, el 100% de las pruebas unitarias definidas pasan correctamente en el entorno de integración continua, lo que permite un despliegue seguro.