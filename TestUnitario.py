import unittest
def suma(a, b):
    return a + b

class TestSuma(unittest.TestCase):
    def test_suma_positiva(self):
        result = suma(1, 2)
        self.assertEqual(result, 3)

    def test_suma_negativa(self):
        result = suma(-1, -2)
        self.assertEqual(result, -3)

    def test_suma_cero(self):
        result = suma(0, 0)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()


