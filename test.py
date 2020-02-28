import polynomial
import unittest

class PolynomialTestRepresentation(unittest.TestCase):

    def test_unsupportedTypes(self):
        with self.assertRaises(Exception):
            polynomial.Polynomial("string")

    def test_supportedType(self):
        polynomial.Polynomial([1,2,3])
        polynomial.Polynomial((1, 2, 3))
        polynomial.Polynomial({1,2,3})

    def test_negativeCoeffs(self):
        self.assertEqual(str(polynomial.Polynomial([1,-2, 3])), "x^2 + 2x + 3")

    def test_negativeCoeffs(self):
        self.assertEqual(str(polynomial.Polynomial([-1, -2, -3])), "-x^2 - 2x - 3")

    def test_badZeros(self):
        self.assertEqual(str(polynomial.Polynomial([0,0,0,1,2,3])), str(polynomial.Polynomial([1,2,3])))

    def test_zeroCoeffs(self):
        self.assertEqual(str(polynomial.Polynomial([1, 0, 0, 4])), "x^3 + 4")

unittest.main()
