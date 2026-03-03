import unittest
import sys
import os

# Apuntamos directamente a la carpeta del frontend
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../frontend')))

# Importamos el módulo completo para evitar ambigüedad con el nombre de la carpeta
import app 

class FrontendTestCase(unittest.TestCase):
    def setUp(self):
        # Accedemos al objeto Flask (app) dentro del archivo importado (app)
        self.ctx = app.app.app_context()
        self.ctx.push()
        self.client = app.app.test_client()

    def tearDown(self):
        self.ctx.pop()

    def test_login_page_loads(self):
        """Verifica que la página de login carga correctamente"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()