class uvm_report_object(uvm_object):

    def __init__(self, name : str = ''):
        super().__init__(name)


    def uvm_info(ID : str, MSG : str, VERBOSITY):
        if VERBOSITY == UVM_NONE:
            logger.info('[%s] %s', ID, MSG)
        elif VERBOSITY == UVM_WARNING and verbosity in [UVM_NONE]
            logger.info('[%s] %s', ID, MSG)
        elif VERBOSITY == UVM_HIGH and verbosity in [UVM_NONE]
            logger.info('[%s] %s', ID, MSG)
        elif VERBOSITY == UVM_LOW and verbosity in [UVM_NONE]
            logger.info('[%s] %s', ID, MSG)
        
    
    def uvm_error(ID : str, MSG : str):
        logger.error()

    def uvm_fatal(ID : str, MSG : str):
        logger.fatal('[%s] %s', ID, msg)
        sys.exit()
