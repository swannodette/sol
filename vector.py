from math import *

# An 2D Vector class for the Sol Project
# Will eventually need a 3 component one
class Vector():
  """
  2D Vector class.
  """
  def __init__(self, x, y):
    # need to make sure we're dealing with floats here
    self.x = float(x)
    self.y = float(y)

  def __add__(self, other):
    """
    Add one vector to another and return a new vector.
    """
    return Vector(self.x + other.x, self.y + other.y)

  def __sub__(self, other):
    """
    Subtract this vector from another. Returns a new vector.
    """
    return Vector(self.x - other.x, self.y - other.y)

  def __mul__(self, scalar):
    """
    Multiply this vector by a scalar. Returns a new vector.
    """
    return Vector(self.x * scalar, self.y * scalar)

  def __div__(self, scalar):
    return Vector(self.x / scalar, self.y / scalar)
    
  def __neg__(self):
    """
    Return this vector * -1.
    """
    return Vector(-self.x, -self.y)

  def __repr__(self):
    """
    Return the string representation of this vector.
    """
    return self.__str__()
    
  def __str__(self):
    """
    Return the string represenation of this vector.
    """
    return "<%f, %f>" % (self.x, self.y)

  def length(self):
    """
    Return the vector length (a float).
    """
    return sqrt(self.x**2 + self.y**2)

  def lengthSquared(self):
    """
    Return the length of this vector squared.
    """
    return self.x**2 + self.y**2

  def normalize(self):
    """
    Return a new normalized vector.
    """
    length = self.length()
    return Vector(self.x/length, self.x/length)

  def isZero(self):
    """Check to see if this vector is close to the zero vector."""
    return self.x == 0 and self.y == 0
    
  def isUnit(self):
    """
    Check to see if this is a unit vector.
    """
    return self.isZero(1.0 - self.x*self.x - self.y*self.y);

  def clean(self):
    """
    If this vector's components are close to zero, set them to zero.
    """
    if IsZero(self.x):
      self.x = 0
    if IsZero(self.y):
      self.y = 0

  def dot(self, other):
    """
    Return the dot produt of this vector.
    """
    return (self.x*other.x + self.y*other.y)
    
  def proj(self, other):
    """
    Project this vector onto another vector and return it.
    """
    return (other*self.dot(other)) / other.length()
    
  def perp(self):
    """
    Return a vector perpendicular to this one.
    """
    return Vector(-self.y, -self.x)
    
  def copy(self):
    """
    Return a copy of this vector.
    """
    return Vector(self.x, self.y)
    
  def getX(self):
    return self.x
    
  def getY(self):
    return self.y


def ZeroVector():
  """
  Convenience function, returns the zero vector.
  """
  return Vector(0.0, 0.0)


def IsZero(a):
  """
  Convenience function, checks to see if a number is close to zero.
  """
  return a < 0.00001
