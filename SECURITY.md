# Informe de Seguridad OWASP

Se han considerado los siguientes aspectos del OWASP Top Ten:

* **A01:2021-Broken Access Control**: Se implementa lógica de autorización en el frontend (`frontend/app.py`) que diferencia el color de fondo y el título según el rol (`admin` o `normal`) almacenado en la sesión.
* **A02:2021-Cryptographic Failures**: Uso de `app.secret_key` en Flask para firmar cookies de sesión de forma segura.
* [cite_start]**Automatización de Seguridad**: Se ha integrado `bandit` en el pipeline de GitHub Actions (`.github/workflows/ci-cd.yml`) para realizar análisis estático de seguridad (SAST) en busca de fallos comunes en el código Python en cada push[cite: 21].