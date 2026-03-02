import unittest
import sys
import os

# --- CORRECCIÓN AQUÍ ---
# Añadimos la carpeta 'frontend' al path para que Python encuentre app.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../frontend')))

# Ahora esta importación funcionará
from app import app

class FrontendTestCase(unittest.TestCase):
    def setUp(self):
        self.ctx = app.app_context()
        self.ctx.push()
        self.client = app.test_client()

    def tearDown(self):
        self.ctx.pop()

    def test_login_page_loads(self):
        """Verifica que la página de login carga correctamente"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()