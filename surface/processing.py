import surface.base;

# ========================================
# ProcessingSurface
# ========================================

class ProcessingSurface(surface.base.SolSurface):
    """
    Load Processing jar and output sources.
    """
    def __init__(self, context):
        surface.base.SolSurface.__init__(self, context, supportsImmediateMode=True)
        pass

    def render(self):
        pass
