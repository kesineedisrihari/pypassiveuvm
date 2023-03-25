import sys

class sv_mailbox:

    def __init__(self, bound : int = 0, T = None):#FIXME : change the default type from None to int
        self.m = []
        self.bound = bound
        if T is None:
            self.type = 'sv_int'
        else:
            self.type = type(T).__name__

    def num(self):
        return len(self.m)

    def try_put(self, t) -> int :
        if self.bound != 0 and len(self.m) == self.bound:
            return 0
        else:
            if type(t).__name__ == self.type:
                self.m.append(t)
                return 1
            else:
                sys.exit('inserting element of type(%s) in to mailbox of type(%s)'%(type(t),self.type))
                #FIXME : add similar kind of typec in all the things

    async def put(self, t):
        if self.bound > 0:
            await len(self.m) > 0
        else:
            await len(self.m) < self.bound
            if isinstance(t, self.type):
                self.m.append(t)
            else:
                sys.exit('inserting element of type(%s) in to mailbox of type(%s)'%(type(t),self.type))

    async def get(self, t):
        await len(self.m) > 0
        t = self.m.pop(0)

    def try_get(self, t) -> int:
        if len(self.m) == 0:
            return 0
        else:
            t.value  = self.m.pop(0).value #FIXME : add type checking for the popped value and the assigned value
            return 1

    async def peek(t):
        await len(self.m) > 0
        t = self.m[0]

    def try_peek(self, t) -> int:
        t = self.m[0]
        return 0 if t == None else 1


