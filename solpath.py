# ========================================
# SolPath
# ========================================

class SolPath:
    """
    Abstraction for paths
    """
    strokeColor = None
    fillColor = None
    lineWidth = 1
    lineJoin = None

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

    
    def stroke(self):
        pass


    def closePath(self):
        self.addInstruction(('lineTo', (self.__instructions[0][1])))
    	pass
