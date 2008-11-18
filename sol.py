import serial 			# for talking to the plotter, install from sourceforge
import copy 			# for copying objects
from vector import Vector	# custom vector class
import solcontext

# StringIO.StringIO() creates an output "file"
# StringIO.StringIO(bufferString) creates an input "file"

# Immediate mode will render right away if appropiate
# Batch will render when flushed

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
        """Setter for the private context reference."""
        self.__context = context

    def context(self):
        """Getter for the private context reference."""
        return self.__context

    def setSupportsImmediateMode(self, value):
        """Set the immediate mode flag.  Not implemented."""
        self.__supportsImmediateMode = value

    def supportsImmediateMode(self):
        """Returns a boolean value stating whether this surface supports immediate mode."""
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
            if object.__class__ == SolPath:
                self.processPath(object)
            if object.__class__ == SolLayer:
                self.processLayer(object)
        # process each layer
        print self.renderList



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

ctxt = None
def test():
    global ctxt
    ctxt = solcontext.SolContext(HPGLSurface())
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
