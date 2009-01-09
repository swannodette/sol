import serial
import solutils.string
import surface.base
import solobjects.path
import solobjects.layer
import solmath.vector

PAPER_SIZE_A4 = "A4"

# x y dimensions are swapped when
# using the plotter
HPGLMediaDimensionsTable = {
  "A4": (279, 216),
}

HPGLMediaMaxDimensionsTable = {
  "A4": (10160, 7840)
}

HPGLMediaMarginsTable = {
  "A4": (16, 12, 4, 12)
}

HPGLMediaRatioTable = {
  "A4": float(HPGLMediaDimensionsTable["A4"][0])/
        float(HPGLMediaDimensionsTable["A4"][1])
}

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


  def __init__(self, 
               left=0.0, 
               bottom=0.0, 
               right=1.0, 
               top=1.0,
               mediaSize=PAPER_SIZE_A4):
    # for treating strings like streams; good ol' Lisp
    import StringIO
    
    surface.base.SolSurface.__init__(self, supportsImmediateMode=True)

    self.setRenderList([])
    self.setCurrentPathRenderList([])
    self.setScale(1, 1)
    self.setMediaSize(mediaSize)
    self.setOrtho2D(left, bottom, right, top)


  def drawing(self):
    """
    Generates all the instructions of the drawing.
    """
    return (self.deviceInitializers() +
            self.plotterUnitInitializers() + 
            self.scaleInitializers() +       
            self.renderList())

  
  def setMediaSize(self, size):
    """
    Sets the media size.
    """
    self.__mediaSize = size


  def mediaSize(self):
    return self.__mediaSize

  
  def setOrtho2D(self, left, bottom, right, top):
    """
    Set the scale and units of the drawing surface.
    """
    mediaSize = self.mediaSize()

    width = abs(left-right)
    height = abs(top-bottom)

    if width >= height:
      height = width * (1.0/HPGLMediaRatioTable[mediaSize])
    else:
      width = height * HPGLMediaRatioTable[mediaSize]
    
    self.__orthod2d = (solmath.vector.Vector(bottom, left), 
                       solmath.vector.Vector(width, height))

    print "Printing ortho!"
    print self.__orthod2d


  def ortho2D(self):
    """
    Return the coordinate system.
    """
    return self.__orthod2d


  def width(self):
    return self.__orthod2d[2]


  def height(self):
    return self.__orthod2d[3]


  def origin(self):
    return (self.__orthod2d[0], self.__orthod2d[1])


  def setViewport(self, x, y, width, height):
    """
    Set the viewport of the surface.
    """
    pass


  def mediaSize(self):
    """
    Returns the media size, one of the above paper size constants.
    """
    return self.__mediaSize


  def setPen(self, path):
    """
    Set the current pen based on path information.
    """
    self.addToRenderList("SP1;")


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
    """
    Returns the current path render list.
    """
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
      return ["IP0,0,1,1;"]


  def setScale(self, x, y):
    """
    Sets the scale of the drawing.
    """
    self.__xscale = x
    self.__yscale = y


  def setClipping(self):
    """
    Returns the clipping instructions.
    """
    # IW, input window
    pass


  def mapPoint(self, vector):
    """
    Convert a floating point value to the destination value.
    """
    dim = HPGLMediaMaxDimensionsTable[self.mediaSize()]
    origin = self.ortho2D()[0]
    size = self.ortho2D()[1]
    # (v - ov) * dim.x/ov.x
    return ((vector - origin) * (dim[0]/size.x)).int()


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
    return ["SC0,%s,0,%s;" % self.getScale()]


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
    self.setPen(path)
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


  def connectToPlotter(self):
    """
    Make a serial connection to a plotter. Assumes your using
    the KeySpan highspeed USB to DB9 dongle.
    """
    try:
      ser = serial.Serial("/dev/tty.KeySerial1", 9600,
                    timeout = 	1,
                    bytesize = 	serial.EIGHTBITS,
                    stopbits = 	serial.STOPBITS_ONE,
                    parity =	serial.PARITY_ODD,
                    xonxoff = 	1)
      return ser
    except Exception:
      return None


  def writeToPlotter(self):
    """
    Write out the render list to the plotter.
    """
    # open up a connection, good defaults, should explore this more
    ser = self.connectToPlotter()    

    def hpglcom(command):
      print "send %s" % command
      # issue the command, should probably auto add semis
      ser.write(command)
      # for handshaking
      ser.read()

    if ser != None:
      for command in self.drawing():
        hpglcom(command)
      ser.close()
    else:
      print "No plotter connected, please connect one."


