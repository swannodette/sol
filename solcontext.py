import solobjects.path
from solutils.list import *	# import lastItem

# ==================================================
# Constants
# ==================================================

IMMEDIATE_MODE = 0
BATCH_MODE = 1

# ==================================================
# SolContext
# ==================================================

class SolContext:
  """
  Represents the drawing context
  """
  def __init__(self, surface=None, mode=IMMEDIATE_MODE):
    self.__surface = surface
    # set backreference from surface
    if self.__surface != None:
      self.__surface.setContext(self)

    # immediate mode or normal mode, do it all at the end of a drawing cycle
    self.mode = mode

    self.__stackVars = ('strokeColor', 
                        'fillColor', 
                        'lineWidth', 
                        'path', 
                        'clippingPath',
                        'point')

    # create current path and display list instance vars
    self.currentPath = None
    self.__displayList = []
    self.__strokeColor = []
    self.__fillColor = []
    self.__lineWidth = []
    self.__point = []
    self.__path = []
    self.__clippingPath = []
    self.__instructionStack = []
    self.__pageBounds = [0, 0, 100, 100]
    self.__scale = [0, 0, 1000, 1000]

  
  def saveState(self):
    """
    Saves the graphics state
    """
    pass


  def restoreGState(self):
    """
    Restores the graphics state
    """
    pass

  
  def getState(Self):
    """
    Returns a dict representing the current state
    """


  def point(self):
    return lastItem(self.__point)


  def fillColor(self):
    return lastItem(self.__fillColor)


  def lineWidth(self):
    return lastItem(self.__lineWidth)


  def path(self):
    return lastItem(self.__path)


  def setSurface(self, surface):
    """
    Sets the destination surface.
    """
    self.__surface = surface


  def surface(self):
    """
    Returns the destination surface.
    """
    return self.__surface

    
  def displayList(self):
    """
    Returns the display list (all the current paths).
    """
    return self.__displayList


  def beginPath(self):
    """
    Beging a path.
    """
    # create a new current path
    self.currentPath = solobjects.path.SolPath()


  def moveTo(self, x, y):
    """
    Move the virtual pen to a new location.
    """
    self.currentPath.moveTo(x, y)


  def lineTo(self, x, y):
    """
    Line to from the last point to the new point.
    """
    self.currentPath.lineTo(x, y)
    pass


  def arcTo(self, x, y):
    self.currentPath.arcTo(x, y)


  def bezierTo(self, cp0x, cp0y, p0x, p0y, cp1x, cp1y):
    self.currentPath.bezierTo(cp0x, cp0y, p0x, p0y, cp1x, cp1y)


  def closePath(self):
    self.currentPath.closePath()


  def stroke(self):
    # update the display list the path
    self.__displayList.append(self.currentPath)


  def fill(self):
    # update the display list with the path
    self.__displayList.append(self.currentPath)


  def drawImage(self):
    pass


  def fillRect(self):
    pass


  def fillEllipse(self):
    pass


  def clearRect(self):
    pass


  def translate(self):
    pass


  def rotate(self):
    pass


  def scale(self):
    pass


  def setCTM(self, ctm):
    pass


  def save(self):
    pass


  def restore(self):
    pass


  def flush(self):
    """
    Flush all current drawing instructions.
    """
    pass
