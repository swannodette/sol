import unittest
from surface.hpgl import HPGLSurface
from solcontext import SolContext

class SolContextTest(unittest.TestCase):
  """
  Tests the SolContext class.
  """

  def setup(self):
    self.context = SolContext(surface.hpgl.HPGLSurface())
    pass

  def teardown(self):
    pass

  def testSaveGState(self):
    pass
