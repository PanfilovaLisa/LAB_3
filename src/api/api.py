import typing
from src.Task import Task
import json
import os
import time
import src.TaskQueue as TaskQueue

class ApiSource:
    def __init__(self):
        ...

    
    def get_tasks(self) -> typing.Iterable[Task.Task]:
        queue = TaskQueue.TaskQueue()
        print("Выполняется запрос...")

        with open(os.path.join("src", "api", "data.json")) as file:
            data = list(json.load(file))

        for task in data:
            queue.add(Task.Task(payload=task['payload'], priority_level=task['priority']))
            
        # TaskList = [
        #     Task.Task(payload=tsk['payload'], priority_level=tsk['priority']) for tsk in data
        # ]

        # TaskDict = {
        #     task.id: task for task in TaskList
        # }

        time.sleep(1)
        print(f"Ответ получен. Кол-во задач: {len(queue)}\n")

        return queue