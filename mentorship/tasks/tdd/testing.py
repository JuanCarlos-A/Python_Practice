import unittest
from main import add, dividir

class Testing(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_dividir(self):
        self.assertEqual(dividir(1, 2), 0.5)
        self.assertEqual(dividir(0, 1), 0)
        self.assertEqual(dividir(-1, 1), -1)
        self.assertEqual(dividir(-1, -1), 1)


if __name__ == "__main__":
    unittest.main()

