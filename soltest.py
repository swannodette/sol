import vector
import unittest

class VectorBaseCheck(unittest.TestCase):
  def testEquals(self):
    v = vector.Vector(1,1)
    self.assertEqual(v, v)

class VectorMathCheck(unittest.TestCase):
  """
  Check that values of each main method returns sane values.
  """

  def testAdd(self):
    """adding two vectors should return a correct result"""
    v1 = vector.Vector(1.1, 2.0)
    v2 = vector.Vector(1/3, 9)
    v3 = vector.Vector(1.1+(1/3), 2.0+9)
    self.assertEqual(v1+v2, v3)

  def testSub(self):
    """subtracting two vectors should return a correct result"""
    v1 = vector.Vector(5, 7)
    v2 = vector.Vector(4, 8)
    v3 = vector.Vector(1, -1)
    self.assertEqual(v1-v2, v3)

  def testMul(self):
    """Multiply a vector with a scalar should return a correct result"""
    v1 = vector.Vector(3.3, 4.00005)
    n = 1.99
    v2 = vector.Vector(3.3*n, 4.00005*n)
    self.assertEqual(v1 * n, v2)

  def testDiv(self):
    """Dividing a vector with a scalar should return a correct result"""
    v1 = vector.Vector(9.45, 0.16)
    n = 0.77
    v2 = vector.Vector(9.45/n, 0.16/n)
    self.assertEqual(v1 / n, v2)
    

if __name__ == "__main__":
  unittest.main()
