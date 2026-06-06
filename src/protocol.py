import typing
from src.Task import Task

@typing.runtime_checkable
class TaskSource(typing.Protocol):
    """Источник задач должен уметь возвращать задачи"""
    def __init__(self):
        ...

    
    def get_tasks(self) -> dict:
        """Возращает задачи"""
        ...

