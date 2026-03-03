import unittest
import sys
import os

# Apuntamos a la carpeta 'app' dentro de 'backend'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../backend/app')))

import main

class BackendTestCase(unittest.TestCase):
    def setUp(self):
        self.client = main.app.test_client()

    def test_api_root(self):
        """Verifica que la API raíz responde correctamente"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "API Backend Funcionando"})

if __name__ == '__main__':
    unittest.main()