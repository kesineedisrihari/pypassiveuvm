import asyncio
class uvm_tlm_fifo(uvm_tlm_fifo_base):

    def __init__(self, T : type = int, name : str, parent, size : int = 1):
        super.__init__(T, name, parent)
        self.m = asyncio.Queue(size)
        self.m_size = size

    def get_type_name()->str:
        pass

    def size():
        return self.m_size

    def used()->int:
        return self.m.qsize()

    def is_empty()->bool:#FIXME : check if it can be made to bool
        return self.m.qsize() == 0

    def is_full()->bool:
        return self.m_size != 0 and self.m.qsize() == self.m_size

    async def put(t):
        await self.m.put(t)

    async def get(t):
        await self.m.get(t)


    def try_get(t) -> bool:
        try:
            t = self.m.get_nowait()
            return True
        except:#QueueEmpty
            return False

        #return await get_ap.write(t)
        get_ap.write(t)

    def try_peek(t)->bool:
        pass

    def try_put(t) -> bool:
        try:
            self.m.put_nowait(t)
            return True
        except:#FIXME add QueueFull exception
            return False

        put_ap.write(t)

    def can_put()-> bool:
        #return not self.m.full()
        return self.m_size == 0 or self.m.qsize() < self.m_size

    def can_get() -> bool:
        #FIXME : dont know how to deal with m_pending_blocked_gets
        pass

    def can_peek():
        return self.m.qsize() > 0

    def flush():
        t = None
        r = True
        while(r):
            r = try_get(t)
        if self.m.qsize() > 0:#FIXME m_pending_blocked_gets
            #uvm_error()
            pass

class uvm_tlm_analysis_fifo(uvm_tlm_fifo):

    def __init__(self, name : str, parent : uvm_component, T : int):
        super.__init__(name, parent)

