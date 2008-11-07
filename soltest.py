import vector
import math
import unittest

# ======================================== #
# VectorBaseCheck
# ======================================== #

class VectorBaseCheck(unittest.TestCase):
  def testEquals(self):
    v = vector.Vector(1,1)
    self.assertEqual(v, v)

  def testSequenceProtocol(self):
    pass

  def testIteratorProtocol(self):
    pass
  

# ======================================== #
# VectorMathCheck
# ======================================== #

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

  def testNeg(self):
    """Test neg returns a vector with the opposite direciton"""
      v1 = vector.Vector(5, 1)
    v2 = vector.Vector(-5, -1)
    self.assertEqual(-v1, v2)

  def testLength(self):
    """Test that the length of the vector returns a correct result"""
    v1 = vector.Vector(5, 4.2)
    self.assertEqual(v1.length(), math.sqrt(5*5 + 4.2*4.2))

  def testLengthSquared(self):
    """Test that lengthSquared returns the correct value"""
    v1 = vector.Vector(5, 3.1)
    self.assertEqual(v1.lengthSquared(), 5*5+3.1*3.1)

  def testNormalize(self):
    """Test that normalize returns a unit vector in the same direction"""
    v1 = vector.Vector(4, 5)
    v2 = v1.normalize()
    # v2 is a unit vector
    self.assertTrue(v2.isUnit())
    # check that the direction of v2 is still the same as v1
    self.assertTrue(v1.sameDirection(v2))

  def testIsZero(self):
    """Check that if zero check returns the proper value"""
    v1 = vector.Vector(0.0, 0.0)
    self.assertTrue(v1.isZero())

  def testIsUnit(self):
    """Test whether a vector has length 1"""
    v1 = vector.Vector(5, 4)
    v2 = v1.normalize()
    self.assertTrue(v2.isUnit())

  def testSameDirection(self):
    """Test check for same direction for two vectors of different magnitudes"""
    v1 = vector.Vector(5, 4)
    v2 = vector.Vector(10, 8)
    self.assertTrue(v1.sameDirection(v2))

  def testClean(self):
    """Test that clean moves a vector that's close to the zero vector"""
    v1 = vector.Vector(0.000000001, 0.00000000000001)
    v1.clean()
    self.assertTrue(v1.x == 0.0 and v1.y == 0.0)

  def testProj(self):
    """Test projections return the correct value"""
    pass

  def testPerp(self):
    """Test that perpendicular returns the correct value"""
    v1 = vector.Vector(5, 10).perp()
    self.assertTrue(v1 == vector.Vector(-10, -5))

  def testDot(self):
    """Test that dot product returns the correct value"""
    pass

if __name__ == "__main__":
  unittest.main()
