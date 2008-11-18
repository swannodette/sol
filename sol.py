import serial 			# for talking to the plotter, install from sourceforge
import copy 			# for copying objects
import math.vector 		# custom vector class
import solcontext
import surface.hpgl 		# load hpgl support

# StringIO.StringIO() creates an output "file"
# StringIO.StringIO(bufferString) creates an input "file"

# Immediate mode will render right away if appropiate
# Batch will render when flushed

def capitalize(string):
    return string[0].upper() + string[1:len(string)]

ctxt = None
def test():
    global ctxt
    ctxt = solcontext.SolContext(surface.hpgl.HPGLSurface())
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
