import serial 			# for talking to the plotter, install from sourceforge
import copy 			# for copying objects
from vector import Vector	# custom vector class

# StringIO.StringIO() creates an output "file"
# StringIO.StringIO(bufferString) creates an input "file"

# Immediate mode will render right away if appropiate
# Batch will render when flushed
IMMEDIATE_MODE = 0
BATCH_MODE = 1

def capitalize(string):
    return string[0].upper() + string[1:len(string)]

# ========================================
# SolSurface
# ========================================

class SolSurface:
    """
    Abstract class for destination renderers.
    """
    def __init__(self, supportsImmediateMode=False):
        self.__context = None
        self.__supportsImmediateMode = supportsImmediateMode
        pass

    def setContext(self, context):
        self.__context = context

    def context(self):
        return self.__context

    def setSupportsImmediateMode(self, value):
        self.__supportsImmediateMode = value

    def supportsImmediateMode(self):
        return self.__supportsImmediateMode


# ========================================
# ProcessingSurface
# ========================================

class ProcessingSurface(SolSurface):
    """
    Load Processing jar and output sources.
    """
    def __init__(self, context):
        SolSurface.__init__(self, context, supportsImmediateMode=True)
        pass

    def render(self):
        pass


# ========================================
# CairoSurface
# ========================================

class CairoSurface(SolSurface):
    """
    Render to specified formats.
    """
    def __init__(self, context):
        SolSurface.__init__(self, context)
        # import cairo
        import cairo
        pass

    def render(self):
        pass


# ========================================
# HPGLSurface
# ========================================

class HPGLSurface(SolSurface):
    """
    Output to device or to a text file.
    """
    def __init__(self):
        # for treating strings like streams; good ol' Lisp
        import StringIO
        
        SolSurface.__init__(self, supportsImmediateMode=True)
        self.renderList = []
        self.currentPathRenderList = []
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
        pass

    def parseFill(self):
        pass

    def processPath(self, path):
        print "Processing path"
        self.setCurrentPath(path)
        for instruction in path.instructions():
            print instruction
            methodName = "parse%s" % capitalize(instruction[0])
            print methodName
            # extend the render list with the result
            self.renderList.append(getattr(self, methodName)(instruction[1]))
            pass
        return self

    def processLayer(self, path):
        # check if not immediate mode
        pass

    def toHPGL(self):
        displayList = self.context().displayList()
        print "toHPGL"
        print displayList
        # build a z table for hidden line removal
        for object in displayList:
            print "object %s" % object
            if object.__class__ == SolPath:
                self.processPath(object)
            if object.__class__ == SolLayer:
                self.processLayer(object)
        # process each layer
        print self.currentPathRenderList

# ========================================
# SolPath
# ========================================

class SolPath:
    """
    Abstraction for paths
    """
    def __init__(self):
        self.__instructions = []

    def setInstructions(self, instructions):
        self.__instructions = instructions

    def instructions(self):
        return self.__instructions

    def addInstruction(self, instruction):
        print "Add instruction (%s, %s)" % instruction
        self.__instructions.append(instruction)

    def moveTo(self, point):
        # add the point, return self
        self.addInstruction(('moveTo', (point)))
        return self

    def lineTo(self, point):
        self.addInstruction(('lineTo', (point)))
        return self

    def arcTo(self, point):
        pass

    def bezierTo(self, cp0, p1, cp1):
        self.addInstruction(('bezierTo', (cp0, p1, cp1)))
        pass

    def closePath(self):
        self.addInstruction(('lineTo', (self.__instructions[0][1])))
    	pass


# ========================================
# SolLayer
# ========================================

class SolLayer:
    """
    Abstraction for layers
    """
    def __init__(self):
        pass


# ========================================
# SolContext
# ========================================

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
        
        # create current path and display list instance vars
        self.currentPath = None
        self.__displayList = []


    def setSurface(self, surface):
        self.__surface = surface


    def surface(self):
        return self.__surface

    
    def displayList(self):
        return self.__displayList


    def beginPath(self):
        # create a new current path
        self.currentPath = SolPath()


    def moveTo(self, point):
        self.currentPath.moveTo(point)
        pass


    def lineTo(self, point):
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

    # Here is a place where Lisp's maskable alists
    # make a whole lot of sense!
    def save(self):
        pass


    def restore(self):
        pass


    def flush(self):
        """
        Flush all current drawing instructions.
        """
        pass


class Sol:
    def __init__(self):
        self.__context__ = None # cairo or plotter
        self.__mode__ = None    # immediate mode, or batch mode
        pass

    def context(self):
        pass

ctxt = None
def test():
    global ctxt
    ctxt = SolContext(HPGLSurface())
    ctxt.beginPath()
    ctxt.moveTo(Vector(10, 10))
    ctxt.lineTo(Vector(50, 50))
    ctxt.closePath()
    ctxt.stroke()
    ctxt.surface().toHPGL()

"""
surface = HPGLSurface()
context = SolContext(surface)

context.beginPath()
context.moveTo(0, 0)
context.lineTo(100, 0)
context.lineTo(0, 100)
context.lineTo(100, 100)
context.lineTo(0, 100)
context.closePath()
context.stroke()

# open up a connection, good defaults, should explore this more
ser = serial.Serial("/dev/tty.USA19H3d1P1.1", 9600,
              timeout = 	1,
              bytesize = 	serial.EIGHTBITS,
              stopbits = 	serial.STOPBITS_ONE,
              parity =		serial.PARITY_ODD,
              xonxoff = 	1)

hpgl = surface.toHPGL()

for instruction in hpgl:
    ser.write(instruction)

ser.close()
"""
