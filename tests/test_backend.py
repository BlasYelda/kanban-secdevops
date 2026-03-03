import unittest
import sys
import os

# Ajustar el path para importar main.py desde backend/app
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../backend')))

from app.main import app

class BackendTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_api_root(self):
        """Verifica que la API raíz responde correctamente"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "API Backend Funcionando"})

if __name__ == '__main__':
    unittest.main()