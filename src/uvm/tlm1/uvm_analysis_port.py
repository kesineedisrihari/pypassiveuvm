class uvm_anlaysis_port(uvm_port_base):

    def __init__(self, string name : str, parent = uvm_component):
        super.__init__(name, parent, UVM_PORT, 0, UVM_BOUNDED_CONNECTIONS)

    def get_type_name():
        return 'uvm_anlaysis_port'

    def write(T t):
        self.tif = uvm_tlm_if_base()
        for i in self.size():
            tif = self.get_if(i)
            if tif is None:
                uvm_report_fatal('','')
            tif.write(t)

class uvm_analysis_imp(uvm_component):

    def __init__(self, name : str, parent)
        super.__init__(name, parent)

    def write(t):
        m_imp.write(t)

class uvm_analysis_export(uvm_component):
    def __init__(self, name : str, parent):
        super.__init__(name, parent)

    def get_type_name()-> str:
        return 'uvm_analysis_export'

    def write(t):
        self.m_imp.write(t)
