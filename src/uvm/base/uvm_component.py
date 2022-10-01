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

    def get_children():
        return self.m_children

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

    def _m_set_full_name():
        if _m_parent is top or _m_parent is None:
            _m_name = get_name()
        else:
            _m_name = _m_parent.get_full_name()+'.'+get_name()

        def build_phase(self, uvm_phase phase):
            pass

        def connect_phase(self, uvm_phase phase):
            pass

        async def run_phase(self):
            pass

        def do_kill_all():
            pass

        def kill():
            pass

