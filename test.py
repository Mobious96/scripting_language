import polynomial
import unittest

class PolynomialTests(unittest.TestCase):

    def test_unsupportedTypes(self):
        with self.assertRaises(Exception):
            polynomial.Polynomial("string")

    def test_supportedType(self):
        polynomial.Polynomial([1,2,3])
        polynomial.Polynomial((1, 2, 3))
        #polynomial.Polynomial({1,2,3})

    def test_copy(self):
        p = polynomial.Polynomial([1,2,3])
        p2 = polynomial.Polynomial(p)
        self.assertEqual(p,p2)

    def test_copyNotLinked(self):
        p = polynomial.Polynomial([1,2,3])
        p2 = polynomial.Polynomial(p)
        p2.coeffs[0] -= 2
        self.assertNotEqual(p,p2)

    # [repr and str]
    def test_negativeCoeffs(self):
        self.assertEqual(str(polynomial.Polynomial([1,-2, 3])), "x^2 + 2x + 3")

    def test_negativeCoeffs(self):
        self.assertEqual(str(polynomial.Polynomial([-1, -2, -3])), "-x^2 - 2x - 3")

    def test_repr(self):
        self.assertEqual(repr(polynomial.Polynomial([1,2,-4])), "Polynomial([1, 2, -4])")

    def test_boundMinZero(self):
        self.assertEqual(str(polynomial.Polynomial(0)), "0")

    def test_boundMinNegativeZero(self):
        self.assertEqual(str(polynomial.Polynomial(-0)), "0")

    def test_boundMin(self):
        self.assertEqual(str(polynomial.Polynomial(1)), "1")

    def test_boundMin2(self):
        self.assertEqual(str(polynomial.Polynomial(6)), "6")

    def test_boundMinNegative(self):
        self.assertEqual(str(polynomial.Polynomial(-1)), "-1")

    def test_boundZeroOnTheEnd(self):
        self.assertEqual(str(polynomial.Polynomial([1,0,0,0,0,0])), "x^5")

    def test_boundZeroInTheStart(self):
        self.assertEqual(str(polynomial.Polynomial([0, 0, 0, 0, 0, 1])), "1")

    def test_zeroCoeffsMixed(self):
        self.assertEqual(str(polynomial.Polynomial([1, 0, 0, 4])), "x^3 + 4")

    def test_badZeros(self):
        self.assertEqual(str(polynomial.Polynomial([0, 0, 0, 1, 2, 3])), str(polynomial.Polynomial([1, 2, 3])))

    # [eq, adds, mult etc]
    def test_eq(self):
        self.assertTrue(polynomial.Polynomial([1,1,1]) == polynomial.Polynomial([1,1,1]))

    def test_neq(self):
        self.assertFalse(polynomial.Polynomial([1,1,1]) == polynomial.Polynomial([0,1,1]))

    def test_neqString(self):
        with self.assertRaises(Exception):
            polynomial.Polynomial(0) == "0"

    def test_eqCoeff(self):
        self.assertEqual(polynomial.Polynomial([1]), 1)

    def test_eqCoeffSide(self):
        self.assertEqual(1, polynomial.Polynomial([1]))

    def test_initZeros(self):
        self.assertEqual(polynomial.Polynomial([0,0,0]), polynomial.Polynomial(0))

    def test_addPolynomial(self):
        self.assertEqual(polynomial.Polynomial([1,2,3]) + polynomial.Polynomial([1,1,1]), polynomial.Polynomial([2,3,4]))

    def test_addPolynomialNegative(self):
        self.assertEqual(polynomial.Polynomial([1,2,3,4]) + polynomial.Polynomial([1,0,-1,1]), polynomial.Polynomial([2,2,2,5]))

    def test_addPolynomialDifferentLength(self):
        self.assertEqual(polynomial.Polynomial([1, 2, 3, 4, 5]) + polynomial.Polynomial([1, 1, 2]), polynomial.Polynomial([1, 2, 4, 5, 7]))

    def test_addPolynomialDifferentLength2(self):
        self.assertEqual(polynomial.Polynomial([1, 2]) + polynomial.Polynomial([1, 2, 3]), polynomial.Polynomial([1, 3, 5]))

    def test_addPolynomialDifferentLength3(self):
        self.assertEqual(polynomial.Polynomial([1, 2, 3, 4]) + polynomial.Polynomial([-1, -2, 0, 0]), polynomial.Polynomial([3,4]))

    def test_addPolynomialDifferentLength4(self):
        self.assertEqual(polynomial.Polynomial([1, 2, 3, 4, 5]) + polynomial.Polynomial([1]), polynomial.Polynomial([1, 2, 3, 4, 6]))

    def test_addPolynomialSameLength3(self):
        self.assertEqual(polynomial.Polynomial([1, 2, 3]) + polynomial.Polynomial([-1, -2, 3]), polynomial.Polynomial([6]))

    def test_addPolynomialZero(self):
        self.assertEqual(polynomial.Polynomial([1,2,3]) + polynomial.Polynomial(0), polynomial.Polynomial([1,2,3]))

    def test_addCoeff(self):
        self.assertEqual(polynomial.Polynomial([1,1,1]) + 1, polynomial.Polynomial([1,1,2]))

    def test_addCoef2(self):
        self.assertEqual(polynomial.Polynomial([1]) + 1, polynomial.Polynomial(2))

    def test_addCoeff3(self):
        self.assertEqual(polynomial.Polynomial(0) + 0, 0)

    def test_raddCoeff(self):
        self.assertEqual(1 + polynomial.Polynomial([1,1,1]), polynomial.Polynomial([1,1,2]))

    def test_sub(self):
        self.assertEqual(polynomial.Polynomial([2,2,2]) - polynomial.Polynomial([1,1,1]), polynomial.Polynomial([1,1,1]))

    def test_subCoeff(self):
        self.assertEqual(polynomial.Polynomial([1, 1, 2]) - 1, polynomial.Polynomial([1, 1, 1]))

    def test_subCoef2(self):
        self.assertEqual(polynomial.Polynomial([2]) - 1, polynomial.Polynomial(1))

    def test_subCoeff3(self):
        self.assertEqual(polynomial.Polynomial(0) - 0, 0)

    def test_subPolynomialNegative(self):
        self.assertEqual(polynomial.Polynomial([1,2,3,4]) - polynomial.Polynomial([1,0,-1,1]), polynomial.Polynomial([0,2,4,3]))

    def test_subPolynomialDifferentLength(self):
        self.assertEqual(polynomial.Polynomial([1, 2, 3, 4, 5]) - polynomial.Polynomial([1, 1, 2]), polynomial.Polynomial([1, 2, 2, 3, 3]))

    def test_subPolynomialDifferentLength2(self):
        self.assertEqual(polynomial.Polynomial([1, 2]) - polynomial.Polynomial([1, 2, 3]), polynomial.Polynomial([-1, -1, -1]))

    def test_subPolynomialDifferentLength3(self):
        self.assertEqual(polynomial.Polynomial([1, 2, 3, 4]) - polynomial.Polynomial([1, 2, 0, 0]), polynomial.Polynomial([3,4]))

    def test_subPolynomialDifferentLength4(self):
        self.assertEqual(polynomial.Polynomial([1, 2, 3, 4]) - polynomial.Polynomial([1]), polynomial.Polynomial([1,2,3,3]))

    def test_subPolynomialSameLength3(self):
        self.assertEqual(polynomial.Polynomial([1, 2, 3]) - polynomial.Polynomial([1, 2, 3]), polynomial.Polynomial([0]))

    def test_subPolynomialZero(self):
        self.assertEqual(polynomial.Polynomial([1,2,3]) - polynomial.Polynomial(0), polynomial.Polynomial([1,2,3]))

    def test_rsubCoeff(self):
        self.assertEqual(1 - polynomial.Polynomial([1, 1, 1]), polynomial.Polynomial([-1, -1, 0]))

    def test_rsubCoeff2(self):
        self.assertEqual(1 - polynomial.Polynomial([1]), polynomial.Polynomial([0]))

    # (x+2)*(x^2 + x + 1) = x^3 + x^2 + x + 2x^2 + 2x + 2 = x^3 + 3x^2 + 3x + 2
    def test_mulPolynomial1(self):
        self.assertEqual(polynomial.Polynomial([1,2]) * polynomial.Polynomial([1,1,1]), polynomial.Polynomial([1,3,3,2]))

    def test_mulPolynomial2(self):
        self.assertEqual(polynomial.Polynomial([1,0,0]) * polynomial.Polynomial([1,1,1]), polynomial.Polynomial([1,1,1,0,0]))

    def test_mulPolynomial3(self):
        self.assertEqual(polynomial.Polynomial([-1,0]) * polynomial.Polynomial([1,1,1]), polynomial.Polynomial([-1,-1,-1,0]))

    def test_mulPolynomial3(self):
        self.assertEqual(polynomial.Polynomial([0]) * polynomial.Polynomial([1,1,1]), polynomial.Polynomial([0]))

    def test_mulCoeff1(self):
        self.assertEqual(polynomial.Polynomial([1,1,1]) * 2, polynomial.Polynomial([2,2,2]))

    def test_mulCoeff2(self):
        self.assertEqual(polynomial.Polynomial([1,1,1]) * (-2), polynomial.Polynomial([-2,-2,-2]))

    def test_mulCoeff3(self):
        self.assertEqual(polynomial.Polynomial([1,1,1]) * 0, polynomial.Polynomial([0]))

    def test_rmulCoeff1(self):
        self.assertEqual(2 * polynomial.Polynomial([1, 1, 1]), polynomial.Polynomial([2, 2, 2]))

    def test_rmulCoeff2(self):
        self.assertEqual((-2) * polynomial.Polynomial([1, 1, 1]), polynomial.Polynomial([-2, -2, -2]))

    def test_rmulCoeff3(self):
        self.assertEqual(0 * polynomial.Polynomial([1, 1, 1]), polynomial.Polynomial([0]))

unittest.main()

#print(repr(polynomial.Polynomial(0)))
# p = polynomial.Polynomial([1,1,1,1,1,1,1])
# for k,v in enumerate(p.coeffs):
#     print(k)