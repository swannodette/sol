import serial
import solutils.string
import surface.base
import solobjects.path
import solobjects.layer

# ========================================
# HPGLSurface
# ========================================

class HPGLSurface(surface.base.SolSurface):
  """
  Output to device or to a text file.
  """
  def __init__(self):
    # for treating strings like streams; good ol' Lisp
    import StringIO
    
    surface.base.SolSurface.__init__(self, supportsImmediateMode=True)
    self.renderList = []
    self.currentPathRenderList = []
    self.initializeDevice()
    pass

  
  def initializeDevice(self):
    """
    Generates the instructions needed to initialize the plotter.
    """
    self.renderList.append(".(;")
    self.renderList.append(".I81;")
    self.renderList.append(";")
    self.renderList.append("17:.N;")
    self.renderList.append("19:IN;")
    pass


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
    print point
    self.currentPathRenderList.append("PU;")
    self.currentPathRenderList.append("PA%d,%d;" % tuple(point))
    pass


  def parseLineTo(self, point):
    self.currentPathRenderList.append("PA%d,%d;" % tuple(point))
    pass


  def parseArcTo(self, arguments):
    pass


  def parseBezierTo(self, arguments):
    # decompose the bezier
    pass


  def parseStroke(self):
    # commit the path
    self.renderList.append("PD;")
    self.renderList.extend(self.currentPathRenderList);
    pass


  def parseFill(self):
    # commit the path
    pass


  def processPath(self, path):
    """
    Process a single path.
    """
    print "Processing path"
    self.setCurrentPath(path)
    for instruction in path.instructions():
      print instruction
      methodName = "parse%s" % solutils.string.capitalize(instruction[0])
      print methodName
      # extend the render list with the result
      getattr(self, methodName)(instruction[1])
    return self


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
    print "toHPGL"
    print displayList
    # build a z table for hidden line removal
    for object in displayList:
      print "object %s" % object
      if object.__class__ == solobjects.path.SolPath:
        self.processPath(object)
      if object.__class__ == solobjects.layer.SolLayer:
        self.processLayer(object)
    # process each layer
    print self.renderList


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

    for command in self.renderList:
      hpglcom(command)


