📋 Kanban Board - SecDevOps Project
Este es un proyecto de tablero Kanban desarrollado bajo una metodología SecDevOps, integrando análisis de seguridad automatizado, pruebas de integración y un despliegue basado en contenedores.

🚀 Cómo ejecutar el proyecto
Este proyecto utiliza Docker Compose para orquestar los microservicios de Frontend y Backend de forma aislada y segura.

🛠️ Prerrequisitos
Tener instalado Docker Desktop.

Git para la gestión de versiones.

🏁 Pasos para el despliegue
Clona el repositorio:

Bash
git clone <url-de-tu-repositorio>
cd kanban-secdevops
Levanta el entorno: Ejecuta el siguiente comando en la raíz para construir y levantar los contenedores:

Bash
docker compose up --build
Acceso a la aplicación:

Interfaz de Usuario (Frontend): http://localhost:8080

API de Datos (Backend): http://localhost:5000

🛡️ Seguridad y Calidad (CI/CD)
El proyecto cuenta con un pipeline automatizado en GitHub Actions (ci-cd.yml) que garantiza la integridad del código en cada commit y pull request:

Análisis SAST: Integración de Bandit para la detección temprana de vulnerabilidades en el código Python.

Tests Unitarios: Suite de pruebas automatizadas con unittest que validan la disponibilidad de las rutas raíz tanto en Frontend como en Backend.

Gestión de Riesgos: Se han documentado y mitigado hallazgos de seguridad, consultables en el archivo SECURITY.md.

Validación de Calidad: Detalles sobre la estrategia de pruebas y resultados en el archivo TESTING.md.

🏗️ Estructura del Proyecto
frontend/: Aplicación Flask que sirve la interfaz de usuario.

backend/: API REST en Flask para la gestión de lógica y datos.

tests/: Pruebas unitarias para asegurar la estabilidad del sistema.

.github/workflows/: Configuración de la Integración Continua (CI).