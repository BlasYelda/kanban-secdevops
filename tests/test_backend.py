import unittest
import sys
import os

# Apuntamos a la carpeta 'app' dentro de 'backend'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../backend/app')))

# Importamos el archivo main.py como módulo
import main

class BackendTestCase(unittest.TestCase):
    def setUp(self):
        # Accedemos a la instancia Flask 'app' dentro de 'main.py'
        self.client = main.app.test_client()

    def test_api_root(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "API Backend Funcionando"})

if __name__ == '__main__':
    unittest.main()