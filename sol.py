import serial 			# for talking to the plotter
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
    def __init__(self, context, supportsImmediateMode=False):
        self.context = context
        self.__supportsImmediateMode__ = supportsImmediateMode
        pass

    def setSupportsImmediateMode(self, value):
        self.__supportsImmediateMode__ = value

    def supportsImmediateMode(self):
        return self.__supportsImmediateMode__


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
    def __init__(self, context):
        # for treating strings like streams; good ol' Lisp
        import StringIO

        SolSurface.__init__(self, context, supportsImmediateMode=True)
        self.renderList = []
        pass

    def buildZTable(self, displayList):
        pass

    def parseMoveTo(self, arguments):
        self.renderList.append("PA%d,%d" % arguments)
        pass

    def parseLineTo(self, arguments):
        
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
        for instruction in path:
            # extend the render list with the result
            self.renderList.append(getAttr("parse" + capitalize(instruction[0]))(instruction[0]), self)
            pass
        return self

    def processLayer(self, path):
        # check if not immediate mode
        pass

    def toHPGL(self):
        displayList = self.context.displayList
        # build a z table for hidden line removal
        for object in displayList:
            if object.__class__ == SolPath:
                self.processPath(object)
            if object.__class__ == SolLayer:
                self.processLayer(object)
        # process each layer

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

    def moveTo(self, point):
        # add the point, return self
        self.__instructions.append(('moveTo', (point)))
        return self

    def lineTo(self, point):
        self.__instructions.append(('lineTo', (point)))
        return self

    def arcTo(self, point):
        pass

    def bezierTo(self, cp0, p1, cp1):
        self.__instructions.append('bezierTo', (cp0, p1, cp1))
        pass

    def closePath(self):
        self.__instructions.append('lineTo', self.instructions[0][0])
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
        # set the surface and backreference
        self.__surface = surface

        if self.__surface != None:
            self.__surface.setContext(self)

        # immediate mode or normal mode, do it all at the end of a drawing cycle
        self.mode = mode
        
        # create current path and display list instance vars
        self.currentPath = None
        self.displayList = []


    def setSurface(self, surface):
        self.__surface = surface


    def surface(self):
        return self.__surface


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
        self.currentPath.close()
        pass


    def stroke(self):
        self.currentPath.stroke()
        # update the display list the path
        self.displayList.append(self.currentPath)
        pass


    def fill(self):
        self.currentPath.fill()
        # update the display list with the path
        self.displayList.append(self.currentPath)
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
