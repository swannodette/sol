import surface.base;

# ========================================
# CairoSurface
# ========================================

class CairoSurface(surface.base.SolSurface):
    """
    Render to specified formats.
    """
    def __init__(self, context):
        surface.base.SolSurface.__init__(self, context)
        # import cairo
        import cairo
        pass

    def render(self):
        pass
