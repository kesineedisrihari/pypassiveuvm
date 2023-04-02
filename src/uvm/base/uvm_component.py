class uvm_component(uvm_report_object):
    _m_inst_count = 0

    def __init__(self, name : str = '', parent = None):
        _m_inst_count += 1
        self._m_children = []
        self._m_parent = parent
        super().__init__(name)

        if name =='':
            self.name = 'COMP_'+str(_m_inst_count)

        if parent is self:
            sys.exit()
        elif parent is None:
            top = get_root()
            self.parent = top

        self._m_parent = self.parent

        try:
            self._m_parent._m_add_child(self)
        except:
            self._m_parent = None


    def _m_add_child(child):
        if child.get_name() in self._m_children:
            uvm_warning('BCLD', 'A child with name(%s) type(%s) cleady exists')

    def get_children(children[] : uvm_component):
        for child in m_children:
            children.append(child.copy())

    def get_first_child(name : sv_str)-> int:#since string is immutable we are using wrapper sv_str
        return m_children.first(name)

    def get_next_child(name : sv_str)-> int:#since string is immutable we are using wrapper sv_str
        return m_children.next(name)

    def get_child(string name) -> uvm_component:
        if m_children.exits(name):
            return m_children[name]
        uvm_warning("NOCHILD", "component with name "+name+"is not a child of component"+get_full_name())
        return None

    def has_child(name : str):
        return m_children.exists(name)

    def get_num_children():
        return m_children.num()

    def get_full_name():
        if _m_name == '':
            return get_name()
        else:
            return m_name

    def get_parent():
        return m_parent

    def set_name(name : str):
        if self._m_name != '':
            uvm_report_error('INVSTM', '')
        super.set_name(name)
        self.m_set_full_name()

    def _m_set_full_name():
        if _m_parent is top or _m_parent is None:
            _m_name = get_name()
        else:
            _m_name = _m_parent.get_full_name()+'.'+get_name()

    def lookup(name : str):
        pass

    def get_depth() -> int:
        if m_name == '':
            return 0
        get_depth_cnt = 1

        for char in m_name:
            if '.' == m_name:
                get_depth_cnt += 1
        return get_depth_cnt

    def m_extract_name():
        pass

    def flush():
        pass

    def do_flush():
        pass

    def create(name : str):
        pass

    def clone():
        pass

    def create_component(requested_type : str, name : str):
        pass

    def create_object(requested_type : str, name : str = ''):
        pass

    def set_type_override():
        pass

    def set_type_override_by_type():
        pass

    def set_inst_override():
        pass

    def set_inst_override_by_type():
        pass

    def set_report_id_verbosity_hier():
        pass

    def set_report_severity_id_verbosity_hier():
        pass

    #FIXME many are leftout


    def build_phase(self, uvm_phase phase):
        self.m_buld_done = 1
        self.build()

    def build():
        self.m_buld_done = 1
    
    def connect_phase(self, uvm_phase phase):
        self.connect()

    def start_of_simulation_phase(self, uvm_phase):
        start_of_simulation()

    def end_of_elaboration_phase(self, phase : uvm_phase):
        end_of_elaboration()
    
    async def run_phase(self, phase : uvm_phase):
        run

    def extract_phase(self, phase : uvm_phase):
        extract()

    def check_phase(self, phase : uvm_phase):
        check()

    def report_phase(self, phase : uvm_phase):
        report()

    
    def do_kill_all():
        pass
    
    def kill():
        pass

