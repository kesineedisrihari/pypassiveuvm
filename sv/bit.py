class bit:

    def __init__(self, width : int = 1, value : int = 0):
        self.width = width
        self.value = value


    def get(self, pos : int):
            if pos > self.width - 1:
                sys.exit('accessing bit position(%0d) whose width is(%0d)'%(pos, self.width))
            else:
                return (self.value >> pos) & 1

    def set(self, val : int, msb : int , lsb : int = None):
            if lsb is None:
                self.value | (val & 1) << msb
            else:
                self.value | val << lsb

