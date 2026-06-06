import sys 

def make_answer(tasks):
    TaskList=[]


def print_all_tasks(TaskCenter, key=1, NotStarted=True, inWork=True, Finished=False) -> str:
    """
    Выводит в консоль список задач. По умлочанию выводится список незавершенных задач, отсортированных в порядке убывания приоритета.
        key: int - ключ, которые указывает на сортировку, фильтрацию задач
        inWork: bool - отображение задач в работе
        NotStarted: bool - отображение не начатых задач
        Finished: bool - отображение законченных задач (по умлочанию False)

        Возможные ключи:
            1 - сортировка по убыванию приоритета
            2 - сортирвка по возрастанию приоритета
            3 - сортировка по убыванию времени создания задачи (она же сортировка по убыванию id - т.к. чем больше id, тем позже ыбыла создана задача)
            4 - сортировка по возрастанию времени создания задачи
            5 - сортировка по возрастанию времени начала выполнения задачи
            6 - сортировка по убыванию времени начала выполнения задачи
            7 - сортировка по возрастанию времени окончания выполнения задачи
            8 - сортировка по убыванию времени окончания задачи

    """
    TaskCenter=list(TaskCenter)
    TaskList=[]
    if NotStarted:
        taskFilter = filter(lambda x: x.status==0, TaskCenter)
        TaskList+=list(taskFilter)
    if inWork:
        taskFilter=filter(lambda x: x.status==1, TaskCenter)
        TaskList+=list(taskFilter)
    if Finished:
        taskFilter=filter(lambda x: x.status==2, TaskCenter)
        TaskList+=list(taskFilter)

    match key:
        case 1:
            TaskList.sort(key=lambda x: -x.priority)
        case 2:
            TaskList.sort(key=lambda x: x.proirity)
        case 3:
            TaskList.sort()
