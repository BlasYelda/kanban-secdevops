import unittest
import sys
import os

# Apuntamos a la carpeta raíz de la aplicación del backend
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../backend/app')))

# Importamos directamente el módulo main
import main

class BackendTestCase(unittest.TestCase):
    def setUp(self):
        # Accedemos al objeto Flask 'app' dentro del módulo 'main'
        self.client = main.app.test_client()

    def test_api_root(self):
        """Verifica que la API raíz responde correctamente"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "API Backend Funcionando"})

if __name__ == '__main__':
    unittest.main()