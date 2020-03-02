import polynomial
import unittest

class PolynomialTests(unittest.TestCase):

    def test_unsupportedTypes(self):
        with self.assertRaises(Exception):
            polynomial.Polynomial("string")

    def test_supportedType(self):
        polynomial.Polynomial([1,2,3])
        polynomial.Polynomial((1, 2, 3))
        polynomial.Polynomial({1,2,3})

    # [repr and str]
    def test_negativeCoeffs(self):
        self.assertEqual(str(polynomial.Polynomial([1,-2, 3])), "x^2 + 2x + 3")

    def test_negativeCoeffs(self):
        self.assertEqual(str(polynomial.Polynomial([-1, -2, -3])), "-x^2 - 2x - 3")

    def test_repr(self):
        self.assertEqual(repr(polynomial.Polynomial([1,2,-4])), "Polynomial([1, 2, -4])")

    def test_boundMin(self):
        self.assertEqual(str(polynomial.Polynomial(1)), "1")

    def test_boundMinNegative(self):
        self.assertEqual(str(polynomial.Polynomial(-1)), "-1")

    def test_boundZeroOnTheEnd(self):
        self.assertEqual(str(polynomial.Polynomial([1,0,0,0,0,0])), "x^5")

    def test_boundZeroInTheStart(self):
        self.assertEqual(str(polynomial.Polynomial([0, 0, 0, 0, 0, 1])), "1")

    def test_zeroCoeffsMixed(self):
        self.assertEqual(str(polynomial.Polynomial([1, 0, 0, 4])), "x^3 + 4")

    def test_boundMinZero(self):
        self.assertEqual(str(polynomial.Polynomial(0)), "")

    def test_badZeros(self):
        self.assertEqual(str(polynomial.Polynomial([0, 0, 0, 1, 2, 3])), str(polynomial.Polynomial([1, 2, 3])))

    # [eq, adds, mult etc]
    def test_eq(self):
        self.assertTrue(polynomial.Polynomial([1,1,1]) == polynomial.Polynomial([1,1,1]))

    def test_neq(self):
        self.assertFalse(polynomial.Polynomial([1,1,1]) == polynomial.Polynomial([0,1,1]))

    def test_addPolynomial(self):
        self.assertEqual(polynomial.Polynomial([1,1,1]) + polynomial.Polynomial([1,1,1]), polynomial.Polynomial([2,2,2]))

unittest.main()

# p = polynomial.Polynomial([1,1,1,1,1,1,1])
# for k,v in enumerate(p.coeffs):
#     print(k)