import logging

def get_log():
    logging.basicConfig(level=logging.INFO, filename='shell.log', format='%(asctime)s %(message)s')
    return


def log_in(line):
    """
    Делает запись в файле shell.log

    Аргументы:
        line - текст для записи
    """
    logging.info(line)
    return