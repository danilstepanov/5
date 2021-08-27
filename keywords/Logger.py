import logging, os

logger = None


def _logger(filename=None):
    global logger
    if not logger:
        logger = logging.getLogger()
        if filename is not None:
            print 'Logfile : %s' % filename
            create_file_handler(logger, filename)
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter('%(filename)s [LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s] %(message)s'))
        handler.setLevel(logging.DEBUG)
        logger.setLevel(logging.DEBUG)
        logger.addHandler(handler)
        logger.name = filename
    else:
        if filename is not None:
            print 'NEW Logfile : %s' % filename
            logger.name = filename
            logger.removeHandler(get_file_handler(logger.handlers))
            create_file_handler(logger, filename)
    return logger


def get_file_handler(handlers):
    for hand in handlers:
        if hand.__class__ == logging.FileHandler:
            return hand


def create_file_handler(logger, file):
    filehandler = logging.FileHandler(file, 'w')
    filehandler.setFormatter(logging.Formatter('%(filename)-15s [LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s] %(message)s'))
    filehandler.setLevel(logging.DEBUG)
    logger.addHandler(filehandler)


def log(message):
    global logger
    logger = _logger()
    logger.info(message)


def get_logger(filename):
    global logger
    print 'Log file %s' % filename
    log_dir = '%s/Logs' % os.path.dirname(os.path.abspath(__file__))
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    logfile = '%s/%s.txt' % (log_dir, filename)
    logger = _logger(logfile)