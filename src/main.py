from src.Terminal import terminal
from src.Exceptions import InvalidTaskSource
from .api import api
from src import handler, log

def main():
    log.get_log()

    print("===== Приём задач из внешнего источника =====")
    log.log_in("Приём задач из внешнего источник")
    source_api = api.ApiSource()

    if handler.check_source(source_api):
        log.log_in("SUCCESS")
    else:
        log.log_in("ERROR: Объект не является источником задач.")
        raise InvalidTaskSource(source_api)

    print("----- Обработка задач завершена -----\n")

    terminal.Terminal(source_api)
    
    return

    
if __name__ == "__main__":
    main()