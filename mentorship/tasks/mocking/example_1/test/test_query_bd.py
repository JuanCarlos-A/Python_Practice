import unittest
from unittest.mock import Mock
from example_1.main import obtener_nombres_usuarios

class QueryBD(unittest.TestCase):

    def test_query_nombres(self):

        db_mock = Mock()

        db_mock.query.return_value = [
            {'id': 1, 'nombre': 'Alice'},
            {'id': 2, 'nombre': 'Bob'}
        ]

        nombres = obtener_nombres_usuarios(db_mock)
        self.assertEqual(nombres, ['Alice', 'Bob'])


if __name__ == '__main__':
    unittest.main()