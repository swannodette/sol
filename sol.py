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
