import sys 
from src import handler

def Terminal(source) -> None:
    TaskCenter = handler.get_all_task_handler(source)
    
    print("Добро пожаловать в систему управления задачами!")
    
    while True:
        print("\nВыберите команду:")
        print("1. Просмотреть список всех задач")
        print("2. Отфильтровать задачи по статусу")
        print("3. Отфильтровать задачи по приоритету")
        print("4. Посмотреть подробную информацию о задаче")
        print("5. Завершить работу")
        
        line = sys.stdin.readline().strip()
        
        match line:
            case "1":
                print("\n=== Список всех задач ===")
                if len(TaskCenter) == 0:
                    print("Задач нет.")
                else:
                    for task in TaskCenter:
                        status_text = task.states[task._status]
                        print(f"Задача № {task.id}. Приоритет: {task.priority}. Статус: {status_text}")
                        print(f"   {task.payload}\n")
            
            case "2":
                print("\n=== Фильтрация по статусу ===")
                print("Доступные статусы: 0 - NotStarted, 1 - InWork, 2 - Finished")
                
                try:
                    status_input = input("Введите номер статуса: ").strip()
                    status_num = int(status_input)
                    
                    if status_num not in [0, 1, 2]:
                        print("Такого статуса нет.")
                        continue
                    
                    status_text = task.states[status_num]
                    filtered = TaskCenter.filter(lambda t: t._status == status_num)
                    
                    print(f"\n=== Задачи со статусом '{status_text}' ===")
                    found = False
                    for task in filtered:
                        found = True
                        print(f"Задача № {task.id}. Приоритет: {task.priority}")
                        print(f"   {task.payload}\n")
                    
                    if not found:
                        print(f"Задач со статусом '{status_text}' не найдено.")
                        
                except ValueError:
                    print("Ошибка: введите число.")
            
            case "3":
                print("\n=== Фильтрация по приоритету ===")
                print(f"Доступный диапазон приоритетов: от {TaskCenter._queue[0].priority_min if len(TaskCenter) > 0 else 1} до {TaskCenter._queue[0].priority_max if len(TaskCenter) > 0 else 3}")
                
                try:
                    min_priority = int(input("Введите минимальный приоритет: ").strip())
                    max_priority = int(input("Введите максимальный приоритет: ").strip())
                    
                    filtered = TaskCenter.filter(lambda t: min_priority <= t.priority <= max_priority)
                    
                    print(f"\n=== Задачи с приоритетом от {min_priority} до {max_priority} ===")
                    found = False
                    for task in filtered:
                        found = True
                        status_text = task.states[task._status]
                        print(f"Задача № {task.id}. Приоритет: {task.priority}. Статус: {status_text}")
                        print(f"   {task.payload}\n")
                    
                    if not found:
                        print("Задач в указанном диапазоне не найдено.")
                        
                except ValueError:
                    print("Ошибка: введите числа.")
            
            case "4":
                print("\n=== Подробная информация о задаче ===")
                try:
                    task_id = int(input("Введите номер задачи: ").strip())
                    
                    found_task = None
                    for task in TaskCenter:
                        if task.id == task_id:
                            found_task = task
                            break
                    
                    if found_task:
                        TaskInfo(found_task)
                    else:
                        print(f"Задача № {task_id} не найдена.")
                        
                except ValueError:
                    print("Ошибка: введите число.")
            
            case "5":
                break
            
            case _:
                print("Неизвестная команда. Пожалуйста, выберите 1-5.")

def TaskInfo(task):
    print(f"\n===== Задача № {task.id} =====")
    print(f"Описание: {task.payload}")
    print(f"Приоритет: {task.priority}")
    
    match task._status:
        case 0:
            print(f"Статус: NotStarted")
        case 1:
            print(f"Статус: InWork")
            print(f"Время начала выполнения: {task.start_time}")
        case 2:
            print(f"Статус: Finished")
            print(f"Время начала выполнения: {task.start_time}")
            print(f"Время завершения: {task.end_time}")
            duration = task.duration
            if duration != 0:
                print(f"Длительность выполнения: {duration[0]}ч {duration[1]}м {duration[2]}с")
    
    print(f"Время создания задачи: {task.make_time}")
    print("=" * 35)