import unittest
import sys
import os

# Apuntamos directamente a la carpeta del frontend
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../frontend')))

# Importamos el archivo app.py como un módulo
import app 

class FrontendTestCase(unittest.TestCase):
    def setUp(self):
        # Accedemos a la instancia Flask 'app' dentro del archivo 'app.py'
        self.ctx = app.app.app_context()
        self.ctx.push()
        self.client = app.app.test_client()

    def tearDown(self):
        self.ctx.pop()

    def test_login_page_loads(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()