import solmath.vector

# ========================================
# SolPath
# ========================================

class SolPath:
  """
  Abstraction for paths
  """
  strokeColor = None
  fillColor = None
  lineWidth = 1
  lineJoin = None

  def __init__(self):
    self.__instructions = []


  def setInstructions(self, instructions):
    self.__instructions = instructions


  def instructions(self):
    return self.__instructions


  def addInstruction(self, instruction):
    self.__instructions.append(instruction)


  def moveTo(self, x, y):
    # add the point, return self
    self.addInstruction(('moveTo', (solmath.vector.Vector(x, y))))
    return self


  def lineTo(self, x, y):
    self.addInstruction(('lineTo', (solmath.vector.Vector(x, y))))
    return self


  def arcTo(self, point):
    pass


  def bezierTo(self, cp0x, cp0y, p0x, p0y, cp1x, cp1y):
    self.addInstruction(('bezierTo', (solmath.vector.Vector(cp0x, cp0y), 
                                      solmath.vector.Vector(p0x, p0y), 
                                      solmath.vector.Vector(cp1x, cp1y))))
    pass


  def closePath(self):
    self.addInstruction(('lineTo', (self.__instructions[0][1])))
    pass
