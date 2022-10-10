class uvm_root(uvm_component):
    __instance = None
    check_name = None:

    m_children = []

    def probe(self):
        parser = OptionParser()
        parser.add_option('-d', '--dumpdir', help = 'dump directory path')
        parser.add_option('-o', '--outdir', help = 'output directory path')
        parser.add_option('-c', '--UVM_CHECKNAME', help = 'check name')

        if self.options.outdir is not None:
            if not os.path.exists():
                sys.exit('outdir(%s) doesnot exist'%(self.options.outdir))
            else:
                if not os.path.exists(self.options.dumpdir):
                    sys.exit('dumpdir(%s) doesnot exists'%(self.options.dumpdir))
                else:
                    dumpdir = self.options.dumpdir

                self.WFP = os.path.join(self.options.dumpdir, 'verdi.fsdb')

            self.WFH = waveform.open(self.WFP)
            npisys.init(sys.argv)

    def __init__(self, isruncheck = False):
        super().__init__('__top__', None)
        self._m_get_config_db = {}
        self.probe()

    def get_type_name():
        return 'uvm_root'

    def get_virtual_interface(self, svinterface):
        for item in vars(svinterface):
            if isinstance(item, hierarchy):
                signal = self.WFH.sig_by_name()
                if signal is None:
                    sys.exit(signal)
                svinterface.item = signal.create_vct()

        return svinterface

    def set_config_db(self, name : str, svinterface):
        pass


    def m_find_all_recursively(sef):
        pass

    def build_phase(self, phase : uvm_phase):
        super().build_phase(phase)
        m_do_verbosity_settings()
        m_do_timeout_settings()
        m_do_start_settings()
        m_do_max_quit_settings()
        m_do_dump_args()

    def m_do_verbosity_settings():
        pass

    def m_do_timeout_settings():
        pass

    def m_do_start_settings():
        pass

    def m_do_max_quit_settings():
        pass

    def m_do_dump_args():
        pass

    def die():
        pass

    def print_topology(self):
        if len(m_children) == 0:
            uvm_report_warning('EMTCOMP', 'print_topology')

        for item in m_children:
            uvm_info('print_topology')

    def run_check(self, check_name : str = ''):
        testname_plusarg = False

        if check_name != '':
            if uvm_check_top is None:
                    if testname_plusarg:
                        msg = 'command line --UVM_CHECK'
                    else:
                        msg = 'call to run_check(%s)'%(check_name)

        if len(self.m.children) == 0:
            msg = 'No components instantiated'
            msg = msg + 'You must eithier instantiate'
            uvm_report_fatal('NOCOMP', msg)

        if check_name == '':
            uvm_check_top = factory.create_component_by_name(check_name)


    def m_run_phases(self):
        for item in m_children:
            m_children.build_phase()

        for item in m_children:
            m_children.connect_phase()

            self.waveform.close(self.WFH)
            npisys.end()

uvm_top = uvm_root()

def get_root():
    return uvm_top

def set_config_db(name : str, svinterface):
    uvm_top.set_config_db(name, svinterface)

def get_config_db(name : str):
    uvm_top = get_root()
    if name in uvm_top._m_get_config_db:
        return uvm_top._m_get_config_sb[str]
    else:
        sys.exit('%s not in _m_get_config_db'%())

def run_check(check_name = None):
    uvm_top = get_root()
    uvm_top.run_check(check_name)
    uvm_top = get_root()
    uvm_top.run_check(check_name)

def getval(vct):
    global ts
    vct.goto_time(ts-10)

    try:
        val = int(vct.value(waveform.VctFormat_e.DecStrVal)
    except:
        val = 0

    return val



