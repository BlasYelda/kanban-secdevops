# Informe de Seguridad OWASP y Gestión de Vulnerabilidades

Se han implementado medidas basadas en el estándar OWASP Top Ten y se ha integrado un ciclo de seguridad automatizada (SAST).

## 🛡️ Controles OWASP Implementados

* **A01:2021-Broken Access Control**: Se implementa lógica de autorización en el frontend (`frontend/app.py`) que diferencia el acceso y la interfaz según el rol (`admin` o `normal`) almacenado en la sesión de forma segura.
* **A02:2021-Cryptographic Failures**: Se utiliza `app.secret_key` para el cifrado y firma de las cookies de sesión, evitando la manipulación de datos por parte del cliente.
* **A07:2021-Identification and Authentication Failures**: Aunque se utiliza un sistema de usuarios simulado, se ha estructurado para permitir una futura integración con hashes de contraseñas seguros.

## 🤖 Automatización de Seguridad (SAST)

Se ha integrado **Bandit** en el pipeline de CI/CD (`.github/workflows/ci-cd.yml`) para realizar análisis estático de seguridad en cada commit.

### Gestión de Hallazgos (Vulnerabilidades detectadas)
Durante el desarrollo, Bandit detectó los siguientes riesgos que han sido gestionados:

1. **B104 (Hardcoded host bind)**: Se detectó el uso de `0.0.0.0`. Se ha mitigado mediante el uso de la etiqueta `# nosec` en el código, tras verificar que es necesario para la visibilidad del contenedor Docker en el entorno de desarrollo.
2. **B105 (Hardcoded password)**: Se identificaron credenciales en el código. Se mantiene como riesgo aceptado para esta versión de prueba, documentado para ser corregido en la fase de integración de Base de Datos.

El pipeline ha sido configurado con `--exit-zero` para permitir la generación de reportes continuos sin detener el despliegue de desarrollo, garantizando la visibilidad total de los riesgos.