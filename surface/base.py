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
