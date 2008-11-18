import surface.base
import objects.path

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
    self.renderList.append(".(;")
    self.renderList.append(".I81;")
    self.renderList.append(";")
    self.renderList.append("17:.N;")
    self.renderList.append("19:IN;")
    pass


  def setCurrentPath(self, path):
    self.__currentPath = path


  def currentPath(self):
    return self.__currentPath


  def setCurrentLayer(self, layer):
    self.__currentLayer = layer


  def currentLayer(self):
      return self.__currentLayer


  def buildZTable(self, displayList):
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
      methodName = "parse%s" % capitalize(instruction[0])
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
      if object.__class__ == objects.path.SolPath:
        self.processPath(object)
      if object.__class__ == objects.layer.SolLayer:
        self.processLayer(object)
    # process each layer
    print self.renderList


