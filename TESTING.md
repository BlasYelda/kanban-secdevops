# Documentación de Pruebas

* [cite_start]**Pruebas de Integración (Docker Compose)**: Se ha verificado que los contenedores `kanban-backend` y `kanban-frontend` se construyen y levantan correctamente utilizando el comando `docker compose up --build`[cite: 19].
* **Pruebas Unitarias - Frontend**: Se ha creado `tests/test_frontend.py` para verificar que la página de login (`/`) responde con un código 200 OK.
* **Pruebas Unitarias - Backend**: Se ha creado `tests/test_backend.py` para verificar que la API raíz (`/`) responde con un código 200 OK y devuelve el mensaje JSON correcto.