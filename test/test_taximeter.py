import unittest
from taximeter import calculating_fare  # importamos de la clase principal el metodo calculating_fare

class TestCalculatingFare(unittest.TestCase):

    def test_fare_only_stopped(self):
        # Test teniendo en cuenta solo tiempo detenido, sin movimiento
        result = calculating_fare(10, 0)
        self.assertAlmostEqual(result, 0.2)  # 10 * 0.02 = 0.2 € deberia resultar

    def test_fare_only_moving(self):
        # Solo tiempo en movimiento, sin estar detenido
        result = calculating_fare(0, 10)
        self.assertAlmostEqual(result, 0.5)  # 10 * 0.05 = 0.5 €

    def test_fare_stopped_and_moving(self):
        # Tiempo mezclado detenido y en movimiento
        result = calculating_fare(5, 5)
        self.assertAlmostEqual(result, 0.35)  # (5*0.02) + (5*0.05) = 0.1 + 0.25 = 0.35 €

    def test_fare_zero(self):
        # Sin tiempo ni detenido ni en movimiento
        result = calculating_fare(0, 0)
        self.assertEqual(result, 0)

if __name__ == "__main__":
    unittest.main()