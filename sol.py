import solcontext		# load the context class
import surface.hpgl 		# load hpgl support

# StringIO.StringIO() creates an output "file"
# StringIO.StringIO(bufferString) creates an input "file"

# Immediate mode will render right away if appropiate
# Batch will render when flushed

ctxt = None
surf = None

def test():
  global ctxt
  ctxt = solcontext.SolContext(surface.hpgl.HPGLSurface())
  ctxt.beginPath()
  ctxt.moveTo(0, 0)
  ctxt.lineTo(254, 0)
  ctxt.lineTo(254, 196)
  ctxt.lineTo(0, 196)
  ctxt.closePath()
  ctxt.stroke()
  ctxt.surface().toHPGL()
  ctxt.surface().printRenderList()
  ctxt.surface().writeToPlotter()


def test2():
  global ctxt
  ctxt = solcontext.SolContext(surface.hpgl.HPGLSurface())
  ctxt.beginPath()
  ctxt.moveTo(0, 0)
  ctxt.lineTo(10160, 0)
  ctxt.lineTo(10160, 7840)
  ctxt.lineTo(0, 7840)
  ctxt.closePath()
  ctxt.stroke()
  ctxt.surface().toHPGL()
  ctxt.surface().printRenderList()
  ctxt.surface().writeToPlotter()


def test3():
  global ctxt
  global surf
  surf = surface.hpgl.HPGLSurface(left=0, bottom=0, right=2.0, top=1.0, 
                                  mediaSize=surface.hpgl.PAPER_SIZE_A4)
  ctxt = solcontext.SolContext(surf)

  from solmath.vector import Vector
  print surf.mapPoint(Vector(1.0, 1.0))


