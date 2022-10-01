class hierarchy:

    def __init__(self, value : str):
            self.value = value
            if value.endswith(']'):
                tmp = value.split('[')[-1].replace(']','')
                if ':' in tmp:
                    a,b = tmp.split(':')
                    self.msb = int(a)
                    self.lsb = int(b)
                else:
                    self.width = 1
                    self.msb = int(tmp)
                    self.lsb = int(tmp)

    def get_width():
        return self,width

    def get_msb():
        return self.msb

    def get_lsb():
        return self.lsb

