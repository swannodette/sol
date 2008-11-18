# import solpath
import objects.path

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
    self.currentPath = objects.path.SolPath()


  def moveTo(self, point):
    """
    Move the virtual pen to a new location.
    """
    self.currentPath.moveTo(point)
    pass


  def lineTo(self, point):
    """
    Line to from the last point to the new point.
    """
    self.currentPath.lineTo(point)
    pass


  def arcTo(self, point):
    self.currentPath.lineTo(point)
    pass


  def bezierTo(self, cp0, p1, cp1):
    self.currentPath.bezierTo(cp0, p1, cp1)
    pass


  def closePath(self):
    self.currentPath.closePath()
    pass


  def stroke(self):
    # update the display list the path
    self.currentPath.stroke()
    self.__displayList.append(self.currentPath)
    pass


  def fill(self):
    self.currentPath.fill()
    # update the display list with the path
    self.__displayList.append(self.currentPath)
    pass


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
