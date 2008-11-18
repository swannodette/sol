# ========================================
# SolLayer
# ========================================

class SolLayer:
  """
  Abstraction for layers
  """
  def __init__(self):
    pass

class Sol:
  def __init__(self):
    self.__context__ = None # cairo or plotter
    self.__mode__ = None    # immediate mode, or batch mode
    pass

  def context(self):
    pass
