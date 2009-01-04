import serial 			# for talking to the plotter, install from sourceforge
import copy 			# for copying objects

import solmath.vector 		# custom vector class
import solcontext		# load the context class
import surface.hpgl 		# load hpgl support

# StringIO.StringIO() creates an output "file"
# StringIO.StringIO(bufferString) creates an input "file"

# Immediate mode will render right away if appropiate
# Batch will render when flushed

ctxt = None
def test():
  global ctxt
  ctxt = solcontext.SolContext(surface.hpgl.HPGLSurface())
  ctxt.beginPath()
  ctxt.moveTo(0, 0)
  ctxt.lineTo(50, 0)
  ctxt.lineTo(50, 50)
  ctxt.lineTo(0, 50)
  ctxt.closePath()
  ctxt.stroke()
  ctxt.surface().toHPGL()
  ctxt.surface().printRenderList()
  ctxt.surface().writeToPlotter()

    
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
