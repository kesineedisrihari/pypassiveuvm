class uvm_object:

    use_uvm_seeding = 1
    m_inst_count = 0

    def __init__(self, name : str = ''):
        self.m_inst_id = m_inst_count ++
        self.m_leaf_name = name

    def reseed():
        pass

    def set_name(name : str):
        pass

    def get_name() -> str:
        return m_leaf_name

    def get_full_name() -> str:
        return get_name()

    def get_inst_id():
        return self.m_inst_id

    def get_inst_count():
        return m_inst_count

    def get_type():
        pass

    def get_type_name() -> str:
        pass

    def create() -> uvm_object:
        pass

    def print():
        pass

    def sprint():
        pass

    def do_print():
        pass

    def convert2string() -> str:
        return ''

    def record():
        pass

    def do_record():
        pass

    def copy():
        return self.copy()

    def do_copy():
        pass

    def compare(rhs):
        return lhs == rhs

    def do_compare(rhs):
        return 1

    def pack()-> int:
        pass

    def pack_bytes()-> int:
        pass

    def pack_ints()-> int:
        pass

    def do_pack():
        pass

    def unpack()->int:
        pass

    def unpack_bytes()->int:
        pass

    def unpack_ints()->int:
        pass

    def do_unpack():
        pass

    def set_int_local():
        pass

    def set_string_local():
        pass

    def set_object_local():
        pass

    def get_object_type():
        pass

    def uvm_object_utils:
        pass

    def clone():
        return self.copy()


    def get_name():
        pass

    str m_leaf_name

    int m_inst_id

    int m_inst_count

    #uvm_status_container __m_uvm_status_container = new

    def __m_uvm_field_automation(tmp_data__ : uvm_object, what__ : int, str__ : str):
        return

    #def m_get_report_object()-> uvm_report_object:

    #uvm_object uvm_global_copy_map[uvm_object];
