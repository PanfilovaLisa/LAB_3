from src import protocol
    
def check_source(source) -> bool:
    if not isinstance(source, protocol.TaskSource):
        print("Ошибка. Объект не является источником.")
        return False
    return True

def get_all_task_handler(source) -> bool | dict:
    if check_source(source):
        return source.get_tasks()
    return False
