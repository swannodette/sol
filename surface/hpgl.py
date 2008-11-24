import serial
import solutils.string
import surface.base
import solobjects.path
import solobjects.layer

PAPER_SIZE_A4 = 0

# ========================================
# HPGLSurface
# ========================================

class HPGLSurface(surface.base.SolSurface):
  """
  Output to device or to a text file.
  """

  __renderList = []
  __currentPathRenderList = []
  __mediaSize = []
  __scalex = 100
  __scaley = 100


  def __init__(self, scaleX=100, scaleY=100, mediaSize=None):
    # for treating strings like streams; good ol' Lisp
    import StringIO
    
    surface.base.SolSurface.__init__(self, supportsImmediateMode=True)

    self.setRenderList([])
    self.setCurrentPathRenderList([])
    self.setScale(scaleX, scaleY)
    self.setMediaSize(mediaSize or PAPER_SIZE_A4)


  def drawing(self):
    return self.deviceInitializers() +      \
           self.plotterUnitInitializers() + \
           self.scaleInitializers() +       \
           self.renderList()

  
  def setMediaSize(self, size):
    """
    Sets the media size.
    """
    self.__mediaSize = size


  def mediaSize(self):
    """
    Returns the media size, one of the above paper size constants.
    """
    return self.__mediaSize


  def renderList(self):
    return self.__renderList


  def setRenderList(self, newList):
    self.__renderList = newList


  def addToRenderList(self, data):
    """
    Adds an instruction or a list of instructions to
    the internal render list.
    """
    if isinstance(data, str):
      self.__renderList.append(data)
    if isinstance(data, list):
      self.__renderList.extend(data)

    
  def addToCurrentPathRenderList(self, data):
    """
    Adds instructions to the current path's
    render list.
    """
    if isinstance(data, str):
      self.__currentPathRenderList.append(data)
    if isinstance(data, list):
      self.__currentPathRenderList.extend(data)


  def setCurrentPathRenderList(self, newList):
    """
      
    Arguments:
    - `newList`:
    """
    self.__currentPathRenderList = newList

  
  def currentPathRenderList(self):
    return self.__currentPathRenderList

  
  def deviceInitializers(self):
    """
    Generates the instructions needed to initialize the plotter.
    """
    return [".(;", ".I81;", ";", "17:.N;", "19:IN;"]


  def plotterUnitInitializers(self):
    """
    Returns the instruction required to set plotter and user coordinates.
    """
    if self.mediaSize() == PAPER_SIZE_A4:
      return ["IP0,0,10760,8200"]


  def setScale(self, x, y):
    """
    Sets the scale of the drawing.
    """
    self.__xscale = x
    self.__yscale = y


  def xscale(self):
    return self.__xscale


  def yscale(self):
    return self.__yscale


  def getScale(self):
    """
    Returns the scale of this drawing.
    """
    return (self.xscale(), self.yscale())


  def scaleInitializers(self):
    """
    Return the scale initializers.
    """
    return ["SC0,%s,0,%s" % self.getScale()]


  def setCurrentPath(self, path):
    """
    Sets the current path.
    """
    self.__currentPath = path


  def currentPath(self):
    """
    Returns the current path, a SolPath instance.
    """
    return self.__currentPath


  def setCurrentLayer(self, layer):
    """
    Sets the current layer.
    """
    self.__currentLayer = layer


  def currentLayer(self):
    """
    Returns the current layer.
    """
    return self.__currentLayer


  def buildZTable(self, displayList):
    """
    Build the z table needed for hidden line removal.
    """
    pass


  def parseMoveTo(self, point):
    return ["PU;","PA%d,%d;" % tuple(point), "PD;"]


  def parseLineTo(self, point):
    return "PA%d,%d;" % tuple(point)


  def parseArcTo(self, arguments):
    pass


  def parseBezierTo(self, arguments):
    # decompose the bezier
    pass


  def processPath(self, path):
    """
    Process a single path.
    """
    self.setCurrentPath(path)
    for instruction in path.instructions():
      methodName = "parse%s" % solutils.string.capitalize(instruction[0])
      # extend the render list with the result
      self.addToCurrentPathRenderList(getattr(self, methodName)(instruction[1]))

    return self.currentPathRenderList()


  def processLayer(self, path):
    """
    Process a layer.
    """
    # check if not immediate mode
    pass


  def toHPGL(self):
    """
    Converts the display list of the associated Sol context to HPGL instructions.
    """
    displayList = self.context().displayList()
    # build a z table for hidden line removal
    for object in displayList:
      if object.__class__ == solobjects.path.SolPath:
        self.addToRenderList(self.processPath(object))
      if object.__class__ == solobjects.layer.SolLayer:
        self.addToRenderList(self.processLayer(object))
    self.addToRenderList("PU;")


  def printRenderList(self):
    """
    For debugging print the render list in a human readable format.
    """
    for instruction in self.drawing():
      print instruction


  def writeToPlotter(self):
    """
    Write out the render list to the plotter.
    """
    # open up a connection, good defaults, should explore this more
    ser = serial.Serial("/dev/tty.KeySerial1", 9600,
                        timeout = 	1,
                        bytesize = 	serial.EIGHTBITS,
                        stopbits = 	serial.STOPBITS_ONE,
                        parity =	serial.PARITY_ODD,
                        xonxoff = 	1)
    

    def hpglcom(command):
      print "send %s" % command
      # issue the command, should probably auto add semis
      ser.write(command)
      # for handshaking
      ser.read()

    for command in self.drawing:
      hpglcom(command)


