class uvm_tlm_fifo(uvm_component):

    def __init__(self, name : str, parent):
        super.__init__(name, parent)
        m = mailbox(size, T)

    def size():
        return self.m_size()

    def try_put(t):
        m.put(t)

    def put(t):
        m.put(t)

    def get(t):
        m.get(t)

class uvm_tlm_analysis_fifo(uvm_tlm_fifo):

    def __init__(self, name : str, parent : uvm_component):
        super.__init__(name, parent)

